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
        brewery_post = BreweryPost(title=form.title.data, text=form.text.data, user_id=current_user.id, beer=form.beer.data)
        db.session.add(brewery_post)
        db.session.commit()
        flash('Brewery Post Created')
        print('Brewery post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

@brewery_posts.route('/<int:brewery_post_id>')
def brewery_post(brewery_post_id):
    brewery_post = BreweryPost.query.get_or_404(brewery_post_id) 
    return render_template('brewery_post.html', title=brewery_post.title, beer=brewery_post.beer, date=brewery_post.date, post=brewery_post)

@brewery_posts.route('/<int:brewery_post_id>/update',methods=['GET','POST'])
@login_required
def update(brewery_post_id):
    brewery_post = BreweryPost.query.get_or_404(brewery_post_id)

    if brewery_post.author != current_user:
        abort(403)

    form = BreweryPostForm()

    if form.validate_on_submit():
        brewery_post.title = form.title.data
        brewery_post.text = form.text.data
        brewery_post.beer = form.beer.data
        db.session.commit()
        flash('Brewery Post Updated')
        return redirect(url_for('brewery_posts.brewery_post',brewery_post_id=brewery_post.id))

    elif request.method == 'GET':
        form.title.data = brewery_post.title
        form.text.data = brewery_post.text
        form.beer.data = brewery_post.beer

    return render_template('create_post.html',title='Updating',form=form)


@brewery_posts.route('/<int:brewery_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(brewery_post_id):

    brewery_post = BreweryPost.query.get_or_404(brewery_post_id)
    if brewery_post.author != current_user:
        abort(403)

    db.session.delete(brewery_post)
    db.session.commit()
    flash('Brewery Post Deleted')
    return redirect(url_for('core.index'))