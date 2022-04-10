#error_pages/handlers.py
from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

# instead of app route we are doing this - flask is performing a lot on the backend for us 
@error_pages.app_errorhandler(404)
def error_404(error):
    #returning a tuple here 
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403 