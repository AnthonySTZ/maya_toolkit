import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection

reload(selection)


def clean_separate():
    faces = selection.get_selected_objects(flatten=False)
    separate(faces)


def separate(faces):
    name = faces[0].rstrip("Shape")
    cmds.polySeparate(faces, ch=False, n=name)
