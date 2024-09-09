# dashboard.py
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def display_total_downloads(df):
    st.subheader("Gráfico de Descargas Totales")
    plt.figure(figsize=(10, 6))
    sns.lineplot(x="date", y="downloads", data=df, marker="o")
    plt.title("Descargas Totales a lo Largo del Tiempo")
    plt.xlabel("Fecha")
    plt.ylabel("Número de Descargas")
    st.pyplot(plt)


def display_recent_downloads(recent_downloads_df):
    st.subheader("Descargas recientes")
    if not recent_downloads_df.empty:
        st.table(recent_downloads_df)


def display_overall_downloads(overall_downloads_df):
    st.subheader("Descargas totales a lo largo del tiempo")
    if not overall_downloads_df.empty:
        overall_chart = (
            alt.Chart(overall_downloads_df)
            .mark_line()
            .encode(x="date:T", y="downloads:Q", color="category:N")
            .properties(width=700, height=400)
        )
        st.altair_chart(overall_chart)


def display_downloads_by_python_major(python_major_df):
    st.subheader("Descargas por versión mayor de Python")
    if not python_major_df.empty:
        python_major_chart = (
            alt.Chart(python_major_df)
            .mark_line()
            .encode(x="date:T", y="downloads:Q", color="category:N")
            .properties(width=700, height=400)
        )
        st.altair_chart(python_major_chart)


def display_downloads_by_python_minor(python_minor_df):
    st.subheader("Descargas por versión menor de Python")
    if not python_minor_df.empty:
        python_minor_chart = (
            alt.Chart(python_minor_df)
            .mark_line()
            .encode(x="date:T", y="downloads:Q", color="category:N")
            .properties(width=700, height=400)
        )
        st.altair_chart(python_minor_chart)


def display_downloads_by_system(system_downloads_df):
    st.subheader("Descargas por sistema operativo")
    if not system_downloads_df.empty:
        system_chart = (
            alt.Chart(system_downloads_df)
            .mark_line()
            .encode(x="date:T", y="downloads:Q", color="category:N")
            .properties(width=700, height=400)
        )
        st.altair_chart(system_chart)
