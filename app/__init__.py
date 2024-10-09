from flask import Flask, render_template
from flask_migrate import Migrate

from app.config import Config
from app.shipping_form import ShippingForm

from app.models import Package, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def root_endpoint():
    return 'Package Tracker'


@app.route('/new_package', methods=['GET', 'POST'])
def form():
    form = ShippingForm()
    return render_template('shipping_request.html', form=form)
