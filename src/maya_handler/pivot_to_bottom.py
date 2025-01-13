import maya.cmds as cmds  # type: ignore


def pivot_to_bottom():
    objects = get_obj_selection()
    for obj in objects:
        set_pivot_bottom(obj)


def get_obj_selection():
    selection = cmds.ls(sl=True, o=True)
    if not selection:
        raise RuntimeError("No selection, please select an object !")
    return selection


def get_y_min(obj):
    return cmds.exactWorldBoundingBox(obj)[1]


def set_pivot_bottom(obj):
    y_min = get_y_min(obj)
    pivot_pos = cmds.xform(obj, q=True, ws=True, rp=True)
    pivot_pos[1] = y_min
    cmds.xform(obj, ws=True, piv=pivot_pos)
