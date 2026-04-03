from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import urllib

# ========= CONFIG =========
SERVER = r"TU_SERVIDOR\SQLEXPRESS"
DB_NAME = "OLIST_PRICING"
SCHEMA = "dbo"
TABLE = "fact_order_items"

CSV_FILE = Path(__file__).resolve().parent.parent / "data" / "olist_order_items_dataset.csv"

# ========= LEER CSV =========
df = pd.read_csv(CSV_FILE, encoding="utf-8")

print(df.head())
print("Filas:", len(df))

# ========= SELECCIONAR COLUMNAS =========
cols = [
    "order_id",
    "order_item_id",
    "product_id",
    "seller_id",
    "shipping_limit_date",
    "price",
    "freight_value"
]
df = df[cols]

# Convertir tipos
df["shipping_limit_date"] = pd.to_datetime(df["shipping_limit_date"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["freight_value"] = pd.to_numeric(df["freight_value"], errors="coerce")

# NaN -> None (para SQL)
df = df.where(pd.notnull(df), None)

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

# Test conexión
with engine.connect() as conn:
    print("✅ Conectado a SQL Server")

# ========= INSERT SEGURO =========
df.to_sql(
    name=TABLE,
    con=engine,
    schema=SCHEMA,
    if_exists="append",
    index=False,
    chunksize=500,   # más columnas → chunk moderado
    method=None
)

print("✅ Carga completada a dbo.fact_order_items")
