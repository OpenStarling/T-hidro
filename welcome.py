import streamlit as st
import time
import os

# Устанавливаем широкоформатный режим
st.set_page_config(layout="wide")

# Приветственная страница
st.title("🌟 Welcome to T-Hydrocarbo Separator Calculator")
st.image("assets/Страница 1 (5).svg", width=300)  # Используем логотип из assets
st.write(
    """
    This tool helps engineers visualize separator calculations.
    Select the separator type, input parameters, and generate 
    accurate calculations with interactive 3D visualization.
    """
)

# Кнопка для перехода к калькулятору
if st.button("Go to Calculator"):
    st.write("Redirecting to Calculator...")
    
    # Ожидание перед переходом
    time.sleep(1)
    
    # Завершаем welcome.py и запускаем app.py
    os.system("python -m streamlit run app.py")
    
    # Останавливаем Streamlit, чтобы нельзя было вернуться
    st.stop()
