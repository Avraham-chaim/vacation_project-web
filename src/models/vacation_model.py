import datetime


class VacationModel:

    def __init__(self, vacation_id, country_id, vacation_description, start_date, end_date, price, image):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.vacation_description = vacation_description
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.image = image

    # validating a new vacation:
    def Validate_insert(self):
        if not self.country_id: return "Missing Country id."
        if not self.vacation_description: return "Missing Vacation description."
        if not self.start_date: return "Missing Start Date."
        if not self.end_date: return "Missing End Date."
        if not self.price: return "Missing Price."
        if not self.image: return "Missing Image."
        if len(self.vacation_description) < 2 or len(self.vacation_description) > 300: return "vacation_description length must be 2 - 300 chars."
        if self.start_date > self.end_date: return "It is not allowed to choose an earlier end date from the beginning."
        time_now = datetime.date.today()
        time_now = str(time_now)
        if time_now > self.start_date: return "The start time is the past.."
        if float(self.price) < 0 or float(self.price) > 10000: return "price must be 0 - 10000 chars."
        return None
    
    def Validate_update(self):
        if not self.vacation_id: return "Missing Vacation id."
        if not self.country_id: return "Missing Country id."
        if not self.vacation_description: return "Missing Vacation description."
        if not self.start_date: return "Missing Start Date."
        if not self.end_date: return "Missing End Date."
        if not self.price: return "Missing Price."
        if len(self.vacation_description) < 2 or len(self.vacation_description) > 300: return "vacation_description length must be 2 - 300 chars."
        if self.start_date > self.end_date: return "It is not allowed to choose an earlier end date from the beginning."
        if float(self.price) < 0 or float(self.price) > 10000: return "price must be 0 - 10000 chars."
        return None    
