from dotenv import load_dotenv
from os import getenv
import pyodbc
from sqlalchemy import create_engine

# This library allows the environment variables to be loaded from a file
load_dotenv()

# To get this working quickly, you can just replace these variables with your own values
svr = getenv("MSSQL_SERVER")
uid = getenv("HALLUX_USER")
pwd = getenv("HALLUX_PASSWORD")
db = getenv("HALLUX_DB")

def connect_odbc():
    # Connect to a MS SQL Server Database
    cnn_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};SERVER="
        + svr
        + ";DATABASE="
        + db
        + ";UID="
        + uid
        + ";PWD="
        + pwd
        + ";TrustServerCertificate=yes;"
    )
    print(cnn_string)
    cnn = pyodbc.connect(cnn_string)
    return cnn
    
def connect_alchemy():
    engine = create_engine(f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes", fast_executemany=True)
    return engine

def execute_odbc(cnn, query):    
    # Create the cursor required to run the command
    cur = cnn.cursor()

    # Run the SQL command
    cur.execute(query)

    for row in cur:
        print(row)

def execute_alchemy(engine, query):
    engine = create_engine(f"mssql+pyodbc://{uid}:{pwd}@{svr}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes", fast_executemany=True)
    cnn = engine.connect()
    # execute sql query using
    
    for row in cnn.execute("select top 10 * from band"):
        print(row)

q = "SELECT top 10 * FROM Band"
#execute_odbc(connect_odbc(), query)
execute_alchemy(connect_alchemy(), q)