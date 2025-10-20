# Tesina-deteccion-fraudes-erc20
El proyecto desarrolla una herramienta que detecta patrones de manipulación y posibles estafas en tokens ERC-20 mediante análisis on-chain y machine learning en BigQuery. Clasifica tokens según su confiabilidad y ofrece una base funcional para detección temprana de fraudes cripto.

# Detección de Patrones de Manipulación en Mercados Criptográficos

**Autor:** Pablo Castillo Martínez  
**Lugar:** Santiago de Chile  
**Fecha:** 18 de septiembre de 2025  
**Proyecto:** Trabajo Final del Máster en Data Science y Big Data – Universidad Complutense de Madrid  

---

## 🧠 Descripción
Este proyecto implementa una herramienta de detección temprana de fraudes en tokens **ERC-20**, combinando **análisis on-chain** con **modelos de machine learning**.  
Los datos se obtienen desde **Google BigQuery**, aplicando técnicas de procesamiento, balanceo y modelado supervisado.

La herramienta permite estimar la probabilidad de que un token presente patrones fraudulentos (p. ej. *rugpull*, *honeypot* o *ponzi*), entregando una interfaz funcional para usuarios no técnicos.

---

## ⚙️ Estructura del proyecto

| Archivo / Notebook | Descripción |
|--------------------|-------------|
| `tfm_2025_09_basededatos.ipynb` | Extracción y construcción de la base de datos desde BigQuery y CoinGecko. |
| `tfm_2025_09_preprocesado.ipynb` | Limpieza, imputación, codificación y escalado de datos. |
| `tfm_2025_09_modelado.ipynb` | Entrenamiento de modelos (Logistic Regression, Random Forest, XGBoost, LightGBM). |
| `tfm_2025_09_gui.py` | Interfaz gráfica (Tkinter) para clasificación e inferencia interactiva. |

---

## 🧩 Modelos utilizados
- **Regresión Logística** (mejor desempeño global ~75 % balanced accuracy)  
- **Random Forest**  
- **XGBoost / LightGBM**  
- **Gradient Boosting**

---

## 📊 Dataset
Datos públicos on-chain desde **BigQuery (GCP)**, procesando más de **5 000 tokens** y varios terabytes de información.  
Variables principales:  
- Número de transferencias  
- Concentración top 10 holders  
- Actividad y antigüedad del token  
- Desviación estándar y promedio diario de transferencias  

---

## 🚀 Resultados
- Logistic Regression alcanzó los mejores resultados en detección equilibrada de clases.  
- Los modelos complejos fueron menos estables por falta de datos etiquetados.  
- Se desarrolló un **dashboard funcional** para uso no técnico.  

---

## 🔮 Recomendaciones futuras
- Incorporar fuentes adicionales (Nansen, Dune, Etherscan API).  
- Mejorar el etiquetado de tokens y aumentar el dataset balanceado.  
- Extender la herramienta a un **entorno web interactivo**.

---

## 📄 Licencia
Este proyecto se distribuye bajo la **Licencia MIT**, permitiendo uso libre, modificación y distribución con atribución al autor.

