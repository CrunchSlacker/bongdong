from flask import Blueprint, request, render_template
from flask.templating import render_template
from . import physics

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    answer = ''
    vi = request.form.get("Vi")
    vf = request.form.get("Vf")
    a = request.form.get("a")
    t = request.form.get("t")

    if vi != '':
        vi = float(vi)
    else:
        answer = physics.no_x(vi, vf, a, t)

    if vf != '':
        vf = float(vf)
    else:
        answer = physics.no_x(vi, vf, a, t)

    if a != '':
        a = float(a)
    else:
        answer = physics.no_x(vi, vf, a, t)

    if t != '':
        t = float(t)
    else:
        answer = physics.no_x(vi, vf, a, t)

   

    return render_template("no_x.html", ans=answer)