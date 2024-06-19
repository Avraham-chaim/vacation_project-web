from flask import Blueprint, render_template, send_file, redirect, session, url_for, request
from facades.vacations_facade import VacationFacade
from facades.auth_facade import AuthFacade
from models.role_model import RoleModel
from utils.image_handler import ImageHandler
from models.client_errors import ValidationError, AuthError

vacations_blueprint = Blueprint("vacations_view", __name__)

vacations_facades = VacationFacade()
auth_facade = AuthFacade()


@vacations_blueprint.route("/vacations")
def list():
    try:
        auth_facade.block_anonymous()
        user = session.get("current_user")
        vacations_facades.save_liked_vacations_in_session(user) 
        all_vacations = vacations_facades.all_vacations_by_order() # get all the vacations from db.
        if user["role_id"] == RoleModel.User.value: # check if the user is user or admin.
            return render_template("user_vacations.html", vacations=all_vacations, active="list") # if user => render to users vacations page.
        return render_template("admin_vacations.html", vacations=all_vacations, active="list") # if admin => render to admin vacations page.
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))

@vacations_blueprint.route("/vacations/images/<string:image_name>")
def get_image(image_name):
    image_path = ImageHandler.get_image_path(image_name)
    return send_file(image_path)

@vacations_blueprint.route("/vacations/new", methods=["GET", "POST"])
def insert():
    try:
        auth_facade.block_non_admin()
        countries = vacations_facades.get_all_countries()
        if request.method == "GET":
            return render_template("insert.html", active = "insert", countries = countries, vacation={})
        vacations_facades.add_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message)) # send error to url query string
    except ValidationError as err:

        # get inserted data  from the form:
        vacation = {
            "country_id": int(request.form.get("country_id")),
            "vacation_description":request.form.get("vacation_description"),
            "start_date":request.form.get("start_date"),
            "end_date":request.form.get("end_date"),
            "price":request.form.get("price"),
            "image":request.form.get("image")}
        return render_template("insert.html", error = err.message, countries = countries, vacation=vacation)


@vacations_blueprint.route("/vacations/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    try:
        auth_facade.block_non_admin()
        countries = vacations_facades.get_all_countries()
        if request.method == "GET":
            one_vacation = vacations_facades.get_one_vacation(id)
            return render_template("edit.html", vacation = one_vacation, countries = countries)
        vacations_facades.update_vacation()
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))    
    except ValidationError as err:

        # get original data:
        one_vacation = vacations_facades.get_one_vacation(id)

        # get edited data  from the form: 
        vacation = {
            "country_id": int(request.form.get("country_id")),
            "vacation_description":request.form.get("vacation_description"),
            "start_date":request.form.get("start_date"),
            "end_date":request.form.get("end_date"),
            "price":request.form.get("price"),
            "vacation_photo_filename": one_vacation["vacation_photo_filename"]}
        
        return render_template("edit.html", error = err.message, vacation = vacation, countries = countries) 
    except Exception as err:
        # get original data:
        one_vacation = vacations_facades.get_one_vacation(id)

        # get edited data  from the form: 
        vacation = {
            "country_id": int(request.form.get("country_id")),
            "vacation_description":request.form.get("vacation_description"),
            "start_date":request.form.get("start_date"),
            "end_date":request.form.get("end_date"),
            "price":request.form.get("price"),
            "vacation_photo_filename": one_vacation["vacation_photo_filename"]}
        
        return render_template("edit.html", error = err.message, vacation = vacation, countries = countries) 


@vacations_blueprint.route("/vacations/delete/<int:id>")
def delete(id):
    try:
        auth_facade.block_non_admin()
        vacations_facades.delete_vacation(id)
        return redirect(url_for("vacations_view.list"))
    except AuthError as err:
        return redirect(url_for("auth_view.login", error = err.message))

