import streamlit as st
import pickle
import numpy as np
reg = pickle.load(open('reg.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
def ap(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = reg.predict(input_data_reshaped)
    return prediction
def main():
    st.title("Phone price predictor")
    ROM = st.selectbox('ROM',df['ROM'].unique())
    RAM= st.selectbox('RAM',df['RAM'].unique())
    Battery_Power= st.selectbox('Battery_Power',df['Battery_Power'].unique())
    Primary_Cam= st.selectbox('Primary_Cam',df['Primary_Cam'].unique())
    Selfi_Cam= st.selectbox('Selfi_Cam',df['Selfi_Cam'].unique())
    Mobile_Size= st.selectbox('Mobile_Size',df['Mobile_Size'].unique())

    diagnosis = ''

    # creating a button for Prediction

    if st.button('Predict price'):
        diagnosis = ap([Battery_Power, ROM, Primary_Cam, Selfi_Cam, RAM, Mobile_Size])

    st.success(diagnosis)


if __name__ == '__main__':
    main()


