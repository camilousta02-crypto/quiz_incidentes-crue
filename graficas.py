import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

# ==============================
# 1️⃣ CARGA Y PREPARACIÓN
# ==============================

df = pd.read_csv("incidentes_crue_diarios.txt", sep=r"\s+")
df.columns = df.columns.str.strip()

df["fecha"] = pd.to_datetime(df["fecha"])
df = df.sort_values("fecha")

# ==============================
# 2️⃣ SERIE TEMPORAL COMPLETA
# ==============================

plt.figure()
plt.plot(df["fecha"], df["incidentes"])
plt.xlabel("Fecha")
plt.ylabel("Incidentes")
plt.title("Serie temporal diaria de incidentes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# 3️⃣ MEDIA MÓVIL 7 DÍAS
# ==============================

df["media_movil_7"] = df["incidentes"].rolling(window=7, center=True).mean()

plt.figure()
plt.plot(df["fecha"], df["incidentes"], label="Incidentes diarios")
plt.plot(df["fecha"], df["media_movil_7"], label="Media móvil 7 días")
plt.xlabel("Fecha")
plt.ylabel("Incidentes")
plt.title("Serie con media móvil de 7 días")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# 4️⃣ PROMEDIO POR DÍA DE SEMANA
# ==============================

df["dia_semana"] = df["fecha"].dt.day_name()

orden_dias = ["Monday", "Tuesday", "Wednesday", "Thursday",
              "Friday", "Saturday", "Sunday"]

promedio_dias = df.groupby("dia_semana")["incidentes"].mean()
promedio_dias = promedio_dias.reindex(orden_dias)

plt.figure()
plt.bar(orden_dias, promedio_dias)
plt.xlabel("Día de la semana")
plt.ylabel("Promedio de incidentes")
plt.title("Promedio de incidentes por día de la semana")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==============================
# 5️⃣ PROMEDIO MENSUAL
# ==============================

df["mes"] = df["fecha"].dt.month

promedio_mes = df.groupby("mes")["incidentes"].mean()

plt.figure()
plt.plot(promedio_mes.index, promedio_mes.values)
plt.xlabel("Mes")
plt.ylabel("Promedio de incidentes")
plt.title("Promedio mensual de incidentes")
plt.xticks(range(1,13))
plt.tight_layout()
plt.show()

# ==============================
# 6️⃣ DESCOMPOSICIÓN TEMPORAL
# ==============================

df_ts = df.set_index("fecha")

descomposicion = seasonal_decompose(df_ts["incidentes"], model="additive", period=7)

descomposicion.plot()
plt.tight_layout()
plt.show()

# ==============================
# 7️⃣ AUTOCORRELACIÓN (ACF)
# ==============================

plt.figure()
plot_acf(df["incidentes"], lags=30)
plt.title("Función de Autocorrelación (ACF)")
plt.tight_layout()
plt.show()