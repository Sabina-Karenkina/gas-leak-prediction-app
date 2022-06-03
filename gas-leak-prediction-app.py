import streamlit as st
import base64
import sklearn
import numpy as np
import pickle as pkl
#Load the saved model
model=pkl.load(open("final_model.p","rb"))

st.set_page_config(page_title="Gas Leak Prediction App",page_icon="⛽️",layout="centered",initial_sidebar_state="expanded")

def preprocess(Km,press_start,press_end,temp_start,temp_end,diameter,gas_consum_start,
               gas_consum_end,Davlenie_proektnoe):   
 
    
    # Pre-processing user input   
    if Km=='МГ "Макат-Северный Кавказ" ':
        Km=371.8
    elif Km=='Основная нитка. МГ ГШ':
        Km=309.0
    elif Km=='Основная нитка. МГ Жанажол - КС13':
        Km=157.4
    elif Km=='САЦ-4':
        Km=823.0
    elif Km=='МГ "САЦ-5" ':
        Km=823.0
    elif Km=='Основная нитка. МГ Союз':
        Km=382.0
    elif Km=='1 нитка. БГР-ТБА':
        Km=954.0
    elif Km=='2 нитка. БГР-ТБА':
        Km=954.0
    elif Km=='1 нитка. Бухара - Урал':
        Km=989.7
    elif Km=='2 нитка. Бухара - Урал':
        Km=989.7
    elif Km=='3 нитка. Бухара - Урал':
        Km=989.7
    
    
    if diameter == 'МГ "Макат-Северный Кавказ" - (1420)':
        diameter=1420
    elif diameter=='Основная нитка. МГ ГШ - (1220)':
        diameter=1220
    elif diameter=='Основная нитка. МГ Жанажол-КС13 - (813)':
        diameter=813
    elif diameter=='САЦ-4 - (1420)':
        diameter=1420
    elif diameter=='МГ "САЦ-5" - (1220)':
        diameter=1220
    elif diameter=='Основная нитка. МГ Союз - (1420)':
        diameter=1420
    elif diameter=='1 нитка. БГР-ТБА - (720)':
        diameter=720
    elif diameter=='2 нитка. БГР-ТБА - (1020)':
        diameter=1020
    elif diameter=='1 нитка. Бухара - Урал - (1020)':
        diameter=1020
    elif diameter=='2 нитка. Бухара - Урал - (1020)':
        diameter=1020
    elif diameter=='3 нитка. Бухара - Урал - (1020)':
        diameter=1020



    user_input=[Km,press_start,press_end,temp_start,temp_end,diameter,gas_consum_start,gas_consum_end,Davlenie_proektnoe]
    user_input=np.array(user_input)
    user_input=user_input.reshape(1,-1)
    prediction = model.predict(user_input)

    return prediction

    

       
    # front end elements of the web page 
html_temp = """ 
    <div style ="background-color:MediumAquamarine;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Gas Leak Prediction app</h1> 
    </div> 
    """
      
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Sabina & Zhanna')

# following lines create boxes in which user can enter data required to make prediction
Km=st.selectbox ("Name of the Pipeline",('МГ "Макат-Северный Кавказ','Основная нитка. МГ ГШ','Основная нитка. МГ Жанажол - КС1',
                                    'САЦ-4','МГ "САЦ-5" ','Основная нитка. МГ Союз','1 нитка. БГР-ТБА','2 нитка. БГР-ТБА',
                                     '1 нитка. Бухара - Урал','2 нитка. Бухара - Урал','3 нитка. Бухара - Урал'))
press_start=st.number_input('Pressure start value(kgf/cm2)',min_value=0, max_value=80)
press_end=st.number_input('Pressure end value(kgf/cm2)',min_value=0, max_value=80)
temp_start=st.number_input('Temperature start value',min_value=0, max_value=100)
temp_end=st.number_input('Temperature end value',min_value=0, max_value=100)
diameter=st.selectbox ("Name of the Pipeline",('МГ "Макат-Северный Кавказ" - (1420)','Основная нитка. МГ ГШ - (1220)',
                                               'Основная нитка. МГ Жанажол-КС13 - (813)','САЦ-4 - (1420)','МГ "САЦ-5" - (1220)',
                                               'Основная нитка. МГ Союз - (1420)','1 нитка. БГР-ТБА - (720)',
                                               '2 нитка. БГР-ТБА - (1020)','1 нитка. Бухара - Урал - (1020)',
                                               '2 нитка. Бухара - Урал - (1020)','3 нитка. Бухара - Урал - (1020)'))
gas_consum_start=st.number_input('Gas consumption start value',min_value=0, max_value=50)
gas_consum_end=st.number_input('Gas consumption end value',min_value=0, max_value=50)
Davlenie_proektnoe=st.number_input('Projected pressure value')



#user_input=preprocess(...)
pred=preprocess(Km,press_start,press_end,temp_start,temp_end,diameter,gas_consum_start,gas_consum_end,Davlenie_proektnoe)




if st.button("Predict"):    
    if pred[0] == 0:
        st.error('No gas leak detected at choosen pipeline')
    else:
        st.text_area('Gas leak detected at',pred[0])
    
   



 st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps you to find out whether there's a gas leak detected in pipeline or not")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether gas leak is detected at pipeline")


feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
    st.header("Thank you for rating the app!")

