import pandas as pd
import plotly.express as px
import streamlit as st
from modules import (
    get_downloads_by_system,
    get_monthly_downloads,
    get_overall_downloads,
)

# Título y Descripción
st.set_page_config(page_title="Projectify! Dashboard", layout="wide")
st.title("📊 Projectify! Dashboard")

# Mostrar el total de descargas acumuladas
overall_df = get_overall_downloads()
total_downloads = overall_df["downloads"].sum()
st.write("### Descargas Acumuladas")
st.metric(
    label="Descargas Acumuladas",
    value=f"{total_downloads:,}",
    label_visibility="collapsed",
)

# Gráfico de Descargas Totales a lo largo del tiempo (sin filtro de tipo de descarga)
st.write("### Descargas Totales")
fig_total_downloads = px.area(
    overall_df,
    x="date",
    y="downloads",
    title="Descargas Totales a lo Largo del Tiempo",
    labels={"date": "Fecha", "downloads": "Número de Descargas"},
    line_shape="linear",
    markers=True,
)
fig_total_downloads.update_traces(line=dict(color="royalblue", width=2))
st.plotly_chart(fig_total_downloads)

# Gráfico de Descargas Agrupadas por Mes (sin filtro de tipo de descarga)
st.write("### Descargas Agrupadas por Mes")
monthly_df = get_monthly_downloads(overall_df)

if not monthly_df.empty:
    monthly_df["year"] = monthly_df["month"].dt.year
    available_years = monthly_df["year"].unique()
    selected_year = st.selectbox(
        "Seleccionar Año", ["Todos"] + list(available_years), key="monthly_year"
    )

    if selected_year != "Todos":
        filtered_monthly_df = monthly_df[monthly_df["year"] == selected_year]
    else:
        filtered_monthly_df = monthly_df

    filtered_monthly_df["month_name"] = filtered_monthly_df["month"].dt.strftime("%B")

    fig_monthly_downloads = px.line(
        filtered_monthly_df,
        x="month_name",
        y="downloads",
        title="Descargas Agrupadas por Mes",
        labels={"month_name": "Mes", "downloads": "Número de Descargas"},
    )
    fig_monthly_downloads.update_traces(line=dict(color="blue", width=2))
    st.plotly_chart(fig_monthly_downloads)
else:
    st.write(
        "No hay datos disponibles para mostrar en el gráfico de descargas agrupadas por mes."
    )

# Gráfico de Descargas por Sistema Operativo (con filtro de tipo de descarga)
st.write("### Descargas por Sistema Operativo")

# Filtro: with_mirrors/without_mirrors para gráficos
mirror_filter = st.selectbox(
    "Seleccionar Tipo de Descarga", ["Todos"] + list(overall_df["category"].unique())
)

# Filtrar el dataframe general según el filtro seleccionado
if mirror_filter != "Todos":
    filtered_overall_df = overall_df[overall_df["category"] == mirror_filter]
else:
    filtered_overall_df = overall_df

os_df = get_downloads_by_system()

# Filtro de año y mes para el gráfico de sistema operativo
os_df["year"] = pd.to_datetime(os_df["date"]).dt.year
os_df["month"] = pd.to_datetime(os_df["date"]).dt.month_name()

selected_year_os = st.selectbox(
    "Seleccionar Año", ["Todos"] + list(os_df["year"].unique()), key="os_year"
)
selected_month_os = st.selectbox(
    "Seleccionar Mes", ["Todos"] + list(os_df["month"].unique()), key="os_month"
)

if selected_year_os != "Todos":
    filtered_os_df = os_df[os_df["year"] == selected_year_os]
else:
    filtered_os_df = os_df

if selected_month_os != "Todos":
    filtered_os_df = filtered_os_df[filtered_os_df["month"] == selected_month_os]

fig_os_downloads = px.bar(
    filtered_os_df,
    x="category",
    y="downloads",
    labels={"category": "Sistema Operativo", "downloads": "Número de Descargas"},
    color="category",
    opacity=1,
)
fig_os_downloads.update_traces(marker=dict(line=dict(width=0)))
st.plotly_chart(fig_os_downloads)
