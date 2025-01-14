import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection

reload(selection)


def center_objects():
    objects = selection.get_selected_objects()
    for obj in objects:
        center_obj(obj)


def center_obj(object):
    obj_pos = get_obj_position_in_worldspace(object)
    cmds.move(
        -obj_pos[0], -obj_pos[1], -obj_pos[2], object, a=True, ls=True, r=True
    )  # center object
    freeze_transform(object)


def get_obj_position_in_worldspace(object):
    return list(cmds.getAttr(object + ".rotatePivot")[0])


def freeze_transform(object) -> None:
    cmds.makeIdentity(object, a=True)
