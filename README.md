# 📊 Olist Pricing Analytics

Proyecto de análisis de datos end-to-end basado en el dataset de e-commerce Olist.  
El objetivo es analizar pricing, logística y comportamiento del cliente utilizando Python, SQL Server y Power BI.

## 🧱 Arquitectura

CSV → Python (ETL) → SQL Server → Power BI

- **Python**: Ingesta y transformación de datos (pandas, SQLAlchemy)  
- **SQL Server**: Almacenamiento estructurado con claves primarias y foráneas  
- **Power BI**: Modelo analítico, medidas DAX y dashboard interactivo  

## 📊 Dashboard

El dashboard está construido en una sola página con navegación mediante bookmarks:

1. **Resumen Ejecutivo** – KPIs principales y desempeño de ventas  
2. **Operaciones y Logística** – Tiempos de entrega, retrasos e impacto del freight  
3. **Producto y Cliente** – Análisis por categorías y comportamiento del cliente  

## 🗄️ Modelo de Datos

Esquema estrella compuesto por:

- Tablas de hechos: `fact_orders`, `fact_order_items`  
- Tablas de dimensiones: `dim_product`, `dim_category`, `dim_customer`, `dim_seller`  

## ⚙️ Tecnologías

- Python (pandas, SQLAlchemy)  
- SQL Server  
- Power BI  
- DAX  

## 📌 Notas

- Los datos fueron cargados a SQL Server mediante procesos ETL en Python  
- La estructura relacional (PK/FK) fue definida mediante SQL  
- El modelo analítico fue construido en Power BI  

