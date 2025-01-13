import maya.cmds as cmds  # type: ignore


def pivot_to_bottom() -> None:
    obj = get_obj_selection()
    y_min = get_y_min(obj)
    set_pivot_y_axis(obj, y_min)


def get_obj_selection() -> None:
    selection = cmds.ls(sl=True, o=True)
    if not selection:
        raise RuntimeError("No selection, please select an object !")
    return selection[0]


def get_y_min(obj: str) -> float:
    return cmds.exactWorldBoundingBox(obj)[1]


def set_pivot_y_axis(obj: str, value: float) -> None:
    pivot_pos = cmds.xform(obj, q=True, ws=True, rp=True)
    pivot_pos[1] = value
    cmds.xform(obj, ws=True, piv=pivot_pos)
