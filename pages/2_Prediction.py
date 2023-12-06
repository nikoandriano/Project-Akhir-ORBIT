import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.tree import DecisionTreeRegressor

st.set_page_config(page_title="Prediction", page_icon="media/logo.png", layout="wide")
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

st.title("Prediction")

with st.container():
    uploaded_file = st.file_uploader('CHOOSE A FILE', type=['xlsx', 'xls'])
    save_button = st.button('Save Data')
    
    if save_button:
        if uploaded_file is not None:
            if uploaded_file.name.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(uploaded_file)
                saved_file_name = "weather_valid.csv"
                save_path = os.path.join("./save_folder", saved_file_name)
                df.to_csv(save_path, index=False)
            
            st.success(f"Saved File")

with st.container():
    display_button = st.button('Display Data')

    if display_button:         
        dataset = pd.read_csv('./save_folder/weather_valid.csv')
        st.write(dataset.head())

        markdown_text = """
        ### Meteorological Data:
        - **Tn      :** Temperatur minimum (°C)
        - **Tx      :** Temperatur maksimum (°C)
        - **Tavg    :** Temperatur rata-rata (°C)
        - **RH_avg  :** Kelembapan rata-rata (%)
        - **RR      :** Curah hujan (mm)
        - **ss      :** Lamanya penyinaran matahari (jam)
        - **ff_x    :** Kecepatan angin maksimum (m/s)
        - **ddd_x   :** Arah angin saat kecepatan maksimum (°)
        - **ff_avg  :** Kecepatan angin rata-rata (m/s)
        - **ddd_car :** Arah angin terbanyak (°)
        """

        st.markdown(markdown_text)
        
        Data_Wind = dataset['ff_x'].values
        fig, ax = plt.subplots()
        plt.plot(Data_Wind)
        plt.title('Data Real Graph')
        plt.xlabel("Day")
        plt.ylabel("Wind Speed (m/s)")
        plt.show()
        st.pyplot(fig)   

with st.container():
    predict_button = st.button('Predict Data')
    if predict_button:
        dataset = pd.read_csv('./save_folder/weather_valid.csv')
        Tx_median = dataset['Tx'].median()
        Tavg_median = dataset['Tavg'].median()
        RH_avg_median = dataset['RH_avg'].median()
        RR_median = dataset['RR'].median()
        ss_median = dataset['ss'].median()
        dataset['Tx'].fillna(Tx_median, inplace=True)
        dataset['Tavg'].fillna(Tavg_median, inplace=True)
        dataset['RH_avg'].fillna(RH_avg_median, inplace=True)
        dataset['RR'].fillna(RR_median, inplace=True)
        dataset['ss'].fillna(ss_median, inplace=True)
        Data_Real = dataset.drop(labels=['Tn','Tx','Tavg','RH_avg','RR','ss','ff_x','ddd_car'], axis=1).values
        Data_Wind = dataset['ff_x'].values

        DTReg = DecisionTreeRegressor().fit(Data_Real, Data_Wind)
    
        with open('model.pkl', 'wb') as file:
            pickle.dump(DTReg, file)

        Data_Prediction = DTReg.predict(Data_Real)

        fig, ax = plt.subplots()
        plt.plot(Data_Prediction)
        plt.title('Data Prediction Graph')
        plt.xlabel("Day")
        plt.ylabel("Wind Speed (m/s)")
        plt.show()
        st.pyplot(fig)

        max_ele = np.amax(Data_Prediction)
        min_ele = np.amin(Data_Prediction)
        avg_ele = np.mean(Data_Prediction)
        
        my_array = np.array([[max_ele, min_ele, avg_ele]])
        
        df = pd.DataFrame(my_array, columns=['Max Wind Speed (m/s)', 'Min Wind Speed (m/s)', 'Average Wind Speed (m/s)'])
        
        st.write('Statistic Information')
        st.write(df)

        pro = 1.2
        A = 2
        p = []

        for i in [30]:
            p[0:i] = 0.5*pro*A*(Data_Prediction[0:i]**3)
        
        fig, ax = plt.subplots()
        plt.plot(p)
        plt.title('Power Conversion')
        plt.xlabel("Day")
        plt.ylabel("Power (watt)")
        plt.show()
        st.pyplot(fig)

        max = np.amax(p)
        min = np.amin(p)
        avg = np.mean(p)
        
        my_array = np.array([[max, min, avg]])
        
        df = pd.DataFrame(my_array, columns=['Max Power (watt)', 'Min Power (watt)', 'Average Power (watt)'])
        
        st.write('Statistic Information')
        st.write(df)

st.sidebar.markdown(
    """
    **Informasi Kontak**\n
    **Telepon       : +628-9560-6415-240**\n
    **Instagram     : enzone_id**\n
    **Email         : support.id@enzone.com**\n


    Hak Cipta © 2023 EnZone: Energy PLTB Potential Zone Application
    """
)

button_style = """
    <style>
        .stButton>button {
            background-color: #00BF63;
            color: white;
        }
    </style>
"""

st.markdown(button_style, unsafe_allow_html=True)
