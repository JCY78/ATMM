import streamlit as st

# Set page configuration    
import os

icon_path = os.path.abspath("photos/logo.jpg")
home = st.set_page_config(page_title="Anhui Top Myanmar", page_icon=icon_path, layout="wide") 


st.title("Anhui Top Myanmar")

tab1, tab2, tab3 = st.tabs(
    ["Home", "Our Products", "Newsletter"], default="Home"
)

with tab1:
    st.header("Home")
    st.write("Anhui Top Myanmar is a leading fashion apparel company based in Myanmar. We are dedicated to providing stylish and comfortable clothing for all occasions. Our    	mission is to deliver high-quality products that meet the diverse needs of our customers while promoting sustainable and ethical fashion practice. We offer premium, 	committed to expanding globally and embracing internationalization—driven by our vision to design clothing for the world and bring people closer through fashion.")
    
with tab2:
   st.header("Our Products")    
  
with tab3:
   st.header("Newsletter")
   
