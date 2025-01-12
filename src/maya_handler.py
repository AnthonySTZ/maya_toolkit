import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def checker_deselect() -> None:
    selected_faces = get_selected_faces()
    print(selected_faces)


def get_selected_faces() -> dict[str : list[int]]:
    selection = get_maya_selection()
    if not selection:
        raise RuntimeError("No selection found. Please select some faces.")
    selected_object = selection[0].split(".")[0]
    selected_faces = logics.extract_faces_from_selection(selection)
    return {selected_object: selected_faces}


def get_maya_selection() -> list[str]:
    return cmds.ls(selection=True, flatten=True)
