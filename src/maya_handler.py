import maya.cmds as cmds


def checker_deselect() -> None:
    selected_faces = get_selected_faces()
    print(selected_faces)


def get_selected_faces() -> dict[str : list[int]]:
    selection = get_maya_selection()
    if not selection:
        raise RuntimeError("No selection found. Please select some faces.")
    selected_object = selection[0].split(".")[0]
    selected_faces = extract_faces_from_selection(selection)
    return {selected_object: selected_faces}


def get_maya_selection() -> list[str]:
    return cmds.ls(selection=True, flatten=True)


def extract_faces_from_selection(selection: list[str]) -> list[int]:
    faces: list[int] = []
    for sel in selection:
        if is_face(sel):
            faces.append(get_face_number_from(sel))
    return faces


def is_face(sel) -> bool:
    return ".f[" in sel


def get_face_number_from(face: str) -> int:
    return face.split(".f[")[1][:-1]
