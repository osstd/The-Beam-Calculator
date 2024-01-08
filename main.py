from flask import Flask, render_template, request
from calculator import Calculator
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('F_KEY')

beam_list = [
    {'name': 'Simply Supported Beam - UDL', 'path': 'assets/img/ss_udl.jpg', 'id': 0},
    {'name': 'Simply Supported Beam - Point Load', 'path': 'assets/img/ss_pl.jpg', 'id': 1},
    {'name': 'Simply Supported Beam - Two Point Load', 'path': 'assets/img/ss_2pl.jpg', 'id': 2},
    {'name': 'Cantilever Beam - UDL', 'path': 'assets/img/cant_udl.jpg', 'id': 3},
    {'name': 'Cantilever Beam - TDL', 'path': 'assets/img/cant_tdl.jpg', 'id': 4},
    {'name': 'Cantilever Beam - Point Load', 'path': 'assets/img/cant_pl.jpg', 'id': 5}
]


@app.route('/')
def index():
    return render_template('home.html', home=True, beam_list=beam_list)


@app.route('/beam/<int:beam_id>')
def beam_home(beam_id):
    beam_dict = beam_list[beam_id]
    return render_template('home.html', beam_dict=beam_dict, choice=True)


@app.route('/calculate/<int:beam_id>', methods=['GET', 'POST'])
def calculate(beam_id):
    if request.method == 'POST':
        beam_dict = beam_list[beam_id]
        length = float(request.form['length'])
        load = float(request.form['load'])
        calculator = Calculator(length, load)
        if beam_id == 0 or beam_id == 3 or beam_id == 4:
            if beam_id == 0:
                points, shear_force, bending_moment = calculator.ss_udl()
            elif beam_id == 3:
                points, shear_force, bending_moment = calculator.cant_udl()
            else:
                points, shear_force, bending_moment = calculator.cant_tpl()

        else:
            force_location = float(request.form['location'])
            message = "Error, don't input the load at the support location!"
            if beam_id == 1:
                try:
                    points, shear_force, bending_moment = calculator.ss_pl(force_location)
                except TypeError:
                    return render_template('home.html', error=message, beam_id=beam_id)
            elif beam_id == 2:
                try:
                    points, shear_force, bending_moment = calculator.ss_2pl(force_location)
                except TypeError:
                    return render_template('home.html', error=message, beam_id=beam_id)
            else:
                try:
                    points, shear_force, bending_moment = calculator.cant_pl(force_location)
                except TypeError:
                    return render_template('home.html', error=message, beam_id=beam_id)

        if 'superimpose' in request.form:
            return render_template('home.html', plot=True, superimpose=True, beam_dict=beam_dict, length=points,
                                   shear=shear_force, moment=bending_moment)

        if '2-plots' in request.form:
            return render_template('home.html', plot=True, choice=False, superimpose=False, beam_dict=beam_dict,
                                   length=points, shear=shear_force, moment=bending_moment)


if __name__ == '__main__':
    app.run(debug=True)
