import math
# Input (leaf node values)
values = [2, 3, 5, 9, 0, 1, 7, 5]
h = int(math.log2(len(values)))

def alphabeta(d, i, a, b, maxp):
    if d == h:
        return values[i]

    if maxp:
        for k in (0, 1):
            a = max(a, alphabeta(d+1, i*2+k, a, b, False))
            if a >= b: break
        return a
    else:
        for k in (0, 1):
            b = min(b, alphabeta(d+1, i*2+k, a, b, True))
            if b <= a: break
        return b

print("Optimal value:", alphabeta(0, 0, -1000, 1000, True))
