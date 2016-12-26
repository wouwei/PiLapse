"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from picam import app
from picam.Toolbox import camera



#INIT
Cam = camera.CameraToolbox()
Cam.Start_Capture()


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title= "Pi-Lapse",
        year=datetime.now().year,
        image = Cam.do.GetLastImage(),
        
    )

@app.route('/parameters')
def parameters():
    """Renders the parameter page."""
    return render_template(
        'parameters.html',
        title= "Pi-Lapse",
        year=datetime.now().year,
    )
