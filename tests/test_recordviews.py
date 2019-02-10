import unittest
import json
from api import app


class Test_incident_views(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.incidents = {
                "incident_type": "Articlkhje",
                "title": "Incident at Kamwokya",
                "description": "Today is the day",
                "location": "Kamwokya",
                "status": "unresolved",
                "images": "image",
                "videos": "video",
                "comments": "hello",
                "created_by": "phiona"
            }

    def test_create_incident(self):
        response = self.client.post('/api/v1/incidents',
                                    content_type='application/json',
                                    data=json.dumps(self.incidents))
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Successfully created", msg['message'])  
 
    def test_fetch_all_incidents(self):
        # Tests that the end point fetches all incidents
        response = self.client.get('/api/v1/incidents',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_incident(self):
        # Tests that the end point returns a single incident
        incident_details = {
                    "title": "Corruption at its tipsefdthryt",
                    "description": "corruption in court in broad day light",
                    "status": "accepted",
                    "location": "nansana",
                    "incident_type": "redflag",
                    "images": "fffff,fghjkj",
                    "videos": "ffcccdsffcvvbfff",
                    "created_by": "mutebiedfvfdhrtjuk",
                    "comments": "cuilrf,mrfre"
            }
        self.client.post('api/v1/incidents',
                         json=incident_details)
        response = self.client.get('/api/v1/incidents/1',
                                   content_type='application/json')
        msg = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_edit_incident(self):
        # Tests that the end point enables user edit their already 
        # created incident before status is changed by admin
        incident_details = {
            "comments": "mutebiedfvfdhrtjuk",
            "created_by": "corruption in court in broad day light",
            "created_on": "Corruption at its tips  in kanjo",
            "description": "fffff,fghjkj",
            "images": "love",
            "location": "kakts",
            "incident_id": 1,
            "incident_type": "accepted",
            "status": "intervention",
            "title": "cuilrf,mrfre",
            "videos": "ffcccdsffcvvbfff"
            }
        response = self.client.post('api/v1/incidents',
                                    content_type='application/json',
                                    json=incident_details)
        new_details = {
                    "title": "Corruption at its tipsefdthryt",
                    "description": "corruption in court in broad day light",
                    "status": "accepted",
                    "location": "mukono",
                    "incident_type": "intervention",
                    "images": "fffff,fghjkj",
                    "videos": "ffcccdsffcvvbfff",
                    "created_by": "mutebiedfvfdhrtjuk",
                    "comments": "cuilrf,mrfre"
        }
        response = self.client.put('api/v1/incidents/1',
                                   json=new_details)
        msg = json.loads(response.data)
        self.assertIn("successfully edited", msg['message'])
        self.assertEqual(response.status_code, 201)

    def test_delete_incident(self):
        # Tests that the end point enables user edit their already created
        # record when rejected by admin
        incident_details = {
            "comments": "mutebiedfvfdhrtjuk",
            "created_by": "corruption in court in broad day light",
            "created_on": "Corruption at its tips  in kanjo",
            "description": "fffff,fghjkj",
            "images": "love",
            "location": "kakts",
            "incident_id": 1,
            "record_type": "accepted",
            "status": "intervention",
            "title": "cuilrf,mrfre",
            "videos": "ffcccdsffcvvbfff"
            }
        response = self.client.post('api/v1/incidents',
                                    content_type='application/json',
                                    json=incident_details)
        new_details = {
        }
        response = self.client.delete('api/v1/incidents/1',
                                      json=new_details)
        msg = json.loads(response.data)
        self.assertIn("successfully deleted", msg['message'])
        self.assertEqual(response.status_code, 201)
