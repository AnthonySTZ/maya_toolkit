import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection

reload(selection)


def restore_translate():
    objects = selection.get_selected_objects()
    for obj in objects:
        restore_translate_to(obj)


def restore_translate_to(object):
    obj_pos = get_obj_position_in_worldspace(object)
    cmds.move(
        -obj_pos[0], -obj_pos[1], -obj_pos[2], object, a=True, ls=True, r=True
    )  # center object
    freeze_transform(object)
    cmds.move(*obj_pos, object, a=True, ls=True, r=True)  # move to previous position


def get_obj_position_in_worldspace(object):
    return list(cmds.getAttr(object + ".rotatePivot")[0])


def freeze_transform(object):
    cmds.makeIdentity(object, a=True)
