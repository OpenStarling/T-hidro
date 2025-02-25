import streamlit as st
import numpy as np
import plotly.graph_objects as go
import uuid
import requests
import os
import datetime

# 🔹 Уникальный ID пользователя для отслеживания
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())[:8]

# 🔹 Устанавливаем широкоформатный режим страницы
st.set_page_config(layout="wide")

st.markdown("""
    <style>
        /* Обычное состояние (серый контур) */
        div[data-baseweb="selectContainer"] {
            border: 1px solid #000 !important;/* Серый */
            border-radius: 10px !important;
            transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
            box-sizing: border-box;
            background-clip: padding-box;
        }

        /* Активное состояние (синий при фокусе) */
        div[data-baseweb="select"]:focus-within {
            border: 2px solid #007BFF !important; /* Синий */
            border-radius: 10px !important;
            box-sizing: border-box;
        }

        /* Убираем красную рамку при ошибке */
        div[data-baseweb="select"][aria-invalid="true"] {
            border: 1px solid #007BFF !important;
        }

        /* Стили для выпадающего списка (меню) */
        div[data-baseweb="popover"] {
            border: 1px solid #007BFF !important;
        }

        /* Кнопка раскрытия списка (стрелка) */
        div[data-baseweb="icon"] path {
            fill: #007BFF !important; /* Синяя стрелка */
        }

        /* Кнопка раскрытия при наведении */
        div[data-baseweb="icon"]:hover path {
            fill: #0056b3 !important; /* Темно-синий */
        }

        /* Обычное состояние инпута (серый) */
        div[data-testid="stNumberInputContainer"] {
            border: 1px solid #000 !important; /* Серый цвет */
            border-radius: 7px !important;
            transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
        }
  
        /* Активное состояние инпута (синий при фокусе) */
        div[data-testid="stNumberInputContainer"]:focus-within {
            border: 1px solid #007BFF !important; /* Синий */
            
        }

        /* Кнопки (-/+) по умолчанию */
        button[data-testid="stNumberInputStepDown"],
        button[data-testid="stNumberInputStepUp"] {
            border: 1px solid #ffffff00 !important; /* Серый */
            transition: border-color 0.2s ease-in-out, background-color 0.2s ease-in-out;
        }

        /* Кнопки (-/+) при наведении (синие) */
        button[data-testid="stNumberInputStepDown"]:hover,
        button[data-testid="stNumberInputStepUp"]:hover {
            border: 1px solid #007BFF !important; /* Синий */
            background-color: #007BFF !important; /* Легкое синее выделение */
        }

        /* Кнопки (-/+) при нажатии */
        button[data-testid="stNumberInputStepDown"]:active,
        button[data-testid="stNumberInputStepUp"]:active {
            border: 2px solid #0056b3 !important; /* Темно-синий */
            background-color: rgba(0, 86, 179, 0.2) !important; /* Темно-синее выделение */
        }
    </style>
""", unsafe_allow_html=True)


# 🔹 Sidebar: Логотип
st.sidebar.image("assets/Страница 1 (5).svg", width=300)

# 🔹 Sidebar: Выбор типа сепаратора
separator_type = st.sidebar.selectbox(
    "Choose Separator Type",
    ("Two-Phase Vertical", "Two-Phase Horizontal", "Three-Phase Vertical", "Three-Phase Horizontal")
)

# 🔹 Sidebar: Поля ввода параметров
Qg = st.sidebar.number_input("Gas Flowrate (MMscfd)", min_value=1.0, max_value=99999.0, value=6.6)
Qo = st.sidebar.number_input("Oil Flowrate (BOPD)", min_value=500, max_value=99999, value=2000)
Qw = st.sidebar.number_input("Water Flowrate (BPD)", min_value=500, max_value=99999, value=2000)
Po = st.sidebar.number_input("Inlet Pressure (psia)", min_value=0, max_value=5000, value=1000)
To = st.sidebar.number_input("Inlet Temperature (°R)", min_value=-100, max_value=1000, value=600)
Sg = st.sidebar.number_input("Gas Specific Gravity", min_value= 0.55, max_value=1.07, value=0.6)
SG_oil = st.sidebar.number_input("Oil Specific Gravity", min_value= 0.55, max_value=1.07, value=0.876)
SG_water = st.sidebar.number_input("Water Specific Gravity",min_value= 0.55, max_value=1.07, value=1.0)
dm_liquid = st.sidebar.number_input("Liquid Droplet Size in the Gas Phase (µ)", min_value=1, max_value=1000, value=140)
dm_oil = st.sidebar.number_input("Oil Droplet Size in the Water Phase (µ)", min_value=1, max_value=1000, value=200)
dm_water = st.sidebar.number_input("Water Droplet Size in the Oil Phase (µ)",  min_value=1, max_value=1000, value=500)
tr_oil = st.sidebar.number_input("Oil Retention Time (min)", min_value=1.0, max_value=100.0, value=3.0)
tr_water = st.sidebar.number_input("Water Retention Time (min)", min_value=1.0, max_value=100.0, value=3.0)

# 🔹 Функции расчёта Z-фактора и плотности газа
def calculate_z_factor(Sg, Po, To):
    if Sg <= 0.6:
        return 0.8
    elif Sg <= 0.7:
        return 0.85
    elif Sg <= 0.8:
        return 0.9
    else:
        return 0.95

def calculate_gas_density(Sg, Po, To, Z):
    return (2.7 * Sg * Po) / (To * Z)

# 🔹 Функции расчёта для двух- и трехфазных сепараторов
def calculate_twophase_vertical():
    Z = calculate_z_factor(Sg, Po, To)
    rg = calculate_gas_density(Sg, Po, To, Z)
    Cd = 0.34
    Vt = 0.0119 * (((SG_oil * 62.4 - rg) * dm_liquid) / (rg * Cd)) ** 0.5
    d = 420 * ((To * Z * Qg) / Po) * ((rg * Cd / ((SG_oil * 62.4 - rg) * dm_liquid)) ** 0.5)
    SR = d / (2 * d)
    return d, Vt, rg, SR

def calculate_twophase_horizontal():
    Z = calculate_z_factor(Sg, Po, To)
    rg = calculate_gas_density(Sg, Po, To, Z)
    Cd = 0.34
    Vt = 0.0119 * (((SG_oil * 62.4 - rg) * dm_liquid) / (rg * Cd)) ** 0.5
    d = 420 * ((To * Z * Qg) / Po) * ((rg * Cd / ((SG_oil * 62.4 - rg) * dm_liquid)) ** 0.5)
    Leff = tr_oil * Qo / (0.7 * d**2)
    Lss = 4 * Leff / 3
    SR = d / Lss  
    return d, Leff, Lss, Vt, rg, SR

def calculate_threephase():
    d_gas, Vt_gas, rg_gas, SR_gas = calculate_twophase_vertical()
    d_liquid = 0.5 * d_gas  # Примерное значение
    Leff = tr_oil * Qo / (0.7 * d_liquid**2)
    Lss = 4 * Leff / 3
    return d_gas, d_liquid, Leff, Lss, Vt_gas, rg_gas, SR_gas


st.markdown("### Separator sizing & 3D visualisation")
# 🔹 Кнопка "Calculate Separator"
if st.button("Calculate Separator"):
    if separator_type == "Two-Phase Vertical":
        d, Vt, rg, SR = calculate_twophase_vertical()
    elif separator_type == "Two-Phase Horizontal":
        d, Leff, Lss, Vt, rg, SR = calculate_twophase_horizontal()
    elif separator_type == "Three-Phase Vertical":
        d, d_liquid, Leff, Lss, Vt, rg, SR = calculate_threephase()
    elif separator_type == "Three-Phase Horizontal":
        d, d_liquid, Leff, Lss, Vt, rg, SR = calculate_threephase()

    # 🔹 Вывод результатов
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Calculation Results")
        st.markdown(f"**Gas Section Diameter:** `{d:.2f} inches`")
        if "Three-Phase" in separator_type:
            st.markdown(f"**Liquid Section Diameter:** `{d_liquid:.2f} inches`")
        st.markdown(f"**Slenderness Ratio (SR):** `{SR:.2f}`")
        st.markdown(f"**Gas Density:** `{rg:.2f} lb/ft³`")

    # 🔹 Функция для построения 3D-модели сепаратора
     # 🔹 Функция для построения 3D-модели сепаратора
    def create_3d_model(diameter, orientation="vertical"):
        if orientation == "vertical":
            height = diameter * 2  # Total height for vertical separator
            theta = np.linspace(0, 2 * np.pi, 100)
            x = np.linspace(0, height, 100)
            theta_grid, x_grid = np.meshgrid(theta, x)
            y_grid = (diameter / 2) * np.cos(theta_grid)
            z_grid = (diameter / 2) * np.sin(theta_grid)
        else:
            height = diameter  # For horizontal separator, height is the diameter
            theta = np.linspace(0, 2 * np.pi, 100)
            x = np.linspace(0, diameter * 3, 100)  # Length of horizontal separator
            theta_grid, x_grid = np.meshgrid(theta, x)
            y_grid = (diameter / 2) * np.cos(theta_grid)
            z_grid = (diameter / 2) * np.sin(theta_grid)
    
        fig = go.Figure()
        fig.add_trace(go.Surface(x=x_grid, y=y_grid, z=z_grid, colorscale="blues", opacity=0.9))
        fig.update_layout(
            title="3D Separator Model",
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



    with col2:
        fig = create_3d_model(d)
        st.plotly_chart(fig, use_container_width=True)
