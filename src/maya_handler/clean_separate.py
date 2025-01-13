import maya.cmds as cmds  # type: ignore


def clean_separate() -> None:
    faces = get_selected_faces()
    separate(faces)


def get_selected_faces() -> None:
    return cmds.ls(sl=True, o=True)


def separate(faces: list[str]) -> None:
    name = faces[0].rstrip("Shape")
    cmds.polySeparate(faces, ch=False, n=name)
