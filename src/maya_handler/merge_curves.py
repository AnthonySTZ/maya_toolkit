import maya.cmds as cmds  # type: ignore
from importlib import reload

from maya_handler import selection, transform

reload(selection)
reload(transform)


def merge_curves():
    curves = selection.get_selected_objects()
    if len(curves) < 2:
        return
    for curve in curves:
        transform.freeze_transform(curve)
    curves_shapes = selection.get_shapes_of(curves)
    cmds.parent(curves_shapes[1:], curves[0], r=True, s=True)
    cmds.delete(curves[1:])
