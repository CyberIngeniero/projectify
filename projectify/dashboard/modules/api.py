import pandas as pd
import requests
import streamlit as st

BASE_URL = "https://pypistats.org/api/packages/projectify"


def fetch_data(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data from {endpoint}: {response.status_code}")
        return None


def get_recent_downloads():
    data = fetch_data("recent")
    if data:
        return pd.DataFrame.from_dict(
            data["data"], orient="index", columns=["Descargas"]
        ).reset_index()
    return pd.DataFrame()


def get_overall_downloads(include_mirrors=False):
    params = {"mirrors": "true"} if include_mirrors else None
    data = fetch_data("overall", params=params)
    if data:
        df = pd.DataFrame(data["data"])
        df["date"] = pd.to_datetime(df["date"])
        return df
    return pd.DataFrame()


def get_downloads_by_python_major(version=None):
    params = {"version": version} if version else None
    data = fetch_data("python_major", params=params)
    if data:
        df = pd.DataFrame(data["data"])
        df["date"] = pd.to_datetime(df["date"])
        return df
    return pd.DataFrame()


def get_downloads_by_python_minor(version=None):
    params = {"version": version} if version else None
    data = fetch_data("python_minor", params=params)
    if data:
        df = pd.DataFrame(data["data"])
        df["date"] = pd.to_datetime(df["date"])
        return df
    return pd.DataFrame()


def get_downloads_by_system(os_name=None):
    params = {"os": os_name} if os_name else None
    data = fetch_data("system", params=params)
    if data:
        df = pd.DataFrame(data["data"])
        df["date"] = pd.to_datetime(df["date"])
        return df
    return pd.DataFrame()


def get_downloads_by_project_version():
    response = requests.get("https://pypistats.org/api/packages/projectify/overall")
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data["data"])
        return df[df["category"] != "null"]
    else:
        return pd.DataFrame(columns=["category", "date", "downloads"])


# Funciones adicionales para agrupar por mes y año


def get_monthly_downloads(df):
    """
    Agrupa las descargas por mes.
    """
    if not df.empty:
        df["month"] = df["date"].dt.to_period("M")
        monthly_df = df.groupby("month").agg({"downloads": "sum"}).reset_index()
        monthly_df["month"] = monthly_df["month"].dt.to_timestamp()
        return monthly_df
    return pd.DataFrame()


def get_yearly_downloads(df):
    """
    Agrupa las descargas por año.
    """
    if not df.empty:
        df["year"] = df["date"].dt.to_period("Y")
        yearly_df = df.groupby("year").agg({"downloads": "sum"}).reset_index()
        yearly_df["year"] = yearly_df["year"].dt.to_timestamp()
        return yearly_df
    return pd.DataFrame()
