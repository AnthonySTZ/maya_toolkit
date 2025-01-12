import src.logics as logics


def test_should_return_true_with_valid_face() -> None:
    face: str = "pCube1.f[1]"
    assert logics.is_face(face) == True


def test_should_return_true_with_invalid_face() -> None:
    face: str = "pCube1.e[1]"
    assert logics.is_face(face) == False
