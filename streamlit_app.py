 
import pandas as pd
import streamlit


streamlit.title("Breakfast")
streamlit.text('🥣omega 3 & blueberry oatmeal')
streamlit.text('🥬kale spinnach & rocket smoothie')
streamlit.text('🍳hardboiled free range eggs')
streamlit.text('🥑avocado toast')
streamlit.header('🍓🫐build your own fruit smoothie🍌🍒')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#added pick list, so customers can pick from a list
fruits_selected = streamlit.multiselect("pick some fruits:" , list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#displays data on page
streamlit.dataframe(fruits_to_show) 

streamlit.header('fruityvice fruit advice')
fruit_choice = streamlit.text_input('what fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
import requests

fruityvice_response = requests.get("http://fruityvice.com/api/fruit/watermelon")

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)



