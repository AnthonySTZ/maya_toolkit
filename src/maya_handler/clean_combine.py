import maya.cmds as cmds  # type: ignore


def clean_combine():
    objects = get_selected_objects()
    combine(objects)


def get_selected_objects():
    selection = cmds.ls(sl=True, o=True)
    if len(selection) < 2:
        raise RuntimeError("Please select at least two objects")
    return selection


def combine(objs):
    merged_name = objs[0] + "_merged"
    cmds.polyUnite(objs, ch=False, n=merged_name)
