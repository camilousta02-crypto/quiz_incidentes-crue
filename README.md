# Quiz_crue

## 📊 Análisis de Incidentes del CRUE

Este proyecto examina datos diarios del Centro Regulador de Urgencias y Emergencias, registrando tendencias en incidentes de salud críticos durante 2022-2023.

## 📌 Descripción de los datos

Este proyecto analiza registros diarios del Centro Regulador de Urgencias y Emergencias (CRUE).  
El CRUE gestiona incidentes de salud críticos, incluyendo:

- Accidentes caseros (traumas, quemaduras)
- Violencia de género (tentativa de feminicidio, violencia sexual)
- Emergencias médicas (problemas respiratorios, dolores torácicos)

La entidad atiende miles de llamadas diarias y coordina ambulancias 24/7 a través de la línea 123.

- 📊 Total de registros: 730
- 📅 Periodo: 2022 - 2023
- 📌 Frecuencia: diaria

---

## 👥 Colaboradores

| Nombre              | GitHub              |
|---------------------|---------------------|
| Camilo Velandia     | camilousta02        |
| Michael Morantes    | michaelmorantesp    |

---

## 📈 Hallazgos principales

| Estadística | Valor |
|-------------|--------|
| Promedio general de incidentes | 1717.47 |
| Mediana | 1711.00 |
| Desviación estándar | 256.31 |
| Coeficiente de variación | 14.92% |
| Rango (máx - mín) | 2340 |
| Día con más incidentes | 25-12-2022 (3275) |
| Día con menos incidentes | 15-04-2022 (935) |
| Año con mayor promedio | 2023 (1767.85) |
| Día de la semana con más incidentes | Domingo (1880.04) |
| Mes con mayor promedio | Diciembre (1881.02) |
| Mes con menor promedio | Enero (1460.61) |

---

## 🔎 ¿Se puede predecir?

Sí, es posible realizar predicciones debido a que los datos presentan patrones temporales claros, especialmente efectos estacionales por mes y por día de la semana. El aumento en fines de semana y en diciembre sugiere comportamiento sistemático. Modelos de series de tiempo como Holt-Winters o ARIMA podrían capturar tendencia y estacionalidad para generar pronósticos confiables.

## 📊 Serie Temporal Diaria

![Serie Temporal que muestra fluctuaciones diarias de incidentes del CRUE entre 935 y 3275 llamadas durante 2022-2023, con un pico notable el 25 de diciembre de 2022](serie_temporal.png)

## 📆 Promedio Mensual de Incidentes

![Gráfico de línea titulado Promedio mensual de incidentes mostrando el eje X con los 12 meses del 1 al 12 y eje Y con valores de 1460 a 1900 incidentes. La línea muestra baja actividad en enero con 1460 incidentes, ascenso gradual hasta mayo con pico de 1760 incidentes, descenso en junio a 1680, recuperación en septiembre con máximo de 1840 incidentes, ligera caída en octubre a 1760, y cierre en diciembre con 1895 incidentes. El patrón sugiere mayor actividad en fines de año](promedio_mensual.png)