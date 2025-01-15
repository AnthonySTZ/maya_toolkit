from importlib import reload

from maya import OpenMayaUI as omui  # type: ignore
from shiboken2 import wrapInstance
from PySide2.QtWidgets import (
    QApplication,
    QDialog,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QLineEdit,
)
from PySide2.QtGui import QIntValidator
from PySide2.QtCore import Qt
import maya_handler

reload(maya_handler)
from maya_handler import (
    drop_to_floor,
    select_every,
    clean_combine,
    clean_separate,
    pivot_to_bottom,
    restore_translate,
    center_objects,
    merge_curves,
)

reload(select_every)
reload(clean_combine)
reload(clean_separate)
reload(pivot_to_bottom)
reload(restore_translate)
reload(center_objects)
reload(drop_to_floor)
reload(merge_curves)


class TootlkitWindow(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle("Maya Toolkit")
        self.setStyleSheet(
            """
                font-size: 10pt;
            """
        )

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        selection_row = Row(
            "Selection",
            [
                ["Select every nth faces", lambda _: SelectEveryNthDialog().exec_()],
                ["Contained faces", lambda _: print("Yes")],
            ],
        )

        object_row = Row(
            "Object",
            [
                ["Clean combine", clean_combine.clean_combine],
                ["Clean separate", clean_separate.clean_separate],
                ["Merge curves", merge_curves.merge_curves],
            ],
        )

        transform_row = Row(
            "Transform",
            [
                ["Center objects", center_objects.center_objects],
                ["Center objects to floor", drop_to_floor.center_floor],
                ["Drop to floor", drop_to_floor.drop_to_floor],
                ["Pivot to bottom", pivot_to_bottom.pivot_to_bottom],
                ["Restore translate", restore_translate.restore_translate],
            ],
        )

        main_layout.addWidget(selection_row)
        main_layout.addWidget(object_row)
        main_layout.addWidget(transform_row)


class Row(QWidget):
    def __init__(self, name, items):
        super().__init__()
        self.init_ui(name, items)

    def init_ui(self, name, items):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)
        main_layout.setContentsMargins(0, 0, 0, 0)

        title = QLabel(name)
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        row_layout = QHBoxLayout()
        row_widget = QWidget()
        row_widget.setStyleSheet(
            """
                .QWidget{
                    border-top: 1px solid grey;
                }
            """
        )
        row_widget.setLayout(row_layout)

        for item in items:
            btn = QPushButton(item[0])
            btn.clicked.connect(item[1])
            row_layout.addWidget(btn)

        main_layout.addWidget(row_widget)


class SelectEveryNthDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.init_ui()
        self.init_logics()

    def init_ui(self) -> None:
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        self.setStyleSheet(
            """
                font-size: 10pt;
            """
        )

        select_every_label = QLabel("Select every")
        self.select_every_le = QLineEdit()
        self.select_every_le.setValidator(QIntValidator(1, 999, self))
        faces_label = QLabel("faces")
        self.select_every_nth_btn = QPushButton("Confirm")

        main_layout.addWidget(select_every_label)
        main_layout.addWidget(self.select_every_le)
        main_layout.addWidget(faces_label)
        main_layout.addWidget(self.select_every_nth_btn)

    def init_logics(self) -> None:
        self.select_every_nth_btn.clicked.connect(self.select_every_nth)

    def select_every_nth(self) -> None:
        select_every.select_every_nth(self.select_every_le.text())
        self.close()


def create_window():
    if QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QApplication.allWindows():
            if (
                "Maya Toolkit" in win.objectName()
            ):  # update this name to match name below
                win.destroy()

    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

    dialog = TootlkitWindow
    dialog.window = dialog(parent=mayaMainWindow)
    dialog.window.setObjectName(
        str(dialog.__name__)
    )  # code above uses this to ID any existing windows
    dialog.window.show()
