# webscraping-tpm
Extracción y visualización de la TPM mensual desde el Banco Central de Chile.


# Web Scraping de la TPM Mensual - Banco Central de Chile

Este proyecto realiza un proceso de **web scraping** para extraer la **Tasa de Política Monetaria (TPM)** mensual desde el sitio web del Banco Central de Chile. Los datos se limpian, transforman y se visualizan en un gráfico de línea.

---

## Tecnologías utilizadas

- Python 3
- pandas
- matplotlib
- BeautifulSoup (usado internamente por `pandas.read_html`)

---

## Fuente de datos

Los datos se obtienen directamente desde el portal del Banco Central de Chile:

https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_TASA_INTERES/MN_TASA_INTERES_09/TPM_C1/T12?cbFechaDiaria=2025&cbFrecuencia=MONTHLY&cbCalculo=NONE&cbFechaBase=

---

## ¿Qué hace el script?

1. Lee una tabla HTML directamente desde la página del Banco Central.
2. Extrae la TPM mensual.
3. Limpia y transforma las fechas y valores.
4. Construye un `DataFrame` con fechas reales.
5. Grafica la evolución de la TPM a lo largo del tiempo.

---


## Cómo ejecutar

1. Asegúrate de tener Python 3 y los paquetes necesarios:

```bash
pip install pandas matplotlib
