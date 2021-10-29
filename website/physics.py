import math

def no_x(vi, vf, a, t):

    if vf == "":
        v = float(vi) + (float(a) * float(t))
        return "vf = " + str(v)
    if vi == "":
        v0 = float(vf) / (float(a) * float(t))
        return "vi = " + str(v0)
    if a == "":
        a = (float(vf) - float(vi)) / float(t)
        return "a = " + str(a)
    if t == "":
        t = (float(vf) - float(vi)) / float(a)
        return "t = " + str(t)

def no_a(x, vi, vf, t):
    if x == "":
        x = 0.5 * (float(vf) + float(vi)) * float(t)
        return "x = " + str(x)
    if vf == "":
        vt = 2 * (float(x) / float(t)) - float(vi)
        return "vf = " + str(vt)
    if vi == "":
        v0 = 2 * (float(x) / float(t)) - float(vf)
        return "vi = " + str(v0)
    if t == "":
        t = (2 * float(x)) / (float(vf) + float(vi))
        return "t = " + str(t)

def no_t(x, vi, vf, a):
    if a == "":
        a = ((pow(float(vf), 2) - pow(float(vi), 2)) / (2 * float(x)))
        return "a = " + str(a)
    if x == "":
        x = ((pow(float(vf), 2) - pow(float(vi), 2)) / (2 * float(a)))
        return "x = " + str(x)
    if vf == "":
        vt = math.sqrt((2 * float(a) * float(x)) + pow(float(vi), 2))
        return "vf = " + str(vt)
    if vi == "":
        v0 = math.sqrt((-2 * float(a) * float(x)) + pow(float(vf), 2))
        return "vi = " + str(v0)

def no_vf(x, vi, a, t):
    if x == "":
        x = (float(vi) * float(t)) + (0.5 * float(a) * pow(float(t), 2))
        return "x = " + str(x)
    if vi == "":
        vo = ((2 * float(x)) - (float(a) * pow(float(t), 2))) / (2 * float(t))
        return "vi = " + str(vo)
    if t == "":
        t = (-float(vi) + math.sqrt(2 * float(a) * float(x) + pow(float(vi), 2)))
        return "t = " + str(t)
    if a == "":
        a = ((2 * float(x)) - (2 * float(vi) * float(t)))
        return "a = " + str(a)