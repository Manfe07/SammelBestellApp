from flask import render_template

from app.module_main import bp

@bp.route('/')
def index():
    return render_template('index.html')