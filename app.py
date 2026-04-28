import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler #load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
scaler =MinMaxScaler()


st.title('health insurence primimum price pridiction')

age = st.number_input('age',min_value=1,max_value=100,value =30)
gender = st.selectbox('gender',('male','female'))
bmi=st.number_input('bmi',min_value=10,max_value=50,value=20)
smoker=st.selectbox('smoker',('yes','no'))
children=st.number_input('children',min_value=0,max_value=10,value=0)
region=st.selectbox('region',('southwest','southeast','northwest','northeast'))

#logic for categorical columns
Smoker = 1 if smoker == 'yes' else 0
region_dict={'southwest':0,'southeast':3,'northwest':1,'northeast':2}
Region = region_dict[region]

sex_male= 1 if gender == 'male' else 0
sex_female = 1 if gender == 'female' else 0

#create dataframe
input_features = pd.DataFrame({
    'age': [age],
    'bmi': [bmi],
    'children': [children],
    'smoker': [Smoker],        # ✅ numeric
    'sex_female': [sex_female],
    'sex_male': [sex_male],
    'Region': [Region]         # ✅ numeric
})

#minmax scaler
input_features[['age','bmi']]=scaler.fit_transform(input_features[['age','bmi']])

#prediction
if st.button('predict'):
  predictions=model.predict(input_features)
  output = round(np.exp(predictions[0]),2)
  st.success(f'Predicted insurance premium price: ${output}')