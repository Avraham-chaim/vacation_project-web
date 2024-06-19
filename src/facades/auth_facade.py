from logic.auth_logic import AuthLogic
from flask import request, session
from models.user_model import UserModel
from models.credentials_model import CredentialsModel
from models.role_model import RoleModel
from models.client_errors import ValidationError, AuthError
from utils.cyber import Cyber


class AuthFacade:

    def __init__(self):
        self.logic = AuthLogic()

    # register a new user:
    def register(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UserModel(None, first_name, last_name, email, password,RoleModel.User.value)
        error = user.Validate_insert()
        if error: raise ValidationError(error, user)
        if self.logic.is_email_taken(email): raise ValidationError("Email already exists.", user)
        user.password = Cyber.hash(user.password)
        self.logic.add_user(user)
        user = self.logic.get_user(user.email, user.password) # get the dictionary user from database
        del user["password"] # remove password from session.
        session["current_user"] = user # save the user inside the session dictionary
    
    # login
    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialsModel(email, password)
        error = credentials.Validate()
        if error: raise ValidationError(error, credentials)
        hashed_password = Cyber.hash(credentials.password)
        user = self.logic.get_user(credentials.email, hashed_password)
        if not user: raise AuthError("Incorrect email or password.", credentials)
        del user["password"] # remove password from session.               
        session["current_user"] = user # save the user inside the session dictionary
        
    # logout for user
    def logout(self):
        session.clear() # clear session for logout    

    # block non logged-in users:
    def block_anonymous(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged_in.")

    # block non admin users:
    def block_non_admin(self):
        user = session.get("current_user")
        if not user: raise AuthError("You are not logged_in.")
        if user["role_id"] != RoleModel.Admin.value: raise AuthError("You are not allowed.")   

    # close connection:
    def close(self):
        self.dal.close()    
    




