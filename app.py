import streamlit as st
import numpy as np
import plotly.graph_objects as go
import uuid

# 🔹 Уникальный ID пользователя
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())[:8]

# 🔹 Устанавливаем широкоформатный режим
st.set_page_config(layout="wide")

st.sidebar.image("assets/Страница 1 (5).svg", width=300)

# 🔹 Sidebar: Выбор типа сепаратора
separator_type = st.sidebar.selectbox(
    "Choose Separator Type",
    ("Two-Phase Vertical", "Two-Phase Horizontal", "Three-Phase Vertical", "Three-Phase Horizontal")
)

Qg = st.sidebar.number_input("Gas Flowrate (MMscfd)", min_value=1.0, max_value=99999.0, value=6.6)
Qo = st.sidebar.number_input("Oil Flowrate (BOPD)", min_value=500, max_value=99999, value=2000)
Po = st.sidebar.number_input("Inlet Pressure (psia)", min_value=0, max_value=5000, value=1000)
To = st.sidebar.number_input("Inlet Temperature (°R)", min_value=-100, max_value=1000, value=600)
Sg = st.sidebar.number_input("Gas Specific Gravity", min_value=0.55, max_value=1.07, value=0.6)
SG_oil = st.sidebar.number_input("Oil Specific Gravity", min_value=0.55, max_value=1.07, value=0.876)

oil_density = SG_oil * 62.4

if "Two-Phase" in separator_type:
    dm_liquid = st.sidebar.number_input("Liquid Droplet Size (µm)", 1, 1000, 140)
else:
    dm_liquid = st.sidebar.number_input("Water Droplet Size (µm)", 1, 1000, 140)
    dm_oil = st.sidebar.number_input("Oil Droplet Size (µm)", 1, 1000, 200)
    dm_water = st.sidebar.number_input("Water-in-Oil Droplet Size (µm)", 1, 1000, 500)
    
    
# 🔹 Функции расчёта
def calculate_z_factor(Sg, Po, To):
    return 0.8 if Sg <= 0.6 else 0.85 if Sg <= 0.7 else 0.9 if Sg <= 0.8 else 0.95

def calculate_gas_density(Sg, Po, To, Z):
    return (2.7 * Sg * Po) / (To * Z)

def calculate_threephase_horizontal(dm_liquid, dm_oil, dm_water, oil_density, p, t, SGgas):
    Cd = 0.34
    Z = 0.8 if SGgas <= 0.6 else 0.85 if SGgas <= 0.7 else 0.9
    rg = (2.7 * SGgas * p) / (t * Z)
    Qg = 6.6
    Qo = 2000
    tr_oil = 3.0
    tr_water = 3.0

    d = 420 * ((t * Z * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    Leff = max(tr_oil * Qo, tr_water * Qo) / (0.7 * d**2)
    Lss = Leff * 1.25  # чуть другое отношение длины
    SR = Lss / d
    return d, Leff, Lss, SR

def calculate_threephase_vertical(dm_liquid, dm_oil, dm_water, oil_density, p, t, SGgas):
    Cd = 0.34
    Z = 0.8 if SGgas <= 0.6 else 0.85 if SGgas <= 0.7 else 0.9
    rg = (2.7 * SGgas * p) / (t * Z)
    Qg = 6.6
    Qo = 2000
    tr_oil = 3.0
    tr_water = 3.0

    d = 420 * ((t * Z * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    Leff = (tr_oil * Qo + tr_water * Qo) / (2 * 0.7 * d**2)  # среднее удержание
    Lss = Leff * 1.33
    SR = Lss / d
    return d, Leff, Lss, SR

def calculate_twophase_horizontal(dm_liquid, oil_density, p, t, SGgas):
    Cd = 0.34
    Z = 0.8 if SGgas <= 0.6 else 0.85 if SGgas <= 0.7 else 0.9
    rg = (2.7 * SGgas * p) / (t * Z)
    Qg = 6.6
    Qo = 2000
    tr_oil = 3.0

    d = 420 * ((t * Z * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    Leff = tr_oil * Qo / (0.65 * d**2)  # немного другая константа
    Lss = 4.2 * Leff / 3  # немного длиннее
    SR = Lss / d
    return d, Leff, Lss, SR

def calculate_twophase_vertical(dm_liquid, oil_density, p, t, SGgas):
    Cd = 0.34
    Z = 0.8 if SGgas <= 0.6 else 0.85 if SGgas <= 0.7 else 0.9
    rg = (2.7 * SGgas * p) / (t * Z)
    Qg = 6.6
    Qo = 2000
    tr_oil = 3.0

    d = 420 * ((t * Z * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    Leff = tr_oil * Qo / (0.7 * d**2)
    Lss = 3.8 * Leff / 3  # чуть короче
    SR = Lss / d
    return d, Leff, Lss, SR

# 🔹 Функция для построения **вертикальной** 3D-модели сепаратора
def create_3d_model_vertical(diameter):
    height = diameter * 2  # базовое предположение для вертикальных
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, height, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = (diameter / 2) * np.cos(theta_grid)
    y_grid = (diameter / 2) * np.sin(theta_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="blues", opacity=0.9))
    fig.update_layout(
        scene=dict(xaxis=dict(visible=True), yaxis=dict(visible=True), zaxis=dict(visible=True)),
        margin=dict(l=10, r=10, b=10, t=40),
        showlegend=False,
        autosize=True
    )
    return fig

def create_3d_model_horizontal(diameter, length):
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, length, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = z_grid
    y_grid = (diameter / 2) * np.cos(theta_grid)
    z_grid = (diameter / 2) * np.sin(theta_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="blues", opacity=0.9, showscale=False))
    fig.update_layout(
        scene=dict(xaxis=dict(visible=True), yaxis=dict(visible=True), zaxis=dict(visible=True)),
        margin=dict(l=10, r=10, b=10, t=40),
        showlegend=False,
        autosize=True
    )
    return fig




st.markdown("###  Separator Sizing & 3D Visualization")
if st.button("Calculate Separator"):
    if separator_type == "Three-Phase Horizontal":
        d, Leff, Lss, SR = calculate_threephase_horizontal(dm_liquid, dm_oil, dm_water, oil_density, Po, To, Sg)
        fig = create_3d_model_horizontal(d, Lss)
    elif separator_type == "Three-Phase Vertical":
        d, Leff, Lss, SR = calculate_threephase_vertical(dm_liquid, dm_oil, dm_water, oil_density, Po, To, Sg)
        fig = create_3d_model_vertical(d)
    elif separator_type == "Two-Phase Horizontal":
        d, Leff, Lss, SR = calculate_twophase_horizontal(dm_liquid, oil_density, Po, To, Sg)
        fig = create_3d_model_horizontal(d, Lss)
    elif separator_type == "Two-Phase Vertical":
        d, Leff, Lss, SR = calculate_twophase_vertical(dm_liquid, oil_density, Po, To, Sg)
        fig = create_3d_model_vertical(d)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📊 Calculation Results")
        st.markdown(f"**Diameter:** `{d:.2f} inches`")
        st.markdown(f"**Effective Length (Leff):** `{Leff:.2f} inches`")
        st.markdown(f"**Seam-to-Seam Length (Lss):** `{Lss:.2f} inches`")
        st.markdown(f"**Slenderness Ratio (SR):** `{SR:.2f}`")
    with col2:
        st.plotly_chart(fig, use_container_width=True)   
else:
    st.markdown('<hr style="width:40%">', unsafe_allow_html=True)
    st.markdown("""
        ### Hi there, I'm Tamirlan Abilzhanov!  
        As a petroleum engineering final-year bachelor, worked on implementation of theoretical knowledge for one of the real field tasks.
    
        - Automating separator sizing from "Surface Production Operations by Ken Arnold and Maurice Stewart (2008)".
        - Observing separator  proportions in 3D.
        - Ensuring that separator  sizes will satisfy production conditions and gas/fluid properties.
    
        ###  What is T-Hydrocarbo?
        -  Foresees scenarios of production regime.
        - Allows surface facilities planning.
        - All calculations are automated! 
        """)
    st.markdown('<hr style="width:50%">', unsafe_allow_html=True)
    st.video("https://youtu.be/_OluqXlB_yM")
    st.markdown("""
    <style>
        .centered-image {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .st-emotion-cache-1cvow4s img {
            border-radius: 15px; /* Закругленные углы */
            max-width: 35%; /* Уменьшенный размер */
            position: absolute;
            bottom: -2em;
            right: -5em;             
        }

        .st-emotion-cache-np12kx {
            width: 40%; 
            padding-bottom: 0;
        }

        .st-emotion-cache-1ibsh2c {
            padding-bottom: 0;
        }

        /* 🔹 Адаптивный дизайн для планшетов */
        @media (max-width: 1024px) {
            .st-emotion-cache-1cvow4s img {
                max-width: 50%;
                bottom: -1em;
                right: 0;
            }
        }

        /* 🔹 Адаптивный дизайн для мобильных устройств */
        @media (max-width: 768px) {
            .st-emotion-cache-1cvow4s img {
                max-width: 70%;
                position: static;
                margin: 0 auto;
                display: block;
            }

            .centered-image img {
                display: none;
            }
            .st-emotion-cache-np12kx {
            width: 80%; 
            padding-bottom: 0;
        }
        }

    </style>
""", unsafe_allow_html=True)

    st.markdown('<div class="centered-image"><img src="https://i.imgur.com/qDpKpyT.png"></div>', unsafe_allow_html=True)

        
        
        
    
