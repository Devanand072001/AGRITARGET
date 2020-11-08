from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .predict import get_noutput
from .cropdetails import get_data

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', current_url=request.path)


@main.route('/predict', methods=['POST', 'GET'])
def predict():
    v1 = float(request.form.get('temperature'))
    v2 = float(request.form.get('humidity'))
    v3 = float(request.form.get('ph'))
    v4 = float(request.form.get('rainfall'))
    v5 = float(request.form.get('water'))
    output = get_noutput(4, v1, v2, v3, v4, v5)
    print(output)
    return render_template('result.html', result=output)


@main.route('/crop/<crop>')
def crop_detail(crop):
    return render_template('crop.html', cropdict={'name': crop})


@main.route('/crop/<crop>/weather')
def crop_weather(crop):
    data = get_data(crop, 'weather')
    return render_template('crop_detail/crop_weather.html', data=data, crop=crop)


@main.route('/crop/<crop>/irrigation')
def crop_irrigation(crop):
    data = get_data(crop, 'irrigation')
    return render_template('crop_detail/crop_irrigation.html', data=data, crop=crop)


@main.route('/crop/<crop>/pest')
def crop_pest(crop):
    data = get_data(crop, 'pests')
    return render_template('crop_detail/crop_pest.html', data=data, crop=crop)


@main.route('/crop/<crop>/disease')
def crop_disease(crop):
    data = get_data(crop, 'diseases')
    return render_template('crop_detail/crop_disease.html', data=data, crop=crop)


@main.route('/crop/<crop>/fertilizer')
def crop_fertilizer(crop):
    data = get_data(crop, 'fertilizers')
    return render_template('crop_detail/crop_fertilizer.html', data=data, crop=crop)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
