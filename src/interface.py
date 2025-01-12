from importlib import reload

from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QPushButton

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

        self.checker_deselect_btn = QPushButton("Checker Deselect")
        main_layout.addWidget(self.checker_deselect_btn)

    def init_logics(self) -> None:
        self.checker_deselect_btn.clicked.connect(maya_handler.checker_deselect)


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
