# all the imports
import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file, webapp.py

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
    return "Vada Pav"