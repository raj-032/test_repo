import pandas as pd
# df = pd.read_excel("C:\\Users\\raju\\OneDrive\\Documents\\sample_data.xlsx")
#
# print(df)
# print(df.shape)
#
df = pd.read_csv("C:\\Users\\raju\\OneDrive\\Documents\\Sample_Spreadsheet.csv",
                encoding = "ISO-8859-1", engine='python')
print(df)
#
#
# result = df.head(10)
# print("First 10 rows of the DataFrame:")    #1st 10 rows
# print(result)
#
# df_last_10 = df.tail(10)
#                                              #last 10 rows
# print(df_last_10)
#
#
#
# print(list(df.columns))      # column names
#
#
#
# df = pd.read_excel("C:\\Users\\raju\\OneDrive\\Documents\\sample_data.xlsx")
# newdf = df.drop_duplicates()
#
# print(newdf)           # remove duplicates
#
#
#
#
# df = df.drop_duplicates(subset='Trainee', keep="first")   #specific column
#
# print(df)
#
# df = pd.DataFrame()       #empty data frame
#
# print(df)

import pandas as pd
import psycopg2
from datetime import datetime,timedelta

d = pd.read_csv




