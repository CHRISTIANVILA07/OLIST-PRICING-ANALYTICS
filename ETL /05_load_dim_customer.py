from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import urllib

SERVER = r"TU_SERVIDOR\SQLEXPRESS"
DB_NAME = "OLIST_PRICING"
SCHEMA = "dbo"
TABLE = "dim_customer"

CSV_FILE = Path(__file__).resolve().parent.parent / "data" / "olist_customers_dataset.csv"

df = pd.read_csv(CSV_FILE, encoding="utf-8")
df = df.where(pd.notnull(df), None)

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DB_NAME};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={params}",
    fast_executemany=True
)

df.to_sql(
    TABLE,
    engine,
    schema=SCHEMA,
    if_exists="append",
    index=False,
    chunksize=500,
    method=None
)

print("✅ dim_customer cargada correctamente")
