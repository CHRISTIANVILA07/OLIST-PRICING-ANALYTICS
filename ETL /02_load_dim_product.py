from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import urllib

# ========= CONFIG =========
SERVER = r"TU_SERVIDOR\SQLEXPRESS"
DB_NAME = "OLIST_PRICING"
SCHEMA = "dbo"
TABLE = "dim_product"

CSV_FILE = Path(__file__).resolve().parent.parent / "data" / "olist_products_dataset.csv"

# ========= CONEXIÓN =========
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

# ========= LEER CSV =========
df = pd.read_csv(CSV_FILE, encoding="utf-8")
df = df.where(pd.notnull(df), None)

print(df.head())
print("Filas:", len(df))

# ========= INSERT SEGURO =========
df.to_sql(
    name=TABLE,
    con=engine,
    schema=SCHEMA,
    if_exists="append",
    index=False,
    chunksize=200,   # evita el error de 2100 parámetros
    method=None
)

print("✅ Carga completada a dbo.dim_product")
