# core/views.py 

from flask import render_template, request, Blueprint
from myapp.models import BreweryPost
core = Blueprint('core', __name__)

@core.route('/posts')
def index():
    page = request.args.get('page', 1, type=int)
    brewery_posts = BreweryPost.query.order_by(BreweryPost.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', brewery_posts=brewery_posts)

@core.route('/')
def info():
    return render_template('info.html')