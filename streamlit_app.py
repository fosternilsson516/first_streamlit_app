import streamlit as stl


stl.title("Breakfast")
stl.text('🥣omega 3 & blueberry oatmeal')
stl.text('🥬kale spinnach & rocket smoothie')
stl.text('🍳hardboiled free range eggs')
stl.text('🥑avocado toast')
stl.header('🍓🫐build your own fruit smoothie🍌🍒')

import pandas as pd
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'
stl.dataframe(my_fruit_list)
