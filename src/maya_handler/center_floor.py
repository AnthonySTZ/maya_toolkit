import maya.cmds as cmds  # type: ignore

from importlib import reload

from maya_handler import center_objects, pivot_to_bottom

reload(center_objects)
reload(pivot_to_bottom)


def center_floor() -> None:
    pivot_to_bottom.pivot_to_bottom()
    center_objects.center_objects()
