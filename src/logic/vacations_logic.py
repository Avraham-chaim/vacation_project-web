from utils.dal import DAL
from utils.image_handler import ImageHandler


class VacationsLogic:

    def __init__(self):
        self.dal = DAL()    

    def get_all_vacations(self, in_order=None):
        if in_order:
            sql = "SELECT * FROM vacations ORDER BY start_date, end_date ASC"
        else:
            sql = "SELECT * FROM vacations"
        return self.dal.get_table(sql)
    
    def get_one_vacation(self, vacation_id):
        sql = "SELECT * FROM vacations WHERE vacation_id=%s"
        return self.dal.get_scalar(sql, (vacation_id,))

    def insert_new_vacation(self, country_id, vacation_description, start_date, end_date,  price, image):
        image_name = ImageHandler.save_image(image)
        sql = ("INSERT INTO vacations(country_id, vacation_description,start_date, end_date, price, vacation_photo_filename) VALUES(%s, %s, %s, %s, %s, %s)")
        data = (country_id, vacation_description, start_date, end_date,  price, image_name)
        return self.dal.insert(sql, data)

    def update_vacation(self, country_id, vacation_description, start_date, end_date,  price, image, vacation_id):
        old_image_name = self.__get_old_image_name(vacation_id)
        image_name = ImageHandler.update_image(old_image_name, image)
        sql = ("UPDATE vacations SET country_id=%s, vacation_description=%s,start_date=%s, end_date=%s, price=%s, vacation_photo_filename=%s WHERE vacation_id=%s")
        data = (country_id, vacation_description, start_date,end_date,  price, image_name, vacation_id)
        return self.dal.update(sql, data)

    def delete_vacation(self, vacation_id):
        sql = ("DELETE FROM vacations WHERE vacation_id = %s")
        data = (vacation_id, )
        return self.dal.delete(sql, data)
    
    def __get_old_image_name(self, id):
        sql = "SELECT vacation_photo_filename FROM vacations WHERE vacation_id=%s"
        result = self.dal.get_scalar(sql, (id,))
        return result["vacation_photo_filename"]
    
    def get_country_name(self,id):
        sql = "SELECT country_name FROM countries WHERE country_id =%s"
        result = self.dal.get_scalar(sql,(id,))
        return result["country_name"]
    
    def get_all_countries(self):
        sql = "SELECT * FROM countries"
        return self.dal.get_table(sql)
    

    # like
    
    # add like to DB:
    def add_like(self, user_id, vacation_id):
        sql = ("INSERT INTO likes VALUES (%s, %s)")
        self.dal.insert(sql, (user_id, vacation_id))

    # delete like from DB:
    def delete_like(self, user_id, vacation_id):
        sql = ("DELETE FROM likes WHERE user_id = %s AND vacation_id = %s")
        self.dal.delete(sql, (user_id, vacation_id))
    
    # getting the likes list from DB:
    def get_likes_count(self, vacation_id):
        sql = ("SELECT COUNT(vacation_id) AS likes_count FROM likes WHERE vacation_id = %s")
        result = self.dal.get_scalar(sql, (vacation_id, ))
        return result["likes_count"]
    
    # getting the likes user:
    def get_likes_by_user(self, user_id):
        sql = ("SELECT vacation_id FROM likes WHERE user_id = %s")
        result = self.dal.get_table(sql,(user_id, ))
        return result


    def close(self):
        self.dal.close()

    def close(self):
        self.logic.close()    
