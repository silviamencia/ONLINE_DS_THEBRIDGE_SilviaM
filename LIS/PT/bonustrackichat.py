# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:41:02 2025

@author: silvi
"""

Diseño del Datamart:

Definición del modelo dimensional.
Identificación de hechos, dimensiones y relaciones.
Representación mediante un diagrama.

Implementación en Python con Pandas:

Carga y limpieza de los datos.
Transformaciones necesarias.
Cálculo de medidas y creación de las tablas del datamart.
Escritura de los resultados en archivos CSV.

Voy a comenzar con la primera parte.


Diseño del Datamart

1. Procesos de Negocio a Modelar

El sistema de BI debe soportar dos tipos principales de análisis:

Análisis Financiero de Compras

Importe total de compras diarias por sección de la empresa.
Conversión de monedas usando el tipo de cambio en la fecha de factura.

Análisis de Proveedores

Ranking de proveedores por importe total comprado y número de
referencias compradas.
Evaluación de la calidad del proveedor basada en el lead time real vs teórico.

2. Granularidad del Modelo

Definimos dos tablas de hechos:

Fact_Purchases (Compras por Producto y Factura)

Granularidad: Una fila por producto comprado en una factura.

Fact_Supplier_Performance (Evaluación de Proveedores)

Granularidad: Una fila por producto-proveedor y año.

3. Dimensiones

Se definen las siguientes dimensiones:

Dim_Date: Fecha de la compra (factura), del pedido y de la recepción.
Dim_Section: Secciones de la empresa a las que van destinadas las compras.
Dim_Supplier: Datos del proveedor (país, moneda, etc.).
Dim_Product: Datos de los productos comprados.
Dim_Currency: Histórico de tipos de cambio diarios.

4. Tablas de Hechos

Fact_Purchases

ID Factura ID Producto ID Sección Fecha Factura Cantidad Precio en
Moneda Tipo de Cambio Precio en EUR
1001 5001 10 2024-02-10 20 15.00 USD 0.90 270.00

Fact_Supplier_Performance

ID Proveedor ID Producto Año Lead Time Real Lead Time Teórico Diferencia
2001 5001 2024 25 20 +5

5. Relaciones entre Tablas

Fact_Purchases se relaciona con Dim_Date, Dim_Section, Dim_Supplier,
Dim_Product y Dim_Currency.
Fact_Supplier_Performance se relaciona con Dim_Supplier y Dim_Product.


He diseñado el modelo del datamart, incluyendo las tablas de hechos y
dimensiones, así como sus relaciones. Ahora procederé a la
implementación en Python con Pandas para cargar, transformar y generar
los datos del datamart.

Bi Datamart Design editado

He añadido una columna "Diferencia" en la tabla de evaluación de
proveedores para calcular la diferencia entre el lead time real y el
teórico. Ahora, procederé con la implementación en Python usando
Pandas.


He implementado el procesamiento de los datos en Python utilizando
pandas. El código carga los datos, realiza las transformaciones
necesarias (como conversión de monedas y cálculo de lead time), y
guarda los resultados en archivos CSV. Si necesitas ajustes o mejoras,
avísame.


import pandas as pd

# Carga de los ficheros
invoice_header = pd.read_csv('Invoice_header.csv')
invoice_products = pd.read_csv('Invoice_products.csv')
products = pd.read_csv('Products.csv')
suppliers = pd.read_csv('Suppliers.csv')
daily_currencies = pd.read_csv('Daily_currencies.csv')

# Conversión de fechas
invoice_header['Fecha Factura'] = pd.to_datetime(invoice_header['Fecha
Factura'])
invoice_header['Fecha Pedido'] = pd.to_datetime(invoice_header['Fecha Pedido'])
invoice_header['Fecha Recepcion'] =
pd.to_datetime(invoice_header['Fecha Recepcion'])

daily_currencies['Fecha'] = pd.to_datetime(daily_currencies['Fecha'])

# Unimos las compras con los productos y secciones
fact_purchases = invoice_products.merge(invoice_header, on='ID Factura')
fact_purchases = fact_purchases.merge(products, on='ID Producto')

# Incorporamos los tipos de cambio para calcular precios en EUR
fact_purchases = fact_purchases.merge(suppliers[['ID Proveedor',
'Moneda']], on='ID Proveedor')
fact_purchases = fact_purchases.merge(daily_currencies,
                                      left_on=['Fecha Factura', 'Moneda'],
                                      right_on=['Fecha', 'Moneda'],
                                      how='left')

fact_purchases['Precio en EUR'] = fact_purchases['Precio en Moneda'] *
fact_purchases['Tipo de Cambio']

# Cálculo de lead time
fact_supplier_performance = invoice_header[['ID Proveedor', 'ID
Factura', 'Fecha Pedido', 'Fecha Recepcion']].copy()
fact_supplier_performance['Lead Time Real'] =
(fact_supplier_performance['Fecha Recepcion'] -

fact_supplier_performance['Fecha Pedido']).dt.days

# Asignación de lead time teórico
conditions = [
    suppliers['Pais'] == 'España',
    suppliers['Pais'].isin(['Francia', 'Alemania', 'Italia', 'Portugal']),
    ~suppliers['Pais'].isin(['España', 'Francia', 'Alemania',
'Italia', 'Portugal'])
]
values = [10, 20, 45]
suppliers['Lead Time Teorico'] = pd.np.select(conditions, values)

fact_supplier_performance =
fact_supplier_performance.merge(suppliers[['ID Proveedor', 'Lead Time
Teorico']],
                                                            on='ID Proveedor')
fact_supplier_performance['Diferencia'] =
fact_supplier_performance['Lead Time Real'] -
fact_supplier_performance['Lead Time Teorico']

# Guardamos los datos transformados
fact_purchases.to_csv('Fact_Purchases.csv', index=False)
fact_supplier_performance.to_csv('Fact_Supplier_Performance.csv', index=False)