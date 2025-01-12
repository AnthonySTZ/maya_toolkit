def extract_faces_from_selection(selection: list[str]) -> list[int]:
    faces: list[int] = []
    for sel in selection:
        if is_face(sel):
            faces.append(get_face_number_from(sel))
    return faces


def is_face(sel) -> bool:
    return ".f[" in sel


def get_face_number_from(face: str) -> int:
    return int(face.split(".f[")[1][:-1])
