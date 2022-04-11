from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import BreweryPost
from myapp.brewery_posts.forms import BreweryPostForm

brewery_posts = Blueprint('brewery_posts', __name__)

@brewery_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = BreweryPostForm()
    if form.validate_on_submit():
        brewery_post = BreweryPost(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(brewery_post)
        db.session.commit()
        flash('Brewery Post Created')
        print('Brewery post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

@brewery_posts.route('/<int:brewery_post_id>')
def brewery_post(brewery_post_id):
    brewery_post = BreweryPost.query.get_or_404(brewery_post_id) 
    return render_template('brewery_post.html', title=brewery_post.title, date=brewery_post.date, post=brewery_post)

