import pandas as pd
import psycopg2
#
# df = pd.DataFrame({'date': ['3/10/2000', '3/11/2000', '3/12/2000'],
#                    'value': [2, 3, 4]})
# df['date'] = pd.to_datetime(df['date'])   #Convert strings to datetime
# print(df)
#
# #handling missing values
#
# df['rolling_sum_backfilled'] = df['rolling_sum'].fillna(method='backfill')
# df.head()
#
#
#


import pandas as pd
# import psycopg2
# from datetime import datetime,timedelta
#
#
# df = pd.read_csv("C:\\Users\\raju\\OneDrive\\Documents\\Book1.csv",
#                 encoding = "ISO-8859-1", engine='python')
# print(df)
#
# conn = psycopg2.connect(hostname = 'localhost',
#     database = 'demo',
#     username = 'postgres',
#     pwd = 'admin',
#     port_id = 5432)
# cur = conn.cursor()
#
#
import pandas as pd
df = pd.read_csv("C:\\Users\\raju\\OneDrive\\Documents\\ordertable.csv",
                encoding = "ISO-8859-1", engine='python')
print(df)
# df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces
#
# from sqlalchemy import create_engine
# # engine = create_engine('postgresql://username:password@localhost:5432/dbname')
# engine = create_engine(''postgresql://postgres:password@localhost/demo')
#
#
# #
# # app.config['sqlalchemy_DATABASE_URI'] = 'postgresql://postgres:password@localhost/demo'
# # db = SQLAlchemy(app)
#
# df.to_sql("my_table_name", engine)

#
#
# sql import sql to read csv
# fillnaa automatic correction
# missing files 3,5
# import pandas as pd
# import psycopg2
# from datetime import datetime, timedelta
#
#
# d = pd.read_csv("C:\\Users\\raju\\OneDrive\\Documents\\ordertable.csv",
#                 encoding = "ISO-8859-1", engine='python')
# df = pd.DataFrame(d)
# print(df)
# conn = psycopg2.connect(
#     database="demo",user="postgres",password='admin', host="localhost",port=5432
# )
# cur = conn.cursor()
#
# cur.execute("select * from ordertable")
# df = pd.DataFrame(cur.fetchall(),columns=['order_id','order_name','order_date'])
# #cur.executemany("select * from ordertable_arc")
# #df = pd.DataFrame(cur.fetchall(),columns=['order_id','order_name','order_date'])
# #print(df)
# #df['order_date'] = pd.to_datetime(df['order_date'])
# # data =[('1','samsung j1','01-01-2022'),
# #        ('2', 'samsung j2','02-01-2022'),
#        ('3', 'samsung j3', 'none'),
#        ('4', 'oneplus 6','02-01-2022'),
#        ('5', 'oneplus 7', 'none'),
#        ('6', 'oneplus 8','02-01-2022'),
#        ('7', 'realme gt', '02-01-2022'),
#        ('8', 'oppo k1','02-01-2022'),
#        ('9', 'iphone 13', '02-01-2022'),
# #        ('10', 'iphone 14','02-01-2022')]
# sql = "INSERT INTO ordertable(order_id,order_name,order_date) VALUES (%s,%s,%s)"
# cur.execute(sql,data)
# conn.commit()
#



















