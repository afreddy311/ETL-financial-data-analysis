# 📊 Proyecto: ETL de Datos Financieros en Python

## 🌟 Descripción

Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** en Python para analizar datos financieros simulados.
El flujo permite extraer transacciones, transformarlas en resúmenes por mes y categoría, y cargarlas en un archivo final listo para visualización.

👉 Es un ejemplo de construccion de un flujo de trabajo reproducible y escalable para análisis financieros.

---

## 🧰 Tecnologías utilizadas

* **Python**
* **Pandas** para manipulación de datos
* **Git/GitHub** para control de versiones
*  más adelante: **Airflow**, **Power BI**, **SQL**

---

## 📂 Estructura del proyecto

```text
etl_finanzas/
├── data/
│   ├── transacciones_financieras.csv      # Dataset de entrada
│   └── resumen_gastos_mensual.csv         # Salida del ETL
├── etl/
│   ├── extract.py                         # Extraer datos
│   ├── transform.py                       # Transformar datos
│   └── load.py                            # Cargar datos
├── main.py                                # Orquestador del pipeline
└── requirements.txt
```

---

## 🔁 Flujo ETL

1. **Extract** → Lee datos financieros desde un CSV.
2. **Transform** → Limpia y agrupa los gastos por mes y categoría.
3. **Load** → Exporta los resultados a un archivo CSV listo para visualización.

---

## 📊 Resultados esperados

* Archivo CSV con el gasto total por categoría y mes.
* Listo para graficar en **Python (Matplotlib/Seaborn)** o en **Power BI/Tableau**.

Ejemplo de salida:

| month   | category     | total\_amount |
| ------- | ------------ | ------------- |
| 2024-05 | Restaurante  | 480.50        |
| 2024-05 | Supermercado | 1250.30       |
| 2024-06 | Transporte   | 350.20        |

---

## 🚀 Próximos pasos

* Integración con **Airflow** para orquestación.
* Guardar resultados en una base de datos SQL.
* Construir un **dashboard financiero** (Power BI / Streamlit).

---

## 👤 Autor

Desarrollado por **Freddy de la Cruz**
💎 [LinkedIn](https://www.linkedin.com/in/freddyarturo311proyect/) | [GitHub](https://github.com/afreddy311)
