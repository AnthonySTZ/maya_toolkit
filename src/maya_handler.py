import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def checker_deselect() -> None:
    selected_faces = get_selected_faces()
    selected_faces["face_selection"] = logics.remove_every_nth(
        selected_faces["face_selection"], 2
    )


def get_selected_faces() -> dict:
    selection = get_maya_selection()
    if not selection:
        raise RuntimeError("No selection found. Please select some faces.")
    selected_object = {"obj": selection[0].split(".")[0], "face_selection": []}
    selected_object["face_selection"] = logics.extract_faces_from_selection(selection)
    return selected_object


def get_maya_selection() -> list[str]:
    return cmds.ls(selection=True, flatten=True)
