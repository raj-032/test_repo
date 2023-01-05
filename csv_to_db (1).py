import pandas as pd
import numpy as np
import psycopg2

csv = "NE--2022.csv"

df = pd.read_csv(csv, low_memory=False) # .fillna('None')

# df = df.replace(r'^\s*$', np.nan, regex=True)

# df = df.replace({np.nan: None})
df = df.where(pd.notnull(df), None)

# print(df)

rows = list(df.itertuples(index=False, name=None))

print(rows[0], f"\nData type of df_tuple is {type(rows)}", \
    f"\nData type of first iterable is {type(rows[0])}" \
        f"\nlenth of First iterable {len(rows[18])}")


# # Get the list of all column names from headers
# column_headers = list(df.columns.values)
# print("\nThe Column Header :", column_headers)

df[['CREATION_DATE']] = df[['CREATION_DATE']].apply(pd.to_datetime)


def postgres_connection_func():
    POSTGRES_DATABASE_HOST_ADDRESS = 'localhost'
    POSTGRES_DATABASE_NAME = 'temporory_DB'
    POSTGRES_USERNAME = 'postgres'
    POSTGRES_PASSWORD = 'Jjsb123'
    POSTGRES_CONNECTION_PORT = 5432

    db_info = "host='%s' dbname='%s' user='%s' password='%s' port='%s'" % (POSTGRES_DATABASE_HOST_ADDRESS, POSTGRES_DATABASE_NAME, POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_CONNECTION_PORT)
    postgres_connection_obj = psycopg2.connect(db_info)
    
    return postgres_connection_obj

print(f'Establishing postgres connection')
postgres_connection = postgres_connection_func()
postgres_connection.autocommit = True
cursor = postgres_connection.cursor()
print(f'Establishing postgres connection successfully.........')


row_count = 0
for row in rows:
    # sql2 = '''
    # COPY xxozf_dealsui_cpt_stg(OFFER_NUMBER,	DEAL_DESC,	DEAL_TYPE_CODE,	DEAL_TYPE_NAME,	DEAL_STATUS,
    #     DEAL_START_DATE,	DEAL_END_DATE,	vendor_id,	VENDOR_NUMBER,	VENDOR_NAME,	MERCHANDISER_NUMBER,
    #     CPT_MERCHANDISER_NUMBER,	PERFORMANCE_ID,	PERFORMANCE_NAME,	AD_WEEK,	AD_DATE,	DIVISION_CODE,
    #     DIVISION_NAME,	DEAL_FEE_ID,	DEAL_FEE_TYPE,	DEAL_LUMPSUM_AMOUNT,	FEES_DIVISION_CODE,
    #     FEES_DESCRIPTION,	DEAL_PRODUCT_ID,	Facility_code,	ITEM_TYPE,	ITEM_CODE,	ITEM_DESC,	ITEM_SSIC,
    #     LEGACY_ITEM_CODE,	TOTAL_ALLOWANCE_AMOUNT,	ITEM_CASE_PACK,	ITEM_CASE_SIZE,	ITEM_CASE_SIZE_UNIT,	UPC_COMM,
    #     UPC_MFG,	UPC_CASE,	UPC_ITEM,	GL_CODE,	GL_CODE_DESC,	buyer_vendor_number,	LINK_CODE,
    #     CATEGORY_CODE,	DEAL_CREATION_DATE,	DEAL_CREATED_BY,	DEAL_LAST_UPDATED_BY,	DEAL_LAST_UPDATE_DATE,
    #     DEAL_LAST_UPDATE_LOGIN,	CREATION_DATE,	CREATED_BY,	LAST_UPDATED_BY,	LAST_UPDATE_DATE,	LAST_UPDATE_LOGIN,
    #     Ad_Group_No,	Ad_Group_Description,	DEPARTMENT,	SUPER_CATEGORY,	CATEGORY,	SUB_CATEGORY,	UOM,
    #     CROSS_CODE,	PRIVATE_LABEL,	MERCHANDISER_NAME,	SUB_VENDOR_NUMBER,	CPT_STATUS,	R7_STATUS,
    #     Record_Conversion_Interface,	Original_Record_ID,	Merchandiser_Email,	National_Regional_Flag,
    #     Ad_Week_Start_Date,	Ad_Theme,	Shipper_Flag,	Seasonal_Flag,	List_Cost,	Cost_Percentage,
    #     Retail,	UNIT_COST,	Batch_ID,	AD_COST,	AD_UNIT_COST,	AD_RETAIL,	REQUEST_ID,	ALLOWANCE_CODE,
    #     ALLOWANCE_NAME,	RUN_ID,	EXTERNAL_KEY,	VENDOR_NOTES,	ACTION_TYPE) 
    # FROM '/Users/ajinkkya24/Development/playground/python/My_Tasks/Nitish Kale/tranform_csv_to_db/csv_to_db.py'
    # DELIMITER ','
    # CSV HEADER;'''
    
    # cursor.execute(sql2)
    
    sql_insert = """
    INSERT INTO xxozf_dealsui_cpt_stg(OFFER_NUMBER,	DEAL_DESC,	DEAL_TYPE_CODE,	DEAL_TYPE_NAME,	DEAL_STATUS,
        DEAL_START_DATE,	DEAL_END_DATE,	vendor_id,	VENDOR_NUMBER,	VENDOR_NAME,	MERCHANDISER_NUMBER,
        CPT_MERCHANDISER_NUMBER,	PERFORMANCE_ID,	PERFORMANCE_NAME,	AD_WEEK,	AD_DATE,	DIVISION_CODE,
        DIVISION_NAME,	DEAL_FEE_ID,	DEAL_FEE_TYPE,	DEAL_LUMPSUM_AMOUNT,	FEES_DIVISION_CODE,
        FEES_DESCRIPTION,	DEAL_PRODUCT_ID,	Facility_code,	ITEM_TYPE,	ITEM_CODE,	ITEM_DESC,	ITEM_SSIC,
        LEGACY_ITEM_CODE,	TOTAL_ALLOWANCE_AMOUNT,	ITEM_CASE_PACK,	ITEM_CASE_SIZE,	ITEM_CASE_SIZE_UNIT,	UPC_COMM,
        UPC_MFG,	UPC_CASE,	UPC_ITEM,	GL_CODE,	GL_CODE_DESC,	buyer_vendor_number,	LINK_CODE,
        CATEGORY_CODE,	DEAL_CREATION_DATE,	DEAL_CREATED_BY,	DEAL_LAST_UPDATED_BY,	DEAL_LAST_UPDATE_DATE,
        DEAL_LAST_UPDATE_LOGIN,	CREATION_DATE,	CREATED_BY,	LAST_UPDATED_BY,	LAST_UPDATE_DATE,	LAST_UPDATE_LOGIN,
        Ad_Group_No,	Ad_Group_Description,	DEPARTMENT,	SUPER_CATEGORY,	CATEGORY,	SUB_CATEGORY,	UOM,
        CROSS_CODE,	PRIVATE_LABEL,	MERCHANDISER_NAME,	SUB_VENDOR_NUMBER,	CPT_STATUS,	R7_STATUS,
        Record_Conversion_Interface,	Original_Record_ID,	Merchandiser_Email,	National_Regional_Flag,
        Ad_Week_Start_Date,	Ad_Theme,	Shipper_Flag,	Seasonal_Flag,	List_Cost,	Cost_Percentage,
        Retail,	UNIT_COST,	Batch_ID,	AD_COST,	AD_UNIT_COST,	AD_RETAIL,	REQUEST_ID,	ALLOWANCE_CODE,
        ALLOWANCE_NAME,	RUN_ID,	EXTERNAL_KEY,	VENDOR_NOTES,	ACTION_TYPE) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" 
    
    record_to_insert = (row[0],	row[1],	row[2],	row[3],	row[4],	row[5],	row[6],	row[7],	row[8],	row[9],	row[10],	
                        row[11],	row[12],	row[13],	row[14],	row[15],	row[16],	row[17],	row[18],	
                        row[19],	row[20],	row[21],	row[22],	row[23],	row[24],	row[25],	row[26],	
                        row[27],	row[28],	row[29],	row[30],	row[31],	row[32],	row[33],	row[34],	
                        row[35],	row[36],	row[37],	row[38],	row[39],	row[40],	row[41],	row[42],	
                        row[43],	row[44],	row[45],	row[46],	row[47],	row[48],	row[49],	row[50],	
                        row[51],	row[52],	row[53],	row[54],	row[55],	row[56],	row[57],	row[58],	
                        row[59],	row[60],	row[61],	row[62],	row[63],	row[64],	row[65],	row[66],	
                        row[67],	row[68],	row[69],	row[70],	row[71],	row[72],	row[73],	row[74],	
                        row[75],	row[76],	row[77],	row[78],	row[79],	row[80],	row[81],	row[82],	
                        row[83],	row[84],	row[85],	row[86],	row[87],	row[88])
    
    cursor.execute(sql_insert, record_to_insert)
    row_count = row_count + 1