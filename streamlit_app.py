 
import pandas as pd

streamlit.title("Breakfast")
streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥬kale spinnach & rocket smoothie')
streamlit.text('🍳hardboiled free range eggs')
streamlit.text('🥑avocado toast')
streamlit.header('🍓🫐build your own fruit smoothie🍌🍒')

import streamlit
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('fruit')

streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index))


streamlit.dataframe(my_fruit_list)

