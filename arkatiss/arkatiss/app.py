from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.employee.employees import GetEmployee

app = Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(GetEmployee, '/employee/get_employee_detail')
# app.run(host='DESKTOP-P5DJTSG', port=5000, debug=False, use_reloader=False)
app.run(host='DESKTOP-P5DJTSG', port=5000, debug=True, use_reloader=True)