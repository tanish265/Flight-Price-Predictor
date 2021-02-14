print("Hello Tanish")
import numpy as np
import datetime
import streamlit as st

import pickle

html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Flight Price Predictor </h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)
st.set_option('deprecation.showfileUploaderEncoding',False)
# @st.cache(allow_output_mutation=True)

hello=open("xgb_flight2.pkl","rb")
model=pickle.load(hello)

dep_date = st.date_input('Select/Enter departure date', datetime.date(2019,1,1))
# st.write(dep_date.year)

# dep_time=st.slider('Departure time',0,23,7,step='timedelta')
dep_time=st.time_input('Departure time', datetime.time(8, 45))
arrival_date = st.date_input('Select/Enter arrival date', datetime.date(2019,1,1))
# st.write(arrival_date)

arrival_time=st.time_input('Arrival time', datetime.time(9, 45))
# st.write(arrival_time.minute)
source=st.selectbox('Source',('Banglore','Delhi','Kolkata','Mumbai','Chennai'))

destination=st.selectbox('Destination',('Cochin','Delhi','Banglore','New Delhi','Hyderabad','Kolkata'))

stops=st.selectbox('Stopage',('Non-Stop','1','2','3','4'))
if stops=='Non-Stop':
    stops='0'
    
airline=st.selectbox('Which Airline do you prefer to travel?',('Jet Airways','Indigo',
                                                               'Air India','SpiceJet',
                                                               'Multiple Carriers',
                                                               'Vistara','Air Asia',
                                                               'GoAir',
                                                               'Multiple carriers Premium economy',
                                                               'Jet Airways Business',
                                                               'Vistara Premium economy','Trujet'))
# st.write(type(dep_time))   
Journey_Day=dep_date.day
Journey_Month=dep_date.month
Dep_hour=dep_time.hour
Dep_min=dep_time.minute

Arrival_hour=arrival_time.hour
Arrival_min=arrival_time.minute

Duration_hours = abs(Arrival_hour - Dep_hour)
Duration_mins = abs(Arrival_min - Dep_min)

# st.write(type(airline))
if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
elif (airline=='Multiple Carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0


if (source == 'Delhi'):
        s_Delhi = 1
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0

elif (source == 'Kolkata'):
        s_Delhi = 0
        s_Kolkata = 1
        s_Mumbai = 0
        s_Chennai = 0

elif (source == 'Mumbai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 1
        s_Chennai = 0

elif (source == 'Chennai'):
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 1

else:
        s_Delhi = 0
        s_Kolkata = 0
        s_Mumbai = 0
        s_Chennai = 0
        
if (destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
elif (destination == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

elif (destination == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

elif (destination == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

elif (destination == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

prediction=model.predict(np.array([[
            int(stops),
            Journey_Day,
            Journey_Month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            Duration_hours,
            Duration_mins,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Trujet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi]]
        ))

output=round(prediction[0],2)

st.write('Predicted Price is >> '+ str(output))