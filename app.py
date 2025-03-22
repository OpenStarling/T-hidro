import streamlit as st
import numpy as np
import plotly.graph_objects as go
import uuid
from threephasehorizontal import dm_oil

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

# 🔹 Sidebar: Поля ввода параметров
if st.button("Two-Phase Vertical" and "Two-Phase Horizontal"):
    Qg = st.sidebar.number_input("Gas Flowrate (MMscfd)", min_value=1.0, max_value=99999.0, value=6.6)
    Qo = st.sidebar.number_input("Oil Flowrate (BOPD)", min_value=500, max_value=99999, value=2000)
    Po = st.sidebar.number_input("Inlet Pressure (psia)", min_value=0, max_value=5000, value=1000)
    To = st.sidebar.number_input("Inlet Temperature (°R)", min_value=-100, max_value=1000, value=600)
    Sg = st.sidebar.number_input("Gas Specific Gravity", min_value=0.55, max_value=1.07, value=0.6)
    SG_oil = st.sidebar.number_input("Oil Specific Gravity", min_value=0.55, max_value=1.07, value=0.876)
    dm_liquid = st.sidebar.number_input("Liquid Droplet Size in the Gas Phase (µ)", min_value=1, max_value=1000, value=140)
    tr_oil = st.sidebar.number_input(" Retention Time (min)", min_value=1.0, max_value=100.0, value=3.0)
else:
    Qg = st.sidebar.number_input("Gas Flowrate (MMscfd)", min_value=1.0, max_value=99999.0, value=6.6)
    Qo = st.sidebar.number_input("Oil Flowrate (BOPD)", min_value=500, max_value=99999, value=2000)
    Po = st.sidebar.number_input("Inlet Pressure (psia)", min_value=0, max_value=5000, value=1000)
    To = st.sidebar.number_input("Inlet Temperature (°R)", min_value=-100, max_value=1000, value=600)
    Sg = st.sidebar.number_input("Gas Specific Gravity", min_value=0.55, max_value=1.07, value=0.6)
    SG_oil = st.sidebar.number_input("Oil Specific Gravity", min_value=0.55, max_value=1.07, value=0.876)
    dm_liquid = st.sidebar.number_input("Water Droplet Size in the Gas Phase (µ)", min_value=1, max_value=1000, value=140)
    dm_oil = st.sidebar.number_input("Oil Droplet Size in the Gas Phase (µ)", min_value=1, max_value=1000, value=140)
    tr_oil = st.sidebar.number_input("Oil Retention Time (min)", min_value=1.0, max_value=100.0, value=3.0)
    tr_water = st.sidebar.number_input("water Retention Time (min)", min_value=1.0, max_value=100.0, value=3.0)
        
    
# 🔹 Функции расчёта
def calculate_z_factor(Sg, Po, To):
    return 0.8 if Sg <= 0.6 else 0.85 if Sg <= 0.7 else 0.9 if Sg <= 0.8 else 0.95

def calculate_gas_density(Sg, Po, To, Z):
    return (2.7 * Sg * Po) / (To * Z)

def calculate_vertical_separator():
    Z = calculate_z_factor(Sg, Po, To)
    rg = calculate_gas_density(Sg, Po, To, Z)
    Cd = 0.34
    Vt = 0.0119 * (((SG_oil * 62.4 - rg) * dm_liquid) / (rg * Cd)) ** 0.5
    d = 420 * ((To * Z * Qg) / Po) * ((rg * Cd / ((SG_oil * 62.4 - rg) * dm_liquid)) ** 0.5)
    
    Leff = tr_oil * Qo / (0.7 * d**2)  # Effective Length
    Lss = 4 * Leff / 3  # Seam-to-Seam Length
    SR = Lss / d  # Slenderness Ratio
    
    return d, Leff, Lss, SR

def calculate_horizontal_separator():
    d, Leff, Lss, SR = calculate_vertical_separator()
    return d, Leff, Lss, SR

# 🔹 Функция для построения **вертикальной** 3D-модели сепаратора
def create_3d_model_vertical(diameter):
    height = diameter * 2  
    theta = np.linspace(0, 2 * np.pi, 100)
    r = diameter / 2
    
    # Создаем сетку для цилиндра
    z = np.linspace(0, height, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = r * np.cos(theta_grid)
    y_grid = r * np.sin(theta_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="blues", opacity=0.9))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=True), 
            yaxis=dict(visible=True), 
            zaxis=dict(visible=True)
        ), 
        margin=dict(l=10, r=10, b=10, t=40), 
        showlegend=False, 
        autosize=True
    )
    

    return fig

def create_3d_model_horizontal(diameter, length):
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, length, 100)
    theta_grid, z_grid = np.meshgrid(theta, z)
    
    x_grid = z_grid  # Используем ось z как длину сепаратора
    y_grid = (diameter / 2) * np.cos(theta_grid)
    z_grid = (diameter / 2) * np.sin(theta_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="blues", opacity=0.9, showscale=False))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=True),
            yaxis=dict(visible=True),
            zaxis=dict(visible=True)
        ),
        margin=dict(l=10, r=10, b=10, t=40),
        showlegend=False,
        autosize=True
    )


    return fig



st.markdown("###  Separator Sizing & 3D Visualization")
if st.button("Calculate Separator"):
    if "Vertical" in separator_type:
        d, Leff, Lss, SR = calculate_vertical_separator()
        fig = create_3d_model_vertical(d)
    else:  # Горизонтальный сепаратор
        d, Leff, Lss, SR = calculate_horizontal_separator()
        fig = create_3d_model_horizontal(d, Lss)

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

        
        
        
    
