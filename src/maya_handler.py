import maya.cmds as cmds  # type: ignore
from importlib import reload
import logics

reload(logics)


def select_every_nth(n: str) -> None:
    if not n.isnumeric():
        return
    selected_object = get_selected_object()
    selected_faces = get_selected_faces()
    start_face = get_start_face(selected_object, selected_faces)
    output_faces = [start_face]
    recurse_faces(
        selected_object,
        start_face,
        selected_faces,
        output_faces,
    )
    new_selected_faces = logics.keep_every_nth(output_faces, int(n))
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


def recurse_faces(
    obj: str, current_face: int, selected_faces: list[int], output_faces: list[int]
) -> None:
    connected_faces = get_connected_faces(f"{obj}.f[{current_face}]")
    for face in logics.extract_faces_from_selection(connected_faces):
        if face in output_faces:
            continue
        if face not in selected_faces:
            continue
        output_faces.append(face)
        recurse_faces(obj, face, selected_faces, output_faces)


def get_connected_faces(face: str):
    edges = cmds.polyListComponentConversion(face, ff=True, te=True)
    connected_faces = cmds.polyListComponentConversion(edges, fe=True, tf=True, bo=True)
    return connected_faces


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
        connected_faces = logics.extract_faces_from_selection(
            get_connected_faces(f"{obj}.f[{face}]")
        )
        selected_connected_faces = [
            conn_face for conn_face in connected_faces if conn_face in faces
        ]
        if len(selected_connected_faces) == nb_of_neighbours:
            output_faces.append(face)
    return output_faces
