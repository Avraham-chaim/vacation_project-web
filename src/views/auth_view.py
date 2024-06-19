from flask import Blueprint, jsonify, render_template, redirect, session, url_for, request
from facades.auth_facade import AuthFacade
from facades.vacations_facade import VacationFacade
from models.client_errors import ValidationError, AuthError


# managing the entire view:
auth_blueprint = Blueprint("auth_view", __name__)

# create facades:
auth_facade = AuthFacade()
vacation_facade = VacationFacade()

# register new user:
@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    try:
        if request.method == "GET":
            return render_template("register.html", user={})
        auth_facade.register()
        return redirect(url_for("vacations_view.list"))
    except ValidationError as err:
        return render_template("register.html", error=err.message, user=err.model)

# login existing user:
@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "GET":
            err = request.args.get("error") # take error from url (if exists)
            return render_template("login.html", error=err, credentials={})
        auth_facade.login()
        return redirect(url_for("vacations_view.list"))
    except (ValidationError, AuthError) as err:
        return render_template("login.html", error=err.message, credentials=err.model)

# logout for user: 
@auth_blueprint.route("/logout")
def logout():
    auth_facade.logout()
    return redirect(url_for("home_view.home"))

@auth_blueprint.route("/get-session-data")
def get_session_data():
    return jsonify(session)

# end point to receive data from the front and update the likes accordingly
@auth_blueprint.route("/update-likes", methods=["POST"])
def update_likes():
    try:
        data = request.json
        vacation_facade.update_likes(data)
        return jsonify({"message":"Likes updated successfully"}), 200
    except Exception as err:
        return jsonify({"error": str(err)}), 400
