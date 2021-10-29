from flask import Blueprint, request, render_template
from flask.templating import render_template
from . import physics
from website import physics


views = Blueprint('views', __name__)

@views.route('/no_x', methods=['GET', 'POST'])
def kinematics():

    answer = 0
    x = request.form.get("x")
    vi = request.form.get("vi")
    vf = request.form.get("vf")
    a = request.form.get("a")
    t = request.form.get("t")

    print(vi)
    print(vf)
    print(a)
    print(t)

    if x == "":
        print("x")
        answer = physics.no_x(vi, vf, a, t)
    if a == "":
        print("a")
        answer = physics.no_a(x, vi, vf, t)
    if t == "":
        print("t")
        answer = physics.no_t(x, vi, vf, a)
    if vf == "":
        print("vf")
        answer = physics.no_vf(x, vi, a, t)

    return render_template("Kinematics.html", ans=answer)

