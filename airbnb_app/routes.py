from flask import Blueprint, jsonify, request, render_template , flash, redirect
from .models import DB, User, Listing
from .airbnb_optimize import get_optimal_pricing
from os import getenv
from dotenv import load_dotenv

load_dotenv()

airbnb_routes = Blueprint("airbnb_routes", __name__)

@airbnb_routes.route('/')
def default_route():
    return render_template('airbnb_op_layout.html')
    
@airbnb_routes.route("/users")
def list_users():
    # SELECT * FROM users
    users = User.query.all()
    print(users)   

    return render_template("users.html", message="Users and their listings", users=users)

@airbnb_routes.route("/users/add")
def add_user():
    return render_template("add_user.html")

@airbnb_routes.route("/users/create", methods=["POST"])
def create_user():
    
    users = User.query.all()

    name=request.form['name']
    
    #If the user doesn't already exist add to the user table
    print(User.query.filter(User.name == name).first())
    if user := User.query.filter(User.name == name).first() is None:
        # create user based on the username passed into the function
        
        user = User(id=len(users)+1, name=name)
        DB.session.add(user)
        DB.session.commit()
        flash(f"User {user.name} created successfully!", "success")

    
    return redirect(f"/users")

@airbnb_routes.route("/listings/add")
def add_listing():
    return render_template("add_listing.html")

@airbnb_routes.route("/listings/create", methods=["POST"])
def create_listings():

    listing = Listing(**request.form)
    
    DB.session.add(listing)
    DB.session.commit()
    flash(f"Listing {listings.name} created successfully!", "success")

    
    return redirect(f"/users")

@airbnb_routes.route("/listings/edit")
def edit_listing():
    return render_template("edit_listing.html")

@airbnb_routes.route("/listings/modify", methods=["POST"])
def modify_listings():

    listing = Listing(**request.form)
    
    DB.session.add(listing)
    DB.session.commit()
    flash(f"Listing {listings.name} created successfully!", "success")

    
    return redirect(f"/users")

@airbnb_routes.route("/listings/delete", methods=["POST"])
def delete_listings():
    
    return redirect(f"/users")


@airbnb_routes.route("/listings/update", methods=["POST"])
def update_listings():
    
    return redirect(f"/users")
