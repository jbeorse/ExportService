"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ExportService import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/export')
def export():
    """Renders the export test."""
    return render_template(
        'export.html',
        name='test',
        year=datetime.now().year,
    )
    
    
