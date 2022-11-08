from flask_restful import Api, Resource, request
from common_ui import config

from models.employee import employees

class GetEmployee(Resource):
    def post(self):
        try:
            data = request.get_json()
            conn = config.conn()
            cur = conn.cursor()

            emp_id = data['emp_id']



            cur.execute("select * from employee where emp_id = '%s'"%(emp_id))

            row = cur.fetchall()

            data = []
            if row is not None:
                for result in row:
                    data.append({"emp_id": result[0], "emp_name": result[1],"emp_sal": type})

                return{"res_status": True, "status": 200, "data": data}
            return{"res_status": False, "msg": "No employee found with that emp_id"}

        except Exception as e:

            if conn:
               conn.close()
            return {"res_status": False, "msg": "No data"}
        finally:
            cur.close()
            conn.close()