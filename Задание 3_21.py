from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, 2 * b)

@lru_cache(None)
def games(h):
    if sum(h) >= 62:
        return "W"
    if any(games(m) == "W" for m in moves(h)):
        return 'P1'
    if all(games(m) == 'P1' for m in moves(h)):
        return 'B1'
    if any(games(m) == "B1" for m in moves(h)):
        return "P2"
    if all(games(m) == "P1" or games(m) == "P2" for m in moves(h)):
        return "B2"
    
for s in range(1, 55):
    if games((7, s)) is not None:
        print(s, games((7, s)))
