# Import Python Libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple

# Ruta al archivo Excel
file_path = "Data/Volve production data-1.xlsx"

# Insert an icon
icon = Image.open("Resources/logo.jpg")

# State the design of the app
st.set_page_config(page_title="Campo Volve", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
footer {
  display: none;
}
</style>""",
    unsafe_allow_html=True,
)

# Insert title for app
st.title("Historial de produccion del Campo Volve")

st.write("---")

# Add information of the app
st.markdown(
    """
    Esta aplicacion nos permitira visualizar y analizar los datos de produccion del campo volve.

    """
)


# Insert Image
image = Image.open("Resources/principal.jpg")
st.image(image, width=100, use_container_width=True)

# Add title to the sidebar section
st.sidebar.title("⬇ Navigation")

# Add sections of the app
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "Plots", ],
        icons=["house", "tv-fill", "box", ],

)
if options == "Data":
    try:
        excel_data = pd.ExcelFile(file_path)
        sheet_name = "Daily Production Data"
        df = excel_data.parse(sheet_name)

        selected_columns = ['NPD_WELL_BORE_NAME', 'DATEPRD', 'BORE_OIL_VOL', 'BORE_GAS_VOL', 'BORE_WAT_VOL']
        extracted_data = df[selected_columns]



    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")