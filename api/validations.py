import re
from .models import Incident, User

name_regex = r"[a-zA-Z]"
password_regex = r"(?=.*[0-9])"
username_regex = r"[a-zA-Z0-9_]"
phone_regex = r"\d{3}-\d{3}-\d{4}"


class Validate:
    """This class contains validators for the different entries"""
    def validate_user(self, data):
        # Validates user fields
        user_details = ['username', 'othernames', 'firstname', 'lastname', 'email', 'password'] 
        username = data['username']
        user_fields = ['othernames', 'firstname', 'lastname']
        key_fields = ['email', 'password', 'phonenumber']
        print(data)
        for key in user_details:
            print(key)
            print(data[key], "this one")
            if not data[key] or data[key].isspace():
                return 'fill in all fields.' 
            if not re.match(username_regex, data['username']):
                return 'Enter a valid username'

        for name in user_fields:
            if not re.match(name_regex, data[name]):
                return 'Enter correct ' + name + ' format'
        
        for user_detail in user_details:
            if len(data[user_detail]) > 30:
                return user_detail + ' too long'

        for key in key_fields:     
            if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", data['email']):
                return 'Enter a valid email address.'
            if not re.match(phone_regex, data['phonenumber']):
                return 'Enter phone format 123-456-7890'
            if len(data['password']) < 8:
                return 'Password must be atleast 8 characters'
        return "is_valid"
            
    def validate_login(self, data):
        if len(data.keys()) < 2 or len(data.keys()) > 2:
            return " email and password  required to login"
        if data['email'] == "":
            return "Input email"
        if data['password'] == "":
            return "Input password"  
        return "credentials_valid"
    