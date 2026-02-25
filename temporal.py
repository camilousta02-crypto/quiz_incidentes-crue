import pandas as pd

# ==============================
# 1. Cargar datos (separado por espacios)
# ==============================

df = pd.read_csv("incidentes_crue_diarios.txt", sep=r"\s+")

# Convertir fecha a datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Crear variables auxiliares
df["año"] = df["fecha"].dt.year
df["mes"] = df["fecha"].dt.month
df["dia_semana"] = df["fecha"].dt.day_name()

# ==============================
# 2. PROMEDIO POR AÑO
# ==============================

promedio_2022 = df[df["año"] == 2022]["incidentes"].mean()
promedio_2023 = df[df["año"] == 2023]["incidentes"].mean()
diferencia = promedio_2023 - promedio_2022

print("PROMEDIO POR AÑO")
print(f"Promedio 2022: {promedio_2022:.2f}")
print(f"Promedio 2023: {promedio_2023:.2f}")
print(f"Diferencia (2023-2022): {diferencia:.2f}")
print()

# ==============================
# 3. PROMEDIO POR DÍA DE LA SEMANA
# ==============================

promedio_dias = df.groupby("dia_semana")["incidentes"].mean()

orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday",
              "Friday", "Saturday", "Sunday"]

promedio_dias = promedio_dias.reindex(orden_dias)

dias_es = {
    "Monday": "Lunes",
    "Tuesday": "Martes",
    "Wednesday": "Miércoles",
    "Thursday": "Jueves",
    "Friday": "Viernes",
    "Saturday": "Sábado",
    "Sunday": "Domingo"
}

print("PROMEDIO POR DÍA DE LA SEMANA")

for dia in orden_dias:
    print(f"{dias_es[dia]}: {promedio_dias[dia]:.2f}")

dia_mayor = promedio_dias.idxmax()
print(f"Día con MÁS incidentes: {dias_es[dia_mayor]}")
print()

# ==============================
# 4. PROMEDIO POR MES
# ==============================

promedio_mes = df.groupby("mes")["incidentes"].mean()
mes_ordenado = promedio_mes.sort_values(ascending=False)

top3 = mes_ordenado.head(3)
mes_mas_bajo = promedio_mes.idxmin()

print("PROMEDIO POR MES")
print(f"Mes #1 (más alto): {top3.index[0]}  Promedio: {top3.iloc[0]:.2f}")
print(f"Mes #2: {top3.index[1]}  Promedio: {top3.iloc[1]:.2f}")
print(f"Mes #3: {top3.index[2]}  Promedio: {top3.iloc[2]:.2f}")
print(f"Mes más BAJO: {mes_mas_bajo}  Promedio: {promedio_mes[mes_mas_bajo]:.2f}")