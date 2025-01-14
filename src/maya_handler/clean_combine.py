import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection

reload(selection)


def clean_combine():
    objects = selection.get_selected_objects()
    combine(objects)


def combine(objs):
    merged_name = objs[0] + "_merged"
    cmds.polyUnite(objs, ch=False, n=merged_name)
