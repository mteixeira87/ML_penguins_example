import streamlit as st
#from sklearn.metrics import accuracy_score
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import train_test_split
import pickle
rf_pickle = open('random_forest_penguin.pickle','rb')
map_pickle = open('output_penguin.pickle','rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
st.write(rfc)
st.write(unique_penguin_mapping)
