from utils.dal import DAL


class UsersLogic:

    def __init__(self):
        self.dal = DAL()

    def insert_user(self, First_name, Last_name, Email, password, role_id):
        sql = ("INSERT INTO users(First_name, Last_name, Email, password, role_id) VALUES(%s, %s, %s, %s, %s)")
        data = (First_name, Last_name, Email, password, role_id)
        prams = self.dal.insert(sql, data)
        return prams

    def user_by_email_and_password(self, email, password):
        sql = ("SELECT user_id FROM users WHERE Email = %s AND password= %s")
        data = (email, password)
        prams = self.dal.get_scalar(sql, data)
        return prams

    def check_email_exists(self, email):
        sql = ("SELECT * FROM users WHERE Email =%s")
        data = (email, )
        prams = self.dal.get_scalar(sql, data)
        return False if prams == None else True

    def close(self):
        self.dal.close()
