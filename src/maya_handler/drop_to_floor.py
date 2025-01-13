import maya.cmds as cmds  # type: ignore

from importlib import reload

from maya_handler import center_objects, pivot_to_bottom

reload(center_objects)
reload(pivot_to_bottom)


def center_floor() -> None:
    pivot_to_bottom.pivot_to_bottom()
    center_objects.center_objects()


def drop_to_floor() -> None:
    pivot_to_bottom.pivot_to_bottom()
    objects = get_selected_objects()
    for obj in objects:
        floor_obj(obj)


def get_selected_objects() -> list[str]:
    sel = cmds.ls(sl=True, o=True)
    if not sel:
        raise RuntimeError("No selection, please select at least one object !")
    return sel


def floor_obj(object: str) -> None:
    obj_pos = get_obj_position_in_worldspace(object)
    cmds.move(0, -obj_pos[1], 0, object, ls=True)  # center object to floor
    freeze_transform(object)


def get_obj_position_in_worldspace(object: str) -> list[float]:
    return list(cmds.getAttr(object + ".rotatePivot")[0])


def freeze_transform(object: str) -> None:
    cmds.makeIdentity(object, a=True)
