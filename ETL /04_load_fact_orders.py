from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
import urllib

SERVER = r"TU_SERVIDOR\SQLEXPRESS"
DB_NAME = "OLIST_PRICING"
SCHEMA = "dbo"
TABLE = "fact_orders"

CSV_FILE = Path(__file__).resolve().parent.parent / "data" / "olist_orders_dataset.csv"

# Leer CSV
df = pd.read_csv(CSV_FILE, encoding="utf-8")

cols = [
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]
df = df[cols]

# Convertir fechas
for c in cols[3:]:
    df[c] = pd.to_datetime(df[c], errors="coerce")

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
    chunksize=300,
    method=None
)

print("✅ fact_orders cargada correctamente")
