import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection, logics

reload(selection)
reload(logics)


def select_contained_faces():
    selected_obj = selection.get_selected_objects()[0]
    selected_edges = selection.get_selected_objects(flatten=True)
    faces = cmds.polyListComponentConversion(
        selected_edges[0], fe=True, tf=True, bo=True
    )
    base_face_number = logics.extract_faces_from_selection(faces)[0]
    selection.select_faces_from(selected_obj, [base_face_number])
