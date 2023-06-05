import pickle
import streamlit as st

model = pickle.load(open('kisaran_harga_mobil.sav', 'rb'))

st.title('estimasi harga mobil bekas')

year = st.number_input('input tahun mobil')
milleage =st.number_input('input KM mobil')
tax =st.number_input('input pajak mobil')
mpg =st.number_input('input konsumsi bensin mobil')
enggineSize =st.number_input('input enigne size mobil')

predict =''

if st.button('munculkan estimasi harga'):
    predict = model.predict(
        [[year, milleage, tax, mpg, enggineSize]]
    )
    st.write ('harga mobil bekas dalam pond : ', predict)
    st.write ('harga mobil bekas dalam rupiah : ', predict)