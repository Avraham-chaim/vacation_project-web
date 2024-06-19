from utils.dal import DAL


class AuthLogic:

    def __init__(self):
        self.dal = DAL()

    def is_email_taken(self, email):
        sql = "SELECT EXISTS(SELECT * FROM users WHERE email = %s) AS is_taken"
        result = self.dal.get_scalar(sql, (email,))
        return result["is_taken"] == 1    
    
    def add_user(self, user):    
        sql = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s, %s, %s)"
        self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password, user.role_id))

    def get_user(self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        user = self.dal.get_scalar(sql, (email, password))
        return user    

    def close(self):
        self.dal.close()