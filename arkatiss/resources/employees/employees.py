import pdb

import psycopg2
from flask_restful import Resource,request

from common import config, utils


class RetrieveEmployees(Resource):
    def post(self):
        try:
            data = request.get_json()
            conn = None
            cur = None

            conn = config.conn()
            cur = conn.cursor()
            if 'emp_ids' not in data or data['emp_ids'] =='':
                return {'res_status': False, 'msg': 'Please provide employee ids'}
            emp_ids = tuple(data['emp_ids'])
            cur.execute(f"select * from employees where emp_id in {emp_ids}")
            # TODO:: See what is commit
            emps = cur.fetchall()
            emps_data = []
            if emps:

                # for emp in emps:
                #     # Way -1 - Waste
                #     emp_id = emp[0]
                #     emp_name = emp[1]
                #     emp_sal = emp[2]
                #     emps_data.append({'emp_id': emp_id, 'emp_name': emp_name, 'emp_id': emp_sal})
                #
                #     # Way -2 - Waste
                #     emps_data.append({'emp_id': emp[0], 'emp_name': emp[1], 'emp_id': emp[2]})

                # Using list comprehension - best way
                emps_data = [{'emp_id':emp[0], 'emp_name':emp[1], 'emp_sal':emp[2]} for emp in emps]

                return {'res_status': True, 'employees': emps_data}

            return {'res_status': False, 'msg': f'There are no employees with the employee ids: {emp_ids}'}
        except Exception as e:
            print(f'employees-RetrieveEmployees: Error: {e}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


class AddEmployee(Resource):
    def post(self):
        try:
            data = request.get_json()
            conn = None
            cur = None

            conn = config.conn()
            cur = conn.cursor()
            if 'emp_name' not in data or data['emp_name'] =='':
                return {'res_status': False, 'msg': 'Please provide employee name'}

            emp_name = data['emp_name']
            emp_sal = data['emp_sal'] if 'emp_sal' in data else 0.0

            cur.execute(f"insert into employees(emp_name,emp_sal) values('{emp_name}', {emp_sal})")
            # TODO:: See what is commit
            conn.commit()
            return {'res_status': False, 'msg': f'Added employee {emp_name}'}
        except Exception as e:
            print(f'employees-AddEmployee: Error: {e}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


class UpdateEmployee(Resource):
    def post(self):
        try:
            data = request.get_json()
            conn = None
            cur = None

            conn = config.conn()
            cur = conn.cursor()
            if 'emp_id' not in data or data['emp_id'] =='':
                return {'res_status': False, 'msg': 'Please provide employee id'}

            if 'emp_name' not in data or data['emp_name'] =='':
                return {'res_status': False, 'msg': 'Please provide employee name'}
            if 'emp_sal' not in data or data['emp_sal'] =='':
                return {'res_status': False, 'msg': 'Please provide employee salary'}

            emp_name = data['emp_name']
            emp_sal = data['emp_sal']

            cur.execute(f"update employees set emp_name='{emp_name}', emp_sal = {emp_sal} where emp_id = {data['emp_id']}")
            # TODO:: See what is commit
            conn.commit()
            return {'res_status': False, 'msg': f'Updated employee {emp_name}'}
        except Exception as e:
            print(f'employees-UpdateEmployee: Error: {e}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()


class DeleteEmployees(Resource):
    def post(self):
        try:
            data = request.get_json()
            data = utils.upper_keys(data)

            conn = None
            cur = None

            conn = config.conn()
            cur = conn.cursor()

            if 'EMP_IDS' not in data or data['EMP_IDS'] in ('', []):
                return {'res_status': False, 'msg': 'Please provide employee ids'}
            emp_ids = data['EMP_IDS']

            # emp_whr_clause = utils.generate_sql_in_cond_string('emp_id', emp_ids, col_type='int')
            emp_whr_clause = utils.generate_sql_in_cond_string('emp_id', emp_ids)

            print(f'emp_whr_clause:{emp_whr_clause}')
            cur.execute(f"delete from employees where {emp_whr_clause}")
            # TODO:: See what is commit
            conn.commit()
            return {'res_status': True, 'msg': 'Deleted employees successfully'}

        except Exception as e:
            print(f'employees-DeleteEmployees: Error: {e}')
            return {'res_status': False, 'msg': str(e)}
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()