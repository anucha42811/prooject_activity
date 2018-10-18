import pypyodbc

print("-----------------------------------")

# Database config
mssql_driver = 'SQL Server Native Client 11.0'
mssql_server = 'DESKTOP-STORPRP\SQLEXPRESS'
mssql_db = 'activity'
mssql_user = 'sa'
mssql_pass = '12345'

# Open Database connection
connection = pypyodbc.connect('Driver={'+ mssql_driver +'};Server='+ mssql_server +';Database='+ mssql_db +';uid='+ mssql_user +';pwd='+ mssql_pass)

# Query command
SQL = 'SELECT TOP (10) * FROM [activity].[dbo].[Table1_sleep]'

# Execute
result_obj = connection.cursor().execute(SQL)

# Raw data
# print(result_obj.description)

# Beautiful 
box = []
for row in result_obj.fetchall():
     box.append(row)

print(box)
print('---------------')
print(box[0][-1])

# Close Database connection
connection.close()
