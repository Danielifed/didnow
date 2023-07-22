from flask import Blueprint, render_template

portfolio_app = Blueprint('portfolio_app', __name__)

@portfolio_app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
