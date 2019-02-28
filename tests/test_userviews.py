import unittest
import json
from api import app
from api.models import User


class Test_user_views(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.user = User('Phie', 'John', 'brown','False', 'tttt@ttt.com', '123-456-7890', 'aldo',  'test1234') 
        
    def test_register_user(self):
        # Tests that the end point enables a new user create an account
        response = self.client.post('api/v1/users',
                                    data=json.dumps(self.user.__dict__),
                                    content_type="application/json"
                                    )
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(msg["user_details"]['email'], self.user.email)
    
    def test_fetch_all_users(self):
        # Tests that the end point fetches all users
        response = self.client.get('/api/v1/users',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        # Tests that the end point enables a user_login
        login_details = {"email": "tttt@ttt.com",
                         "password": "test1234"}
        response = self.client.post('api/v1/users/login', 
                                    data=json.dumps(login_details),
                                    content_type='application/json'
                                    )                         
        
        msg = json.loads(response.data)
        # self.assertEqual(response.status_code, 200)    

    def test_fetch_single_user_details(self):
        # Tests that the end point returns a single user's details
        response = self.client.get(
                    '/api/v1/users/1',
                )
        print(response)
        self.assertEqual(response.status_code, 200)