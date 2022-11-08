from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# TODO:: See what is the use of flask,flask_cors,flask_restful modules

from resources.employees.employees import RetrieveEmployees, AddEmployee, UpdateEmployee, DeleteEmployees

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(RetrieveEmployees, '/arkatiss/employees/retrieve')
api.add_resource(AddEmployee, '/arkatiss/employee/add')  # TODO: Add employee
api.add_resource(UpdateEmployee, '/arkatiss/employee/update')  # TODO: Update employee
api.add_resource(DeleteEmployees, '/arkatiss/employees/delete')  # TODO:: Delete multiple employees by emp_id
if __name__ == '__main__':
    # TODO:: Keep hostname, port in properties file(<project_name>.properties) and read from it
    hostname = 'DESKTOP-P5DJTSG'               # get hostname by executing "hostname" cmd on command prompt
    port = 5000                                 # default port for flask
    app.run(host=hostname, port=port, debug=True, use_reloader=True)