# 🚲 Análisis de Movilidad Urbana con PySpark

[![Python](https://img.shields.io/badge/Python-3.12+-blue)](https://www.python.org/)
[![Spark](https://img.shields.io/badge/Spark-3.5.0-orange)](https://spark.apache.org/)
[![License: GPL v2](https://img.shields.io/badge/Licencia-GPLv2-blue.svg)](./LICENSE)

Este proyecto realiza un análisis distribuido de datos simulados de movilidad urbana en la Ciudad de México, utilizando **Apache Spark**.

---

## 💡 Descripción General

Se procesaron más de **1000 registros simulados** de viajes de bicicleta compartida en la CDMX para analizar:

- Horarios de mayor congestión.
- Rutas más concurridas.
- Estaciones de mayor actividad.

Se utilizó **PySpark** para manejar los datos de forma distribuida y **Matplotlib** para visualizar los resultados.

---

## ⚙️ Tecnologías utilizadas

- Python 3.12+
- Apache Spark 3.5.0 (PySpark)
- Pandas
- Matplotlib

---

## 🗺️ Diagrama del proceso

📎 [`Diagrama de flujo de vialidad.pdf`](./Diagrama%20de%20flujo%20de%20vialidad.pdf)

---

## 📊 Visualización generada

📎 [`grafica_origenes.png`](./grafica_origenes.png)

---

## 📁 Archivos del Proyecto

- 📜 [`main.py`](./main.py) — Código fuente principal
- 🗺️ [`Diagrama de flujo de vialidad.pdf`](./Diagrama%20de%20flujo%20de%20vialidad.pdf) — Diagrama del flujo de procesamiento
- 📄 [`viajes_bici.csv`](./viajes_bici.csv) — Dataset base
- 📄 [`rutas_populares.csv`](./rutas_populares.csv) — Rutas más utilizadas
- 📄 [`resumen_origenes.csv`](./resumen_origenes.csv) — Conteo por estación origen
- 📄 [`resumen_destinos.csv`](./resumen_destinos.csv) — Conteo por estación destino
- 🧾 [`Practica_Spark.pdf`](./Practica_Spark.pdf) — Informe completo de la práctica

---

## ✅ Uso ético de IA

Durante el desarrollo de esta práctica se utilizó inteligencia artificial como asistencia técnica para:

- Generación de datasets simulados.
- Estructuración de código y corrección de errores.
- Formato y presentación del repositorio.

El uso fue documentado de manera responsable como apoyo al aprendizaje.

---

## ✨ Conclusión

El proyecto permitió aplicar Apache Spark para procesamiento distribuido en un escenario urbano realista, logrando optimizar consultas, resúmenes y análisis masivos de movilidad de forma eficiente.
