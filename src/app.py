from flask import Flask, render_template, request
from views.home_view import home_blueprint
from views.vacations_view import vacations_blueprint
from views.auth_view import auth_blueprint
from logging import getLogger, ERROR
from utils.app_config import AppConfig
from flask_limiter import Limiter, util


app = Flask(__name__)

Limiter(
    util.get_remote_address, # user remote ip address
    app = app, #our flask app object
    default_limits = ["10 per second"], # how many requests per window of time
    storage_uri = "memory://", #save data in memory (and not in some file)
    default_limits_exempt_when = lambda: "vacations/images" in request.url
)


app.secret_key = AppConfig.session_secret_key


app.register_blueprint(auth_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(vacations_blueprint)


@app.errorhandler(404)
def page_not_fount(error):
    return render_template("404.html")


@app.errorhandler(Exception)
def catch_all(error):
    print(error)
    error_message = error if AppConfig.is_development else "Some error, please try again."
    return render_template("500.html", error = error_message)


# Quiet consol:
getLogger("werkzeug").setLevel(ERROR)

# display website address on terminal
print("Listening on http://localhost:5000")

