import maya.cmds as cmds  # type: ignore

from importlib import reload

from maya_handler import center_objects, pivot_to_bottom, selection, transform

reload(center_objects)
reload(pivot_to_bottom)
reload(selection)
reload(transform)


def center_floor():
    pivot_to_bottom.pivot_to_bottom()
    center_objects.center_objects()


def drop_to_floor():
    pivot_to_bottom.pivot_to_bottom()
    objects = selection.get_selected_objects()
    for obj in objects:
        floor_obj(obj)


def floor_obj(object):
    transform.freeze_transform(object)
    obj_pos = transform.get_obj_position_in_worldspace(object)
    cmds.move(0, -obj_pos[1], 0, object, ls=True)  # center object to floor
    transform.freeze_transform(object)
