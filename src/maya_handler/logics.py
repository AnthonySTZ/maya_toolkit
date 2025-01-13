def extract_faces_from_selection(selection: list[str]) -> list[int]:
    faces: list[int] = []
    for sel in selection:
        if is_face(sel):
            faces.extend(get_face_number_from(sel))
    return faces


def is_face(sel) -> bool:
    return ".f[" in sel


def get_face_number_from(face: str) -> list[int]:
    number: str = face.split(".f[")[1][:-1]
    if ":" not in number:
        return [int(number)]

    indices = list(map(int, number.split(":")))
    numbers = [i for i in range(indices[0], indices[1] + 1)]

    return numbers


def keep_every_nth(list_to_modify: list[int], n: int) -> list[int]:
    return list_to_modify[::n]
