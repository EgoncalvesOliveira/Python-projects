import pyodbc
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=HomeComputer;"
                      "Database=Automation;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
cursor.execute('exec [dbo].[Pessoas] 1, ''feva''')

#for row in cursor:
 #   print('row = %r' % (row,))
