import maya.cmds as cmds  # type: ignore
from importlib import reload

from maya_handler import logics

reload(logics)


def get_selected_objects(flatten=False):
    sel = cmds.ls(sl=True, o=not flatten, flatten=flatten)
    if not sel:
        raise RuntimeError("No selection, please select at least one object !")
    return sel


def get_selected_faces():
    selection = get_selected_objects(flatten=True)
    selected_faces = logics.extract_faces_from_selection(selection)
    return selected_faces


def select_faces_from(obj, faces):
    format_faces = logics.convert_face_numbers_to_correct_faces_object(obj, faces)
    cmds.select(clear=True)
    cmds.select(format_faces)
