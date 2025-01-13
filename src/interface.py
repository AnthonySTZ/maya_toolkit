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

        main_layout.addWidget(self.select_every_nth_btn)

    def init_logics(self) -> None:
        self.select_every_nth_btn.clicked.connect(
            lambda _: SelectEveryNthDialog().exec_()
        )


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
        maya_handler.select_every_nth(self.select_every_le.text())
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
