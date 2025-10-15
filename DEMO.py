from typing import List, Set

def set_cover(U, S):
    U = set(U); C = []
    while U:
        b = max(S, key=lambda s: len(s & U), default=set())
        g = b & U
        if not g: raise ValueError("No hay cobertura")
        C.append(b); U -= g
    return C

# Demo mínima
U = {1,2,3,4,5,6,7,8}
S = [{1,2,3}, {2,4}, {3,4,5}, {4,5,6,7}, {6,7,8}, {1,8}]
print(set_cover(U, S))


def vertex_cover_2approx(E):
    E = {tuple(e) for e in E}
    C = set()
    while E:
        u, v = E.pop()
        C |= {u, v}
        E = {e for e in E if u not in e and v not in e}
    return C

# Demo mínima
E = {(1,2),(2,3),(3,4),(4,1),(2,4)}
print(vertex_cover_2approx(E))


