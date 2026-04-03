USE OLIST_PRICING;
GO

/* =========================================================
   DOCUMENTACIÓN DEL ESQUEMA RELACIONAL
   Proyecto: OLIST Pricing Dashboard
   Objetivo:
   Formalizar las claves primarias y foráneas de las tablas
   ya cargadas en SQL Server mediante procesos ETL en Python.
   ========================================================= */


/* =========================================================
   1. PRIMARY KEYS
   ========================================================= */

/* -------------------------------
   Tabla: dbo.dim_category
   Clave primaria:
   - category_name_pt
-------------------------------- */
ALTER TABLE dbo.dim_category
ADD CONSTRAINT PK_dim_category
PRIMARY KEY (category_name_pt);
GO


/* -------------------------------
   Tabla: dbo.dim_customer
   Clave primaria:
   - customer_id
-------------------------------- */
ALTER TABLE dbo.dim_customer
ADD CONSTRAINT PK_dim_customer
PRIMARY KEY (customer_id);
GO


/* -------------------------------
   Tabla: dbo.dim_product
   Clave primaria:
   - product_id
-------------------------------- */
ALTER TABLE dbo.dim_product
ADD CONSTRAINT PK_dim_product
PRIMARY KEY (product_id);
GO


/* -------------------------------
   Tabla: dbo.dim_seller
   Clave primaria:
   - seller_id
-------------------------------- */
ALTER TABLE dbo.dim_seller
ADD CONSTRAINT PK_dim_seller
PRIMARY KEY (seller_id);
GO


/* -------------------------------
   Tabla: dbo.fact_orders
   Clave primaria:
   - order_id
-------------------------------- */
ALTER TABLE dbo.fact_orders
ADD CONSTRAINT PK_fact_orders
PRIMARY KEY (order_id);
GO


/* -------------------------------
   Tabla: dbo.fact_order_items
   Clave primaria compuesta:
   - order_id
   - order_item_id
-------------------------------- */
ALTER TABLE dbo.fact_order_items
ADD CONSTRAINT PK_fact_order_items
PRIMARY KEY (order_id, order_item_id);
GO



/* =========================================================
   2. FOREIGN KEYS
   ========================================================= */

/* -------------------------------
   Relación:
   fact_orders.customer_id
   -> dim_customer.customer_id
-------------------------------- */
ALTER TABLE dbo.fact_orders
ADD CONSTRAINT FK_fact_orders_dim_customer
FOREIGN KEY (customer_id)
REFERENCES dbo.dim_customer(customer_id);
GO


/* -------------------------------
   Relación:
   fact_order_items.order_id
   -> fact_orders.order_id
-------------------------------- */
ALTER TABLE dbo.fact_order_items
ADD CONSTRAINT FK_fact_order_items_fact_orders
FOREIGN KEY (order_id)
REFERENCES dbo.fact_orders(order_id);
GO


/* -------------------------------
   Relación:
   fact_order_items.product_id
   -> dim_product.product_id
-------------------------------- */
ALTER TABLE dbo.fact_order_items
ADD CONSTRAINT FK_fact_order_items_dim_product
FOREIGN KEY (product_id)
REFERENCES dbo.dim_product(product_id);
GO


/* -------------------------------
   Relación:
   fact_order_items.seller_id
   -> dim_seller.seller_id
-------------------------------- */
ALTER TABLE dbo.fact_order_items
ADD CONSTRAINT FK_fact_order_items_dim_seller
FOREIGN KEY (seller_id)
REFERENCES dbo.dim_seller(seller_id);
GO


/* -------------------------------
   Relación:
   dim_product.product_category_name
   -> dim_category.category_name_pt

-------------------------------- */
ALTER TABLE dbo.dim_product
ADD CONSTRAINT FK_dim_product_dim_category
FOREIGN KEY (product_category_name)
REFERENCES dbo.dim_category(category_name_pt);
GO
