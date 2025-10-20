# Tesina - Detección de Fraudes en Tokens ERC-20

Versión inicial simplificada del proyecto de tesis que desarrolla una herramienta para detectar patrones de manipulación y posibles estafas en tokens **ERC-20**, combinando análisis **on-chain** y **machine learning** con datos de **BigQuery**.  
Esta versión presenta una base funcional y resumida de la herramienta para detección temprana de fraudes cripto.

---

# Detección de Patrones de Manipulación en Mercados Criptográficos

**Autor:** Pablo Castillo Martínez  
**Lugar:** Santiago de Chile  
**Fecha:** 18 de septiembre de 2025  
**Proyecto:** Trabajo Final del Máster en Data Science y Big Data – Universidad Complutense de Madrid  

---

## 🧠 Descripción
Esta versión inicial del proyecto implementa una herramienta básica de detección de fraudes en tokens **ERC-20**, usando **modelos supervisados** y datos on-chain.  
El enfoque combina **Google BigQuery** para la extracción y procesamiento de datos, junto con modelos de aprendizaje automático de complejidad media.

El objetivo principal de esta versión es ofrecer una base reproducible y fácilmente extensible, priorizando claridad y simplicidad sobre optimización.

---

## ⚙️ Estructura del proyecto

| Archivo / Notebook | Descripción |
|--------------------|-------------|
| `tfm_2025_09_basededatos.ipynb` | Extracción y construcción de la base de datos desde BigQuery y CoinGecko. |
| `tfm_2025_09_preprocesado.ipynb` | Limpieza, imputación, codificación y escalado de datos. |
| `tfm_2025_09_modelado.ipynb` | Entrenamiento de modelos básicos (Logistic Regression, Random Forest, XGBoost, LightGBM). |
| `tfm_2025_09_gui.py` | Interfaz gráfica inicial (Tkinter) para pruebas de clasificación. |

---

## 🧩 Modelos utilizados
- **Regresión Logística** (mejor desempeño global ~75 % balanced accuracy)  
- **Random Forest**  
- **XGBoost / LightGBM**  
- **Gradient Boosting**

> 💡 En esta versión, los modelos fueron entrenados sobre un subconjunto reducido del dataset original para facilitar la replicación.

---

## 📊 Dataset
Datos públicos on-chain desde **BigQuery (GCP)**, procesando información resumida de ~5 000 tokens ERC-20.  
Variables incluidas:
- Número de transferencias  
- Concentración top 10 holders  
- Antigüedad del token  
- Actividad media y desviación de transferencias  

---

## 🚀 Resultados
- **Regresión Logística** obtuvo el mejor equilibrio entre precisión y estabilidad.  
- Modelos complejos mostraron sobreajuste en esta versión reducida.  
- Se implementó una **interfaz gráfica simple** para realizar inferencias locales.

---

## 🔮 Próximos pasos
- Integrar fuentes adicionales (Nansen, Dune, Etherscan API).  
- Aumentar el tamaño y balanceo del dataset.  
- Migrar la herramienta hacia un entorno web interactivo.  

---

## 📄 Licencia
Versión simplificada publicada bajo la **Licencia MIT**, permitiendo uso, modificación y redistribución con atribución al autor original.

---
