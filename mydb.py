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

# Ensure table exists
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

# Optional: Clear all data and reset ID counter
# ---------------------------------------------------
clear_data = False  # Set to True only when you want to delete all and reset IDs

if clear_data:
    cursor.execute("DELETE FROM Customers")
    cursor.execute("DBCC CHECKIDENT ('Customers', RESEED, 0)")
    conn.commit()
    print("All data deleted and ID reset to start from 1.")

# ---------------------------------------------------

# Close connection
cursor.close()
conn.close()


#? ------- SuperUser ---> Username : MB23CRM,  Password: admin --------