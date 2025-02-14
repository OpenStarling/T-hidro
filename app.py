import streamlit as st
import numpy as np
import plotly.graph_objects as go
import uuid

# 🟢 Генерация уникального ID пользователя для отслеживания
if "user_id" not in st.session_state:
    st.session_state["user_id"] = str(uuid.uuid4())[:8]

# 🟢 Устанавливаем широкоформатный режим страницы
st.set_page_config(layout="wide")

# 🟢 Заголовок страницы
st.title(" Configure Separator")

# 🟢 Sidebar: Выбор типа сепаратора
st.sidebar.image("assets/Страница 1 (5).svg", width=300)  # Новый путь к логотипу
st.sidebar.title("Separator Settings")
separator_type = st.sidebar.selectbox(
    "Choose Separator Type",
    ("Two-Phase Vertical", "Two-Phase Horizontal", "Three-Phase Horizontal", "Three-Phase Vertical")
)

# 🟢 Sidebar: Поля ввода параметров
dm_liquid = st.sidebar.number_input("Liquid Droplet ize (µ)", min_value=10, max_value=500, value=140)
dm_oil = st.sidebar.number_input("Oil Droplet Size (µ)", min_value=10, max_value=500, value=200)
dm_water = st.sidebar.number_input("Water Droplet Size (µ)", min_value=10, max_value=500, value=500)
oil_density = st.sidebar.number_input("Oil Density (lb/ft³)", min_value=30.0, max_value=70.0, value=54.67)
p = st.sidebar.number_input("Pressure (psia)", min_value=500, max_value=3000, value=1000)
t = st.sidebar.number_input("Temperature (°R)", min_value=400, max_value=1000, value=600)
SGgas = st.sidebar.number_input("Gas Specific Gravity", min_value=0.5, max_value=1.0, value=0.6)
Qg = st.sidebar.number_input("Gas Flow Rate (MMscfd)", min_value=1.0, max_value=20.0, value=6.6)
tr = st.sidebar.number_input("Retention Time (min)", min_value=0.5, max_value=10.0, value=3.0)
Qoil = st.sidebar.number_input("Oil Flow Rate (BOPD)", min_value=500, max_value=5000, value=2000)

# 🟢 Функции расчёта для каждого типа сепаратора
def calculate_twophase_vertical():
    Zfactor = 0.8  
    rg = 2.7 * SGgas * p / (t * Zfactor)
    Cd = 0.34
    Vt = 0.0119 * ((((oil_density - rg) * dm_liquid) / (rg * Cd)) ** 0.5)
    d = 420 * ((t * Zfactor * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    SR = d / (2 * d)  
    return d, Vt, rg, SR

def calculate_twophase_horizontal():
    Zfactor = 0.85  
    rg = 2.7 * SGgas * p / (t * Zfactor)
    Cd = 0.34
    Vt = 0.0119 * ((((oil_density - rg) * dm_liquid) / (rg * Cd)) ** 0.5)
    d = 420 * ((t * Zfactor * Qg) / p) * ((rg * Cd / ((oil_density - rg) * dm_liquid)) ** 0.5)
    d_squaredLeff = tr * Qoil / 0.7
    Leff = d_squaredLeff / (d**2)
    Lss = 4 * Leff / 3
    SR = d / Lss  
    return d, Leff, Lss, Vt, rg, SR

# 🟢 Функция для построения 3D-модели сепаратора
def create_3d_model(diameter):
    height = diameter * 2  
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.linspace(0, height, 100)
    theta_grid, x_grid = np.meshgrid(theta, x)
    y_grid = (diameter / 2) * np.cos(theta_grid)
    z_grid = (diameter / 2) * np.sin(theta_grid)

    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=x_grid, 
        y=y_grid, 
        z=z_grid, 
        colorscale="blues", 
        opacity=0.9,
    ))

    fig.update_layout(
        title="3D Separator Model",
        scene=dict(
            xaxis=dict(visible=False),  # Убираем ось X
            yaxis=dict(visible=False),  # Убираем ось Y
            zaxis=dict(visible=False),  # Убираем ось Z
        ),
        margin=dict(l=10, r=10, b=10, t=40),
        showlegend=False,  # Убираем легенду
        autosize=True
    )

    return fig



# 🟢 Перемещение кнопки Calculate на главную страницу
if st.button("Calculate Separator"):
    if separator_type == "Two-Phase Vertical":
        d, Vt, rg, SR = calculate_twophase_vertical()
    elif separator_type == "Two-Phase Horizontal":
        d, Leff, Lss, Vt, rg, SR = calculate_twophase_horizontal()
    else:
        d, Vt, rg, SR = calculate_twophase_horizontal()

    # 🟢 Выводим результаты расчётов
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Calculation Results")
        st.markdown(f"**Diameter:** `{d:.2f} inches`")
        st.markdown(f"**Slenderness Ratio (SR):** `{SR:.2f}`")
        st.markdown(f"**Gas Density:** `{rg:.2f} lb/ft³`")

    with col2:
        # 🟢 Выводим 3D-модель в правой колонке
        fig = create_3d_model(d)
        st.plotly_chart(fig, use_container_width=True)
