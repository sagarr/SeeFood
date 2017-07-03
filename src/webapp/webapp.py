# all the imports
import os
import sys

# tell our app where our saved model is
# sys.path.append(os.path.abspath("../src"))
from .. import predict

from flask import Flask, request, render_template
from skimage import io

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file, webapp.py

# Load default config and override config from an environment variable
app.config.update(dict(
    MODEL='UNET_64x64',
    WEIGHTS_PATH=os.path.join(app.root_path, 'weights/weights.h5')
))

app.config.from_envvar('SEEFOOD_SETTINGS', silent=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    pic_url = request.form['pic_url']
    print("Predicting URL: {}".format(pic_url))

    img = io.imread(pic_url)

    return predict.predict_img(img)
