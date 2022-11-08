from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Install below modules
# pip install flask_restful
# pip install flask_cors

from resources.archive_tables.archive_billing_tables import ArchiveTables  # ArchiveTables --> class

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(ArchiveTables, '/archive_tables')   # Mapped class with end_point

# TODO::READ host,port from properties
app.run(host='ANIL', port=5003, debug=True, use_reloader=True)