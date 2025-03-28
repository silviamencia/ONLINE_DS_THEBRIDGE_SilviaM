# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 12:38:29 2025

@author: silvi
"""

import os
import pandas as pd
import pandas as pd
os.chdir(r"C:\Users\silvi\Downloads\BonusTrackDatos\DatosProyecto")
df_daily_currencies = pd.read_csv("daily_currencies.csv", delimiter=";")
df_invoices_header=pd.read_csv("invoices_header.csv", delimiter=";")
df_invoices_products=pd.read_csv("invoices_products.csv", delimiter=";")
df_products=pd.read_csv("products.csv", delimiter=";")
df_suppliers=pd.read_csv("suppliers.csv", delimiter=";")

df_daily_currencies['Date'] = pd.to_datetime(df_daily_currencies['Date'])
df_invoices_header["InboundDate"] = pd.to_datetime(df_invoices_header["InboundDate"])
df_invoices_header["OrderDate"] = pd.to_datetime(df_invoices_header["OrderDate"])
df_invoices_header["InvoiceDate"] = pd.to_datetime(df_invoices_header["InvoiceDate"])
df_products=df_products.dropna(subset=["Type"])
df_products=df_products.dropna(subset=["Division", "Product"])
df_products=df_products.dropna(subset=["ShortDescription"])
df_suppliers=df_suppliers.dropna(subset=["PaymentMethod", "PaymentTerms"])
df_daily_currencies.info()
df_invoices_header.info()
df_invoices_products.info()
df_products.info()
df_suppliers.info()
df_invoices_header = df_invoices_header.rename(columns={"Supplier": "IDSupplier"})
tabla_compras=pd.merge(df_invoices_header, df_invoices_products, on="Invoice")
tabla_compras=pd.merge(tabla_compras, df_products, on="Product")
tabla_compras=pd.merge(tabla_compras, df_suppliers, on="IDSupplier")

df['F'] = df_suppliers.apply(lambda row: row['A'] * row['B'], axis=1)