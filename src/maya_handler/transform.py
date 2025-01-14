import maya.cmds as cmds  # type: ignore


def get_obj_position_in_worldspace(object):
    return list(cmds.getAttr(object + ".rotatePivot")[0])


def freeze_transform(object):
    cmds.makeIdentity(object, a=True)


def get_pivot_pos_of(object):
    return cmds.xform(object, q=True, ws=True, rp=True)
