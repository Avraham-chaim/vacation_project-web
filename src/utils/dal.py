from mysql.connector import connect
from .app_config import AppConfig


class DAL:

    def __init__(self):
        self.connection = connect(
            host=AppConfig.mysql_host,
            user=AppConfig.mysql_user,
            password=AppConfig.mysql_password,
            database=AppConfig.mysql_database)

    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table

    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar

    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save to database now.
            last_row_id = cursor.lastrowid
            return last_row_id

    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save to database now.
            row_count = cursor.rowcount
            return row_count

    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit()  # Save to database now.
            row_count = cursor.rowcount
            return row_count

    # Close connection:
    def close(self):
        self.connection.close()
