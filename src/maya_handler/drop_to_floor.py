import maya.cmds as cmds  # type: ignore

from importlib import reload

from maya_handler import center_objects, pivot_to_bottom, selection

reload(center_objects)
reload(pivot_to_bottom)
reload(selection)


def center_floor():
    pivot_to_bottom.pivot_to_bottom()
    center_objects.center_objects()


def drop_to_floor():
    pivot_to_bottom.pivot_to_bottom()
    objects = selection.get_selected_objects()
    for obj in objects:
        floor_obj(obj)


def floor_obj(object):
    freeze_transform(object)
    obj_pos = get_obj_position_in_worldspace(object)
    cmds.move(0, -obj_pos[1], 0, object, ls=True)  # center object to floor
    freeze_transform(object)


def get_obj_position_in_worldspace(object):
    return list(cmds.getAttr(object + ".rotatePivot")[0])


def freeze_transform(object):
    cmds.makeIdentity(object, a=True)
