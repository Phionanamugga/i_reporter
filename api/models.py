# from datetime.datetime import now

class Incident:
    # this class defines the record created by a user
    def __init__(self, incident_id, createdOn, created_by, incident_type, title,
                 description, location, status, images, videos, comments):
        self.incident_id = incident_id
        self.createdOn = createdOn
        self.created_by = created_by
        self.incident_type = incident_type
        self.title = title
        self.description = description
        self.location = location
        self.status = status
        self.images = images
        self.videos = videos
        self.comments = comments

    def get_incident(self):
        return {
            "incident_id": self.incident_id,
            "created_on": self.createdOn,
            "created_by": self.created_by,
            "incident_type": self.incident_type,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comments": self.comments
        }


class User:
    # this class defines the details of a user
    def __init__(self, user_id, firstname, lastname, othernames, email,
                 phonenumber, username, password):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phonenumber = phonenumber
        self.username = username
        self.password = password
        self. registered_on = None


# 