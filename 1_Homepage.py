import streamlit as st

st.set_page_config(page_title="Homepage", page_icon="media/logo.png", layout="wide")
st.sidebar.image("media/logo.png")
st.sidebar.title("EnZone")

st.markdown(
    """
    <style>
        .reportview-container .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            text-align: center;
            color: #7ED957;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("EnZone Homepage")

st.image(image = "media/1.png", use_column_width=True)

st.sidebar.markdown(
    """
    **Informasi Kontak**\n
    **Telepon       : +628-9560-6415-240**\n
    **Instagram     : enzone_id**\n
    **Email         : support.id@enzone.com**\n


    Hak Cipta © 2023 EnZone: Energy PLTB Potential Zone Application
    """
)
