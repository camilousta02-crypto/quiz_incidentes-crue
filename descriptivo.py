import pandas as pd
import numpy as np



df = pd.read_csv("incidentes_crue_diarios.txt", sep="\t")


df['fecha'] = pd.to_datetime(df['fecha'])

incidentes = df['incidentes']

print("\n========== ANÁLISIS DESCRIPTIVO ==========\n")


media = np.mean(incidentes)
mediana = np.median(incidentes)
moda = incidentes.mode()[0]

print("MEDIA:", media)
print("MEDIANA:", mediana)
print("MODA:", moda)

# ==============================
# MEDIDAS DE DISPERSIÓN
# ==============================

desv_std = np.std(incidentes, ddof=1)
varianza = np.var(incidentes, ddof=1)
cv = (desv_std / media) * 100
rango = np.max(incidentes) - np.min(incidentes)

print("\nDESVIACIÓN ESTÁNDAR:", desv_std)
print("VARIANZA:", varianza)
print("COEFICIENTE DE VARIACIÓN (%):", cv)
print("RANGO:", rango)


q1 = np.percentile(incidentes, 25)
q2 = np.percentile(incidentes, 50)
q3 = np.percentile(incidentes, 75)
iqr = q3 - q1
p95 = np.percentile(incidentes, 95)

print("\nQ1 (25%):", q1)
print("Q2 (Mediana):", q2)
print("Q3 (75%):", q3)
print("RANGO INTERCUARTÍLICO (IQR):", iqr)
print("PERCENTIL 95:", p95)


max_dia = df.loc[incidentes.idxmax()]
min_dia = df.loc[incidentes.idxmin()]

print("\nDÍA CON MÁS INCIDENTES:")
print("Fecha:", max_dia['fecha'])
print("Valor máximo:", max_dia['incidentes'])

print("\nDÍA CON MENOS INCIDENTES:")
print("Fecha:", min_dia['fecha'])
print("Valor mínimo:", min_dia['incidentes'])