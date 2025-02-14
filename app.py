import streamlit as st
import numpy as np
import plotly.graph_objects as go
import uuid

import streamlit as st
import requests
import os
import subprocess

# Укажи SSH или HTTPS ссылку на свой репозиторий
GIT_REPO_SSH = "git@github.com:OpenStarling/T-hidrogit"  # Если используешь SSH
GIT_REPO_HTTPS = "https://<SHA256:yh3bQ5TaT2NtOdGnq9rtjvYLJP9ElKaWRBqtW+spOSk>@github.com/OpenStarling/T-hidro.git"  # Если используешь Token

# Файл для хранения списка посетителей
VISITOR_FILE = "visitors.txt"

# Функция для получения IP пользователя
def get_visitor_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        return response.json()["ip"]
    except Exception:
        return "Не удалось получить IP"

# Функция для загрузки списка посетителей
def load_visitors():
    if os.path.exists(VISITOR_FILE):
        with open(VISITOR_FILE, "r") as file:
            return file.read().splitlines()
    return []

# Функция для сохранения IP в файл
def save_visitor(ip):
    with open(VISITOR_FILE, "a") as file:
        file.write(ip + "\n")

# Функция для обновления GitHub-репозитория
def update_github():
    try:
        subprocess.run(["git", "config", "--global", "user.name", "GitHub Actions Bot"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "actions@github.com"], check=True)
        subprocess.run(["git", "add", VISITOR_FILE], check=True)
        subprocess.run(["git", "commit", "-m", "Автообновление списка посетителей"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        st.success("Данные успешно обновлены в GitHub!")
    except subprocess.CalledProcessError:
        st.warning("Не удалось обновить данные в GitHub. Проверь настройки доступа.")

# Загружаем список сохраненных IP
saved_visitors = load_visitors()

# Получаем IP текущего пользователя
user_ip = get_visitor_ip()

# Если пользователя еще нет в списке, добавляем
if user_ip not in saved_visitors:
    save_visitor(user_ip)
    saved_visitors.append(user_ip)
    update_github()  # Автоматически отправляем изменения в GitHub

# Вывод информации
st.write(f"**Ваш IP:** `{user_ip}`")
st.write("### 📌 История посещений (сохранено в файле и GitHub):")
for ip in saved_visitors:
    st.write(f"🔹 {ip}")











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
