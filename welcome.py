import streamlit as st
import os

# Set wide screen mode
st.set_page_config(layout="wide")

# Initialize session state for button tracking
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

# JavaScript function to update Python session state
toggle_js = """
<script>
    document.addEventListener("DOMContentLoaded", function() {
        document.getElementById("start-button").addEventListener("click", function() {
            fetch('/_stcore/set_query_params?page=app')
                .then(response => response.json())
                .then(data => {
                    console.log("State updated to True");
                    window.location.reload();
                });
        });
    });
</script>
"""

# Apply styles
st.markdown(
    """
    <style>
        body {
            background-color: #0E1117;
            margin: 0;
            padding: 0;
        }
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 5vh;
            position: relative;
            flex-direction: column;
        }
        .text-container {
            text-align: center;
            color: white;
        }
        .speech-bubble {
            position: absolute;
            top: -4em;
            right: 10%;
            width: 400px;
            background: white;
            padding: 15px;
            border-radius: 15px;
            font-size: 14px;
            font-weight: bold;
            text-align: center;
            color: #000;
            box-shadow: 3px 3px 10px rgba(255, 255, 255, 0.2);
            animation: fadeIn 1.5s ease-in-out;
        }
        .speech-bubble::after {
            content: "";
            position: absolute;
            bottom: -15px;
            left: 50%;
            margin-left: -10px;
            border-width: 10px;
            border-style: solid;
            border-color: white transparent transparent transparent;
        }
        .engineer {
            position: absolute;
            right: -6%;
            bottom: -40em;
            width: 380px;
            animation: fadeIn 2s ease-in-out;
        }
        .button-container {
            margin-top: 20px;
            display: flex;
            justify-content: center;
        }
        .custom-button {
            padding: 15px 35px;
            font-size: 20px;
            background: linear-gradient(135deg, #FF4B4B, #E03E3E);
            color: white;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease-in-out;
            box-shadow: 0px 5px 15px rgba(255, 75, 75, 0.3);
            text-align: center;
        }
        .custom-button:hover {
            background: linear-gradient(135deg, #E03E3E, #FF4B4B);
            transform: scale(1.08);
            box-shadow: 0px 8px 18px rgba(255, 75, 75, 0.5);
        }
        .footer {
            position: absolute;
            bottom: -40em;
            width: 100%;
            text-align: center;
            font-size: 14px;
            color: #bbb;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Inject JavaScript into the page
st.markdown(toggle_js, unsafe_allow_html=True)

# Centered text & Custom HTML button
st.markdown(
    """
    <div class="text-container">
        <h1 style="font-size: 42px; font-weight: bold;">Welcome!</h1>
        <p style="font-size: 18px; color: #bbb;">Visualization of three-phase separator calculations.</p>
        <div class="button-container">
            <button id="start-button" class="custom-button">Proceed to Calculations</button>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Speech bubble & Engineer image
st.markdown('<div class="speech-bubble">Welcome! Let’s calculate your separator dimensions.</div>', unsafe_allow_html=True)
st.markdown('<img src="https://i.imgur.com/qDpKpyT.png" class="engineer">', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Read query parameters to update Streamlit state
query_params = st.query_params

if query_params.get("page") == ["app"]:
    st.session_state.button_clicked = True

# Run app.py if button was clicked
if st.session_state.button_clicked:
    os.system("python -m streamlit run app.py")
