from flask import Blueprint, Flask, render_template, send_file
from flask_bootstrap import Bootstrap
from os import listdir
from os import getcwd
from os.path import isfile, join, basename

GALLERY_PATH = getcwd() + '/catapp/static/img/gallery/'

frontend = Blueprint('frontend', __name__)

@frontend.route('/', methods=['GET'])
def home():
	return render_template('home.html'), 200

@frontend.route('/about', methods=['GET'])
def about():
	return render_template('about.html'), 200

@frontend.route('/gallery', methods=['GET'])
def gallery():
	img_list = [f for f in listdir(GALLERY_PATH) if isfile(join(GALLERY_PATH, f))]
	return render_template('gallery.html', img_list=img_list), 200

@frontend.route('/static/img/gallery/<image>', methods=['GET'])
def image(image):
	image = GALLERY_PATH + image
	return send_file(image, mimetype='image/gif'), 200

@frontend.route('/contact', methods=['GET', 'POST'])
def contact():
	return render_template('contact.html'), 200