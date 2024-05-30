from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/services')
def services():
    return render_template('services.html')

@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@bp.route('/blog')
def blog():
    return render_template('blog.html')
