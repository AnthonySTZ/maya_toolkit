import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def checker_deselect() -> None:
    selected_object = get_selected_object()
    selected_faces = get_selected_faces()
    new_selected_faces = logics.remove_every_nth(selected_faces, 2)
    new_selection = convert_face_numbers_to_correct_faces_object(
        new_selected_faces, selected_object
    )
    cmds.select(clear=True)
    cmds.select(new_selection)


def get_selected_object() -> str:
    selection = get_maya_selection()
    selected_object = selection[0].split(".")[0]
    return selected_object


def get_selected_faces() -> list[int]:
    selection = get_maya_selection()
    selected_faces = logics.extract_faces_from_selection(selection)
    return selected_faces


def get_maya_selection() -> list[str]:
    selection = cmds.ls(selection=True, flatten=True)
    if not selection:
        raise RuntimeError("No selection found. Please select some faces.")
    return selection


def convert_face_numbers_to_correct_faces_object(
    faces: list[int], object: str
) -> list[str]:
    return [f"{object}.f[{face_number}]" for face_number in faces]
