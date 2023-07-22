from flask import Blueprint, render_template

blog_app = Blueprint('blog_app', __name__)

@blog_app.route('/blog')
def blog():
    return render_template('blog.html')

