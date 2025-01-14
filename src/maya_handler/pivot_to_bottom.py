import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection, transform

reload(selection)
reload(transform)


def pivot_to_bottom():
    objects = selection.get_selected_objects()
    for obj in objects:
        set_pivot_bottom(obj)


def get_y_min(obj):
    return cmds.exactWorldBoundingBox(obj)[1]


def set_pivot_bottom(obj):
    y_min = get_y_min(obj)
    pivot_pos = transform.get_pivot_pos_of(obj)
    pivot_pos[1] = y_min
    cmds.xform(obj, ws=True, piv=pivot_pos)
