import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def checker_deselect() -> None:
    selected_object = get_selected_object()
    selected_faces = get_selected_faces()
    selected_faces = logics.remove_every_nth(selected_faces, 2)

    print(selected_object)
    print(selected_faces)


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
