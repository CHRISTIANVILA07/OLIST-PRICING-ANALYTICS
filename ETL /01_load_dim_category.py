from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

csv_path = Path(__file__).resolve().parent.parent / "data" / "product_category_name_translation.csv"
df = pd.read_csv(csv_path, encoding="utf-8")

df = df.rename(columns={
    "product_category_name": "category_name_pt",
    "product_category_name_english": "category_name_en"
})

print(df.head())
print("Filas:", len(df))

server = r"TU_SERVIDOR\SQLEXPRESS"
database = "OLIST_PRICING"

conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine("mssql+pyodbc:///?odbc_connect=" + quote_plus(conn_str))

# Test conexión
with engine.connect() as conn:
    print("✅ Conectado a SQL Server correctamente")

# Cargar datos
df.to_sql("dim_category", engine, schema="dbo", if_exists="append", index=False)
print("✅ Carga completada a dbo.dim_category")
