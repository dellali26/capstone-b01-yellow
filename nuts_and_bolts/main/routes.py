from flask import Blueprint, render_template
from nuts_and_bolts import db
from nuts_and_bolts.models import Products

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/product_list')
def product_list():
    product_list = db.session.query(Products).order_by(Products.sku)
    return render_template('product_list.html', product_list=product_list)
