#
#!--- Connecting to Microsoft SQL Server ----

import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=LAPTOP-APLJD65M\\MSSQLSERVER01;'
    'DATABASE=DCRM;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
    'Encrypt=yes;'
)

cursor = conn.cursor()

cursor.execute("""
    IF NOT EXISTS (
        SELECT * FROM sys.tables WHERE name = 'Customers'
    )
    CREATE TABLE Customers (
        ID INT PRIMARY KEY IDENTITY(1,1),
        Name NVARCHAR(100),
        Email NVARCHAR(100)
    )
""")

conn.commit()
print("Connected and ensured table exists!")

# Close connection
cursor.close()
conn.close()


#? ------- SuperUser ---> Username : MB23CRM,  Password: admin --------