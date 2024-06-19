from validate_email_address import validate_email


class CredentialsModel:

    def __init__(self, email, password):
        self.email = email
        self.password = password


    # check the data from the user:
    def Validate(self):
        if not self.email: return "Missing Email"
        if not self.password: return "Missing Password"
        if len(self.email) < 5 or len(self.email) > 100: return "Email must be 5 - 100 chars"
        if len(self.password) < 4 or len(self.password) > 100: return "Password must be 4 - 100 chars"
        if not validate_email(self.email): return "Email not valid"
        return None 