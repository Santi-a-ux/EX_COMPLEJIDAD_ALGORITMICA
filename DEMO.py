from typing import List, Set

def greedy_set_cover(universe: Set[int], sets: List[Set[int]]) -> List[Set[int]]:
    uncovered = set(universe)
    chosen: List[Set[int]] = []
    candidates = [s.copy() for s in sets]

    while uncovered:
        best = max(candidates, key=lambda s: len(s & uncovered), default=set())
        gain = best & uncovered
        if not gain:
            raise ValueError("No hay cobertura completa con los subconjuntos dados.")
        chosen.append(best)
        uncovered -= gain
    return chosen

# Demo
U = {1,2,3,4,5,6,7,8}
S = [{1,2,3}, {2,4}, {3,4,5}, {4,5,6,7}, {6,7,8}, {1,8}]
cover = greedy_set_cover(U, [set(x) for x in S])
print("Cobertura elegida:", cover, "| tamaño:", len(cover))
