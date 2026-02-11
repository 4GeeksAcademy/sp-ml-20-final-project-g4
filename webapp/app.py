import streamlit as st
import pickle
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.express as px

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Predicción de delitos",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODELS_DIR = BASE_DIR / "models"

PROVINCIAS = ["Madrid", "Barcelona", "Valencia", "Alicante", "Castellón"]

# ---------------- CACHE ----------------
@st.cache_resource
def cargar_modelo(model_path):
    with open(model_path, "rb") as f:
        return pickle.load(f)

# ---------------- UI ----------------
st.title("Predicción trimestral de delitos")

st.markdown(
    """
    Esta aplicación muestra la **predicción trimestral de la tasa de hurtos**
    por cada **100.000 habitantes**, utilizando un modelo **SARIMAX** entrenado
    con datos históricos.
    """
)

provincia = st.selectbox(
    " Elige una provincia",
    PROVINCIAS
)

# ---------------- MODELO ----------------
model_path = MODELS_DIR / f"modelo_{provincia.lower()}.pkl"
modelo = cargar_modelo(model_path)

# ---------------- PREDICCIÓN ----------------
st.subheader(" Predicción para los próximos 4 trimestres")

future_exog = np.zeros((4, 1))  # dummy COVID = 0
pred = modelo.forecast(steps=4, exog=future_exog)

# Convertimos a DataFrame para trabajar cómodo
df_pred = pred.reset_index()
df_pred.columns = ["Fecha", "Tasa"]

# ---------------- MÉTRICA DESTACADA ----------------
st.metric(
    label="Última predicción",
    value=f"{df_pred['Tasa'].iloc[-1]:.2f}",
    delta=f"{df_pred['Tasa'].iloc[-1] - df_pred['Tasa'].iloc[0]:.2f}"
)

# ---------------- GRÁFICA ----------------
st.subheader("Evolución prevista")

fig = px.line(
    df_pred,
    x="Fecha",
    y="Tasa",
    markers=True,
    title=f"Predicción trimestral de hurtos – {provincia}",
)

fig.update_layout(
    xaxis_title="Fecha",
    yaxis_title="Tasa por 100.000 habitantes",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- TABLA ----------------
st.subheader("Valores numéricos")

st.dataframe(
    df_pred.style.format({"Tasa": "{:.2f}"}),
    use_container_width=True
)

# ---------------- INFO ----------------
st.caption(
    "Los valores representan una **proyección estadística** basada en "
    "patrones históricos y no constituyen una predicción exacta."
)
