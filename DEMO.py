from typing import List, Set

def greedy_set_cover(universe, sets):
    uncovered = set(universe)
    chosen = []

    while uncovered:
        # Elegir el subconjunto que cubre más elementos no cubiertos
        best = max(sets, key=lambda s: len(s & uncovered), default=set())
        if not best:
            raise ValueError("No hay cobertura completa con los subconjuntos dados.")
        
        # Añadir el subconjunto elegido al conjunto de la solución
        chosen.append(best)
        uncovered -= best
        
        print(f"Subconjunto elegido: {best}, Elementos cubiertos: {best & uncovered}")
        print(f"Elementos aún por cubrir: {uncovered}")
    
    return chosen

# Demo
U = {1,2,3,4,5,6,7,8}
S = [{1,2,3}, {2,4}, {3,4,5}, {4,5,6,7}, {6,7,8}, {1,8}]
cover = greedy_set_cover(U, S)
print("Cobertura elegida:", cover, "| tamaño:", len(cover))

