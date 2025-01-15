import maya.cmds as cmds  # type: ignore
from importlib import reload
from maya_handler import selection

reload(selection)


def select_contained_faces():
    edges = selection.get_selected_edges()
    print(edges)
