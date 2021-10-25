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