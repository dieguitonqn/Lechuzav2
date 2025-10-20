

class UserCreateDTO:
    def __init__(self, email:str, password:str, is_active:bool=False, is_epen_user:bool=False, is_admin:bool=False):
        self.email = email
        self.password = password
        self.is_active = is_active
        self.is_epen_user = is_epen_user
        self.is_admin = is_admin

