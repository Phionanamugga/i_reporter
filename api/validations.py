# import re
# from .models import Incident, User
# from datetime import datetime
# from flask import jsonify, request, abort

# name_regex = r"[a-zA-Z]"
# password_regex = r"(?=.*[0-9])"
# username_regex = r"[a-zA-Z0-9_]"
# phone_regex = r"\d{3}-\d{3}-\d{4}"
# incidents = []

# users = [
#     User(1, 'aldo', 'Okware', 'Padde', 'aldo@gmail.com', '0779862290','aldo', 'test12345'),
# ]

# user_id_mapping = {u.user_id: u for u in users}
# user_email_mapping = {u.email: u for u in users}


# class Validate:
#     """This class contains validators for the different entries"""

#     def validate_product(self, data):
#         # Validates the product fields
#         product_fields = ['product_name', 'product_quantity', 'price']
#         try:
#             for product_field in product_fields:
#                 if data[product_field] == "":
#                     return product_field + " cannot be blank"

#             if not re.match(r"^[a-zA-Z0-9 _]*$", data['product_name']):
#                 return "productname should contain alphanumerics only"

#             if not re.match(r"^[0-9_]*$", data['price']):
#                 return "price should contain integers only"

#             if not re.match(r"^[0-9_]*$", data['product_quantity']):
#                 return "quantity should contain integers only"
#             else:
#                 return "Valid"
#         except KeyError:
#             return "Invalid Key Fields"

#     def validate_user(self, data):
#         # Validates user fields
#         # data = request.get_json()
#         user_id = len(users)+1
#         registered_on = datetime.now()
#         username = data['username']
#         text_fields = ['othernames', 'firstname', 'lastname', 'username']
#         user_fields = ['othernames', 'firstname', 'lastname']
#         key_fields = ['email', 'password']
#         for user in users:
#             print(user.email)
#             print(data['email'])
#             if user.email == data['email']:
#                 return jsonify({"message": "user already exists!"}), 400
#         for name in user_fields:
#             if not re.match(name_regex, data[name]):
#                 return jsonify({'message': 'Enter correct ' + name + ' format'}), 400
        
#         for key in key_fields:
#             if not data[key] or data[key].isspace():
#                 return jsonify({'message': key + ' field can not be empty.'}), 400   
#             if not username or username.isspace():
#                 return jsonify({'message': 'Username can not be empty.'}), 400 
#             if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", data['email']):
#                 return jsonify({'message': 'Enter a valid email address.'}), 400
#             if not re.match(username_regex, data['username']):
#                 return jsonify({'message': 'Enter a valid username'}), 400
#             if not re.match(phone_regex, data['phonenumber']):
#                 return jsonify({'message': 'Enter phone format 123-456-7890'}), 400
#             if len(data['password']) < 8:
#                 return jsonify({'message': 'Password must be atleast 8 characters'}), 400 
#             if len(data.keys()) == 0:
#                     return "No user added"
#             user = User(user_id, data['firstname'], data['lastname'],
#                         data['othernames'], data['email'], data['phonenumber'],
#                         data['username'], data['password'])
#             users.append(user)
#             return jsonify({"user_details": user.__dict__}), 201

#     def validate_login(self, data):
#         try:
#             if len(data.keys()) == 0 or len(data.keys()) > 2:
#                 return "Only email and password for login"
#             if 'email' not in data.keys():
#                 return "Email is missing"
#             if 'password' not in data.keys():
#                 return "Missing password"
#             if data['email'] == "" or data['password'] == "":
#                 return "Input email or password"
#             else:
#                 return "Credentials valid"
#         except KeyError:
#             return "Invalid fields"

#     def validate_id(self, item_id, item_list):
#         if item_id != 0 and item_id <= len(item_list):
#             return True
#         return False

#     def check_role(self, created_token):
#         try:
#             if created_token[0]['roles'] != 'Attendant':
#                 return True
#             return False
#         except IndexError:
#             return "Index out of range"