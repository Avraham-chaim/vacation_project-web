from hashlib import sha512
from utils.app_config import AppConfig


class Cyber:

    @staticmethod
    def hash(plain_text):
        encoded_text = plain_text.encode("UTF-8") + AppConfig.passwords_salt.encode("UTF-8")
        hashed_text = sha512(encoded_text).hexdigest()
        hashed_text = hashed_text[1:15]
        return hashed_text
