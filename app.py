"""Flask app for Cupcakes"""

from flask import Flask, jsonify, request, render_template

from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
# from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """Shows homepage"""
    return render_template("index.html")


@app.route("/api/cupcakes")
def get_all_cupcakes():
    """get data about all cupcakes. Outputs jsonified cupcake object for
       all cupcakes."""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """get data about a specific cupcake. Takes the cupcake_id from URL
       and outputs jsonified cupcake object"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a cupcake in database. Receives an entire cupcake
       object:
       {
           "flavor": "red velvet",
           "size": "large",
           "rating": 6,
           "image": ""
       }
        and outputs the created cupcake jsonified object.
       """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image') or None

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """update a cupcake in the database. Receives an entire cupcake
       object:
       {
           "flavor": "red velvet",
           "size": "large",
           "rating": 6,
           "image": ""
       }
       Will output updated cupcake jsonified object"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    cupcake.image = request.json.get('image') or None

    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Delete a cupcake from the database. Takes in cupcake_id from URL
       and outputs a jsonified "deleted" message if successful."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)

    db.session.commit()

    return jsonify(message="deleted")
