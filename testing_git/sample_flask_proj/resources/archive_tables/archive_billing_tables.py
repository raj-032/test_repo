import pdb

from flask import Flask
from flask_restful import Resource,request

from models.archive_tables.archive_billing_tables import archive_billing_tbls


class ArchiveTables(Resource):
    # see get/post/put/delete methods of restful but use only post for now.
    # If required we may use later
    def post(self):
        try:
            data = request.get_json()

            # Call models.archive_tables.archive_billing_tables.archive_billing_tbls()

            res = archive_billing_tbls(data)
            if res['res_code']== 1:
                return {'code': True, 'msg':res['msg'], 'status_code':200}
            if res['res_code']==0:
                return {'code':False,'msg':res['msg'],'status_code':200}  # TODO::see codes for api
        except Exception as e:
            return {'code': False,'msg':str(e), 'status_code':200}