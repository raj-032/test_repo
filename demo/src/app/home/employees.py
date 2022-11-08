from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import psycopg2
from common.config import create_conn
import pandas as pd



class GETEMPLOYEE(Resource):
    def get(self):
        query = "SELECT * FROM employee"
        conn = create_conn()
        df = pd.read_sql(query, conn)
        print(df)
        js = df.to_json(orient='records')
        conn.close()
        return js


class UPDATEEMPLOYEE(Resource):
    def post(self):
        req_data = request.get_json()
        print(req_data)
        conn = create_conn()
        emp_id = req_data['emp_id']
        emp_salary = req_data['emp_salary']
        update_script = f'UPDATE employee SET emp_salary = {emp_salary} where emp_id = {emp_id}'
        cur = conn.cursor()
        cur.execute(update_script)
        conn.commit()
        conn.close()
        return "update sucess"


class INSERTEMPLOYEE(Resource):
    def post(self):
        req_data = request.get_json()
        print(req_data)
        conn = create_conn()
        update_script = f'INSERT INTO employee(emp_id, emp_name, emp_salary) VALUES(%s,%s,%s)'
        # insert_values = [(6,'mahesh',16000),(7,'anil',17000),(8,'sudha',18000),(9,'raju',19000)]
        insert_values = (req_data['emp_id'], req_data['emp_name'], req_data['emp_salary'])

        cur = conn.cursor()
        cur.execute(update_script, insert_values)
        conn.commit()
        conn.close()
        return "update sucess"


class DELETEEMPLOYEE(Resource):
    def delete(self):
        req_data = request.get_json()
        print(req_data)
        conn = create_conn()
        emp_id = req_data['emp_id']
        delete_script = f'DELETE FROM employee where emp_id = {emp_id}'

        cur = conn.cursor()
        cur.execute(delete_script)
        conn.commit()
        conn.close()
        return "delete sucess"

#
# api.add_resource(GETEMPLOYEE, '/')
# api.add_resource(UPDATEEMPLOYEE, '/update_query')
# api.add_resource(INSERTEMPLOYEE, '/insert_query')
# api.add_resource(DELETEEMPLOYEE, '/delete_query')
#
# if __name__ == '__main__':
#     app.run(port=5001, debug=True)
