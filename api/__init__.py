from flask import Flask
from api.views import user, incident

app = Flask(__name__)
app.register_blueprint(incident)
app.register_blueprint(user)


