import maya.cmds as cmds  # type: ignore


def clean_combine() -> None:
    pass


def get_selected_objects() -> list[str]:
    selection = cmds.ls(sl=True, o=True)
    if len(selection) < 2:
        raise RuntimeError("Please select at least two objects")
    return selection
