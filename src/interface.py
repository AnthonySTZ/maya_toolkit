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
        self.init_logics()

    def init_ui(self) -> None:
        self.setWindowTitle("Maya Toolkit")
        self.setStyleSheet(
            """
                font-size: 10pt;
            """
        )

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.select_every_nth_btn = QPushButton("Select every nth faces")
        self.clean_combine_btn = QPushButton("Clean combine")
        self.clean_separate_btn = QPushButton("Clean separate")
        self.pivot_to_bottom_btn = QPushButton("Pivot to bottom")
        self.restore_translate_btn = QPushButton("Restore translate")
        self.center_objects_btn = QPushButton("Center objects")
        self.center_floor_btn = QPushButton("Center objects to floor")
        self.drop_to_floor_btn = QPushButton("Drop to floor")
        self.merge_curves_btn = QPushButton("Merge curves")

        main_layout.addWidget(self.select_every_nth_btn)
        main_layout.addWidget(self.clean_combine_btn)
        main_layout.addWidget(self.clean_separate_btn)
        main_layout.addWidget(self.pivot_to_bottom_btn)
        main_layout.addWidget(self.restore_translate_btn)
        main_layout.addWidget(self.center_objects_btn)
        main_layout.addWidget(self.center_floor_btn)
        main_layout.addWidget(self.drop_to_floor_btn)
        main_layout.addWidget(self.merge_curves_btn)

    def init_logics(self) -> None:
        self.select_every_nth_btn.clicked.connect(
            lambda _: SelectEveryNthDialog().exec_()
        )
        self.clean_combine_btn.clicked.connect(clean_combine.clean_combine)
        self.clean_separate_btn.clicked.connect(clean_separate.clean_separate)
        self.pivot_to_bottom_btn.clicked.connect(pivot_to_bottom.pivot_to_bottom)
        self.restore_translate_btn.clicked.connect(restore_translate.restore_translate)
        self.center_objects_btn.clicked.connect(center_objects.center_objects)
        self.center_floor_btn.clicked.connect(drop_to_floor.center_floor)
        self.drop_to_floor_btn.clicked.connect(drop_to_floor.drop_to_floor)
        self.merge_curves_btn.clicked.connect(merge_curves.merge_curves)


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
