import pandas as pd
import json
technologies = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000],
    'Duration':['30days','50days','35days','40days','60days','35days','55days','50days'],
    'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
                })
df = pd.DataFrame(technologies, columns=['Courses','Fee','Duration','Discount'])
print(df)

# Using groupby() and count()
df2 = df.groupby(['Courses'])['Courses'].count()
print(df2)

# Using GroupBy & count() on multiple column
df2 = df.groupby(['Courses','Duration'])['Fee'].count()
print(df2)

# Using GroupBy & size() on multiple column
df2 = df.groupby(['Courses','Duration'])['Fee'].size()
print(df2)

# using DataFrame.size() and max()
df2 = df.groupby(['Courses','Duration']).size().groupby(level=0).max()
print(df2)

# Use size().reset_index() method
df2 = df.groupby(['Courses','Duration']).size().reset_index(name='counts')
print(df2)

# Using pandas DataFrame.reset_index()
df2 = df.groupby(['Courses','Duration'])['Fee'].agg('count').reset_index()
print(df2)

#Using DataFrame.transform()
df2 = df.groupby(['Courses','Duration']).Courses.transform('count')
print(df2)

#Use DataFrame.groupby() and Size()
print(df.groupby(['Discount','Duration']).size()
   .sort_values(ascending=False)
   .reset_index(name='count')
   .drop_duplicates(subset='Duration'))



df = pd.DataFrame([['Jay',16,'BBA'],
                   ['Jack',19,'BTech'],
                   ['Mark',18,'BSc']],
                  columns = ['Name','Age','Course'])

print(df)

js = df.to_json(orient = 'columns')

js = df.to_json(orient = 'records')

js = df.to_json(orient = 'index')

js = df.to_json(orient = 'split')

js = df.to_json(orient = 'table')

print(js)


countries_df = pd.DataFrame({
    "country":["india","us","pakistan"],"state":[["ap","telangana"],["california","texas"],["islamabad","balochistan"]]})
print(countries_df)


data = [['india',['bengalore','ap','hyderabad']],
        ['pakistan',['islamabad','lahore','balochisthan']],
        ['us',['california','texas','alaska']]]

df = pd.DataFrame(data,columns = ['country','state'])

print(df)

df1 = df.explode('state')
print(df1)

