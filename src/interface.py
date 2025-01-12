from maya import OpenMayaUI as omui
import maya.cmds as cmds
import os
from shiboken2 import wrapInstance
from PySide2.QtWidgets import QApplication, QDialog, QWidget


class TootlkitWindow(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Maya Toolkit")


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
