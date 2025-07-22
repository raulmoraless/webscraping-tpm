import pandas as pd
import matplotlib.pyplot as plt

# URL de la tabla web
url = "https://si3.bcentral.cl/Siete/ES/Siete/Cuadro/CAP_TASA_INTERES/MN_TASA_INTERES_09/TPM_C1/T12?cbFechaDiaria=2025&cbFrecuencia=MONTHLY&cbCalculo=NONE&cbFechaBase="

# Leer tabla desde la web
tablas = pd.read_html(url)
tabla = tablas[0]

# Extraer fila con TPM (la primera) y columnas desde la segunda en adelante
tpm_valores = tabla.iloc[0, 1:]
fechas_raw = tabla.columns[1:]

# Crear DataFrame con fechas y valores
df = pd.DataFrame({
    "FechaStr": fechas_raw,
    "TPM": tpm_valores.values
})

# EXTRAER nombre de mes y año
df['MesStr'] = df['FechaStr'].str.extract(r'([A-Za-záéíóúñÑ]+)', expand=False).str.lower().str[:3]
df['Año'] = df['FechaStr'].str.extract(r'(\d{4})')

# Eliminar filas sin año o sin mes reconocido
df = df.dropna(subset=['MesStr', 'Año'])

# Mapear meses a número
meses_map = {
    'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'ago': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dic': 12
}
df['Mes'] = df['MesStr'].map(meses_map)

# Eliminar filas con mes no reconocido
df = df.dropna(subset=['Mes'])

# Convertir año a entero
df['Año'] = df['Año'].astype(int)

# Construir columna de fecha
df['Fecha'] = pd.to_datetime(dict(year=df['Año'], month=df['Mes'], day=1))

# Convertir TPM a número
df['TPM'] = pd.to_numeric(df['TPM'], errors='coerce')
df = df.dropna(subset=['TPM'])

# Ordenar por fecha
df = df.sort_values('Fecha')

# Graficar
plt.figure(figsize=(10, 5))
plt.plot(df['Fecha'], df['TPM'], marker='o')
plt.title('TPM Mensual - Banco Central de Chile')
plt.xlabel('Fecha')
plt.ylabel('TPM (%)')
plt.grid(True)
plt.tight_layout()
plt.show()
