import src.logics as logics


def test_should_return_true_with_valid_face() -> None:
    face: str = "pCube1.f[1]"
    assert logics.is_face(face) == True


def test_should_return_true_with_invalid_face() -> None:
    face: str = "pCube1.e[1]"
    assert logics.is_face(face) == False


def test_should_return_face_number() -> None:
    face_number: int = 54
    face: str = f"pCylinder2.f[{face_number}]"
    assert logics.get_face_number_from(face) == 54


def test_should_return_list_of_faces_numbers() -> None:
    faces_numbers: list[int] = [12, 4, 456]
    faces: list[str] = [f"pCube12.f[{number}]" for number in faces_numbers]
    assert logics.extract_faces_from_selection(faces) == faces_numbers
