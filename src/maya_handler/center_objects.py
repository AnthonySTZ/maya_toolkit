import maya.cmds as cmds  # type: ignore


def center_objects() -> None:
    objects = get_selected_objects()
    for obj in objects:
        center_obj(obj)


def get_selected_objects() -> list[str]:
    sel = cmds.ls(sl=True, o=True)
    if not sel:
        raise RuntimeError("No selection, please select at least one object !")
    return sel


def center_obj(object: str) -> None:
    pass
