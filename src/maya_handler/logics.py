def extract_faces_from_selection(selection):
    faces = []
    for sel in selection:
        if is_face(sel):
            faces.extend(get_component_number_from(sel, "f"))
    return faces


def extract_edges_from_selection(selection):
    edges = []
    for sel in selection:
        if is_edge(sel):
            edges.extend(get_component_number_from(sel, "e"))
    return edges


def is_face(sel):
    return ".f[" in sel


def is_edge(sel):
    return ".e[" in sel


def get_component_number_from(component, type):
    number = component.split("." + type + "[")[1][:-1]
    if ":" not in number:
        return [int(number)]

    indices = list(map(int, number.split(":")))
    numbers = [i for i in range(indices[0], indices[1] + 1)]

    return numbers


def keep_every_nth(list_to_modify, n):
    return list_to_modify[::n]


def convert_face_numbers_to_correct_faces_object(object, faces):
    return [f"{object}.f[{face_number}]" for face_number in faces]
