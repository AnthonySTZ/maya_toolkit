import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def select_every_nth(n: str) -> None:
    if not n.isnumeric():
        return
    selected_object = get_selected_object()
    selected_faces = get_selected_faces()
    print(len(selected_faces))
    organize_selected_faces = reorganize_face_selection(selected_object, selected_faces)
    print(len(organize_selected_faces))
    new_selected_faces = logics.keep_every_nth(organize_selected_faces, int(n))
    select_faces(selected_object, new_selected_faces)


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


def reorganize_face_selection(obj: str, faces: list[int]) -> list[int]:
    start_face = get_start_face(obj, faces)
    output_faces = [start_face]
    recurse_faces(
        obj,
        start_face,
        faces,
        output_faces,
    )
    return output_faces


def convert_face_numbers_to_correct_faces_object(
    object: str, faces: list[int]
) -> list[str]:
    return [f"{object}.f[{face_number}]" for face_number in faces]


def recurse_faces(
    obj: str, current_face: int, selected_faces: list[int], output_faces: list[int]
) -> None:
    connected_faces = get_connected_faces(obj, current_face)
    print(connected_faces)
    for face in connected_faces:
        if face in output_faces:
            continue
        if face not in selected_faces:
            continue
        output_faces.append(face)
        recurse_faces(obj, face, selected_faces, output_faces)


def get_connected_faces(obj: str, face: int):
    edges = cmds.polyListComponentConversion(f"{obj}.f[{face}]", ff=True, te=True)
    connected_faces = cmds.polyListComponentConversion(edges, fe=True, tf=True)
    return logics.extract_faces_from_selection(connected_faces)


def get_start_face(obj: str, faces: list[int]) -> int:
    boudaries = select_by_number_of_neighbours(obj, faces, 1)
    if boudaries:
        return boudaries[0]
    return faces[0]


def select_by_number_of_neighbours(
    obj: str, faces: list[int], nb_of_neighbours: int
) -> list[int]:
    output_faces: list[int] = []
    for face in faces:
        connected_faces = get_connected_faces(obj, face)
        selected_connected_faces = [
            conn_face for conn_face in connected_faces if conn_face in faces
        ]
        if len(selected_connected_faces) == nb_of_neighbours:
            output_faces.append(face)
    return output_faces


def select_faces(obj: str, faces: list[int]) -> None:
    format_faces = convert_face_numbers_to_correct_faces_object(obj, faces)
    cmds.select(clear=True)
    cmds.select(format_faces)
