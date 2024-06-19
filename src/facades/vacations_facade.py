from logic.vacations_logic import VacationsLogic
from flask import request, session
from models.vacation_model import VacationModel
from models.client_errors import ResourceNotFoundError, ValidationError



class VacationFacade:

    def __init__(self):
        self.logic = VacationsLogic() 
       
    # get one vacation:    
    def get_one_vacation(self, vacation_id):
        vacation = self.logic.get_one_vacation(vacation_id)
        if not vacation: raise ResourceNotFoundError(vacation_id) 
        return vacation
    
    # get all the vacations by order:
    def all_vacations_by_order(self):
        result = self.logic.get_all_vacations(in_order=True)
        for vacation in result:
            vacation["country_name"] = self.logic.get_country_name(vacation["country_id"])
            vacation["likes"] = self.logic.get_likes_count(vacation["vacation_id"])     
        return result

    # add vacation:
    def add_vacation(self):
        country_id = request.form.get("country_id")
        vacation_description = request.form.get("vacation_description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files["image"]
        vacation = VacationModel(None,country_id, vacation_description, start_date, end_date, price, image)
        error = vacation.Validate_insert()
        if error: raise ValidationError(error, vacation)
        self.logic.insert_new_vacation(country_id, vacation_description, start_date, end_date,  price, image)

    # update vacation:
    def update_vacation(self):
        vacation_id = request.form.get("vacation_id")
        country_id = request.form.get("country_id")
        vacation_description = request.form.get("vacation_description")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        price = request.form.get("price")
        image = request.files["image"]
        vacation = VacationModel(vacation_id, country_id, vacation_description, start_date, end_date, price, image)
        error = vacation.Validate_update()
        if error: raise ValidationError(error, vacation)    
        self.logic.update_vacation(country_id, vacation_description, start_date, end_date,  price, image, vacation_id)

    # delete vacation:
    def delete_vacation(self, vacation_id):
        self.logic.delete_vacation(vacation_id)  

    # get all the countries list:
    def get_all_countries(self):
        countries = self.logic.get_all_countries()  
        return countries
    
    # add like:
    def add_like_vacation(self, user_id, vacation_id):
        result = self.logic.add_like(user_id, vacation_id)
        return result

    # delete like:
    def delete_like_vacation(self, user_id, vacation_id):
        result = self.logic.delete_like(user_id, vacation_id)
        return result
    
    # get the likes from specific vacation:
    def get_likes_count(self, vacation_id):
        vacation_count = self.logic.get_likes_count(vacation_id)
        return vacation_count

    # save the like in the session:
    def save_liked_vacations_in_session(self, user):
        result = self.logic.get_likes_by_user(user["user_id"])
        liked_vacations = [vacation["vacation_id"] for vacation in result]
        user["liked_vacations"] = liked_vacations
        session["current_user"] = user

    # update the likes table:
    def update_likes(self, data):
        user_id = data.get("user_id")
        vacation_id = data.get("vacation_id")
        #if data.liked is tru then add the like to the table, if its false then delete it:
        self.logic.add_like(user_id, vacation_id) if data.get("liked") else self.logic.delete_like(user_id, vacation_id)         
    
    def close(self):
        self.logic.close()

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()

