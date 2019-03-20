r = int(r/255)
g = int(g/255)
b = int(b/255)

def max(r,g,b):
    if r >= g:
        if r >= b:
            return r
        else:
            return b
    elif g >= b:
        return g
    else:
        return b

def min(r,g,b):
    if r >= g:
        if g >= b:
            return b
        else:
            return g
    elif r >= b:
        return b
    else:
        return r

max = max(r,g,b)
min = min(r,g,b)
delta = max - min

v = max

def h(r,g,b,delta,max):
    if delta == 0:
        return 0
    elif max == r:
        return 60 * (int((g - b) / delta) % 6)
    elif max == g:
        return 60 * (int((b - r) / delta) + 2)
    elif max == b:
        return 60 * (int((b - r) / delta) + 4)

def s(delta,max):
    if delta == 0:
        return 0
    else:
        return int(delta / max)


