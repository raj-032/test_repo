import pandas as pd
import logging
import numpy as np
import inspect
from pathlib import Path
import traceback
import time
from datetime import datetime

import pdb

def archive_billing_tbls(data):
    try:

        # https://stackoverflow.com/questions/30732915/convert-all-keys-of-a-dictionary-into-lowercase

        # data = utils.upper_keys(data)  # TODO::Check how to convert keys from lower to upper case in {}/[{},{}]

        # archive_tbls = utils.upper_keys(eval(properties['archive_tbls']))
        # archive_tbls = eval(properties['archive_tbls'])
        # archive_tbl_past_days = int(properties['archive_tbl_past_days'])

        # TODO::see how to read archive_tbls, archive_tbl_past_days from properties file(app.proerties)

        archive_tbls = [{"type": "ARCHIVE", "src_table": "apps.oms_wms_ord_delivery_in_stg",
                         "target_table": "apps.oms_wms_ord_delv_in_stg_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "DELETE", "src_table": "apps.oms_wms_ord_delivery_iw_stg",
                         "target_table": "apps.oms_wms_ord_delv_iw_stg_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "ARCHIVE", "src_table": "apps.oms_wms_ord_delivery_bc_stg",
                         "target_table": "apps.oms_wms_ord_delv_bc_stg_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "ARCHIVE", "src_table": "apps.oms_wms_ord_delivery_oc_stg",
                         "target_table": "apps.oms_wms_ord_delv_oc_stg_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "ARCHIVE", "src_table": "apps.oms_wms_ord_delivery_ld_stg",
                         "target_table": "apps.oms_wms_ord_delv_ld_stg_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "ARCHIVE", "src_table": "apps.oms_wms_release_status",
                         "target_table": "apps.oms_wms_release_status_arch", "where_clause": "PROCESS_STATUS = 'P'",
                         "backup_days": "21", "backup_column": "creation_date"},
                        {"type": "ARCHIVE", "src_table": "apps.oms_invoice_header",
                         "target_table": "apps.oms_invoice_header_arch", "where_clause": "", "backup_days": "21",
                         "backup_column": "order_close_date", "SKIP_WHERE": "Y",
                         "child_table": {"apps.oms_invoice_lines": "apps.oms_invoice_lines_arch"},
                         "relation_col": {"INVOICE_ID": "INVOICE_ID"}},
                        {"type": "ARCHIVE", "src_table": "apps.oms_delivery_headers_stg",
                         "target_table": "apps.oms_delivery_headers_stg_arch", "backup_days": "21",
                         "backup_column": "order_close_date", "SKIP_WHERE": "Y",
                         "child_table": {"apps.oms_delivery_lines_stg": "apps.oms_delivery_lines_stg_arch"},
                         "relation_col": {"DELIVERY_HEADER_ID": "DELIVERY_HEADER_ID"}}]

        archive_tbl_past_days = 21
        pdb.set_trace()
        # prop_src_tbls = [prop_archive_tbl['SRC_TABLE'] for prop_archive_tbl in archive_tbls]
        # TODO:: use above commented line
        prop_src_tbls = [prop_archive_tbl['src_table'] for prop_archive_tbl in archive_tbls]

        if data not in [[], {}]:
            process_archive_tbls = data
        else:
            process_archive_tbls = archive_tbls

        non_archived = []
        archived = []
        # TODO:: See whether all conditions working fine
        for archive_tbl in process_archive_tbls:
            if 'SRC_TABLE' not in archive_tbl or archive_tbl['SRC_TABLE'] == '':
                archive_tbl['msg'] = 'Please provide source table'
                non_archived.append(archive_tbl)
                continue
            if data not in [[], {}] and archive_tbl['SRC_TABLE'] not in prop_src_tbls:
                archive_tbl['msg'] = f'{archive_tbl["SRC_TABLE"]} is not allowed to archive/delete'
                non_archived.append(archive_tbl)
                continue

            for archive_tbl in process_archive_tbls:
                if 'SRC_TABLE' not in archive_tbl or archive_tbl['SRC_TABLE'] == '':
                    archive_tbl['msg'] = 'Please provide source table'
                    non_archived.append(archive_tbl)
                    continue
            if data not in [[], {}] and archive_tbl['SRC_TABLE'] not in prop_src_tbls:
                archive_tbl['msg'] = f'{archive_tbl["SRC_TABLE"]} is not allowed to archive/delete'
                non_archived.append(archive_tbl)
                continue

            if archive_tbl['TYPE'] != [prop_archive_tbl['TYPE'] for prop_archive_tbl in archive_tbls if
                                       prop_archive_tbl['SRC_TABLE'] == archive_tbl['SRC_TABLE']][0]:
                archive_tbl['msg'] = f"{archive_tbl['TYPE']} type is not allowed in {archive_tbl['SRC_TABLE']}"
                non_archived.append(archive_tbl)
                continue

            # backup_column should always be defined. If not there then give error backup_column is mandatory
            if 'BACKUP_COLUMN' not in archive_tbl or archive_tbl['BACKUP_COLUMN'] == '':
                archive_tbl['msg'] = 'backup_column is mandatory'
                non_archived.append(archive_tbl)
                continue

            # if BACKUP_DAYS not given in user payload or archive_tbls property in properties file
            # then take archive_tbl_past_days as BACKUP_DAYS

            if 'BACKUP_DAYS' not in archive_tbl or archive_tbl['BACKUP_DAYS'] == '':
                archive_tbl['BACKUP_DAYS'] = archive_tbl_past_days

            if int(archive_tbl['BACKUP_DAYS']) < archive_tbl_past_days:
                archive_tbl['msg'] = f'backup_days must be greater than or equals to {archive_tbl_past_days}'
                non_archived.append(archive_tbl)
                continue

            src_table = archive_tbl['SRC_TABLE']
            backup_days = archive_tbl['BACKUP_DAYS']
            backup_column = archive_tbl['BACKUP_COLUMN']
            type = archive_tbl['TYPE'].lower()

            if type not in ['archive', 'delete']:
                archive_tbl['msg'] = f'type must be either archive/delete'
                non_archived.append(archive_tbl)
                continue

            # WHERE clause Shouldn't be empty.

            if 'WHERE_CLAUSE' not in archive_tbl or archive_tbl['WHERE_CLAUSE'] == '':
                if 'SKIP_WHERE' in archive_tbl and archive_tbl['SKIP_WHERE'] == 'Y':
                    where_clause = f"{backup_column} < sysdate - {backup_days}"  # SKIP_WHERE = 'Y'
                else:
                    archive_tbl['msg'] = 'Please provide where clause'
                    non_archived.append(archive_tbl)
                    continue

            else:
                where_clause = f"{archive_tbl['WHERE_CLAUSE']} and {backup_column} < sysdate - {backup_days}"


            # Started by Mahesh on 092222

            parent_link_col = ''
            child_col = ''
            child_src_table = ''
            child_target_table = ''

            if 'CHILD_TABLE' in archive_tbl and archive_tbl['CHILD_TABLE'] != {}:
                # child_src_table, child_target_table
                child_src_table = list(archive_tbl['CHILD_TABLE'].keys())[0]
                # Checking archival table is given or not
                if archive_tbl['CHILD_TABLE'][child_src_table] == '':
                    archive_tbl['msg'] = f'Please provide archive table for child - {child_src_table}'
                    non_archived.append(archive_tbl)
                    pass

                child_target_table = archive_tbl['CHILD_TABLE'][child_src_table]

                if 'RELATION_COL' in archive_tbl and archive_tbl['RELATION_COL'] != {}:
                    parent_link_col = list(archive_tbl['RELATION_COL'].keys())[0]
                    child_col = archive_tbl['RELATION_COL'][parent_link_col]
                else:
                    archive_tbl['msg'] = f'Please provide RELATION_COL for child - {child_src_table}'
                    non_archived.append(archive_tbl)
                    pass
        if non_archived!=[]:
            return {'msg':{'non_archived':non_archived}, 'res_code':1}
        return {'msg': 'All tables archived', 'res_code': 1}
    except Exception as e:
        return {'msg':str(e),'res_code':0}