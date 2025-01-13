import maya.cmds as cmds  # type: ignore


def clean_separate():
    faces = get_selected_faces()
    separate(faces)


def get_selected_faces():
    return cmds.ls(sl=True, o=True)


def separate(faces):
    name = faces[0].rstrip("Shape")
    cmds.polySeparate(faces, ch=False, n=name)
