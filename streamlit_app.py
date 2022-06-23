 
import pandas as pd
import streamlit
import requests
import snowflake.connector
from urllib.error import URLError


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
try:fruit_choice = streamlit.text_input('what fruit would you like information about?')
if not fruit_choice
streamlit.error("please select a fruit to get information")
else
fruityvice_response = requests.get("http://fruityvice.com/api/fruit/watermelon")
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

except url as e:
 streamlit.error()

streamlit.write('The user entered', fruit_choice)

streamlit.stop

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains")
streamlit.dataframe(my_data_rows)

add_fruit = streamlit.text_input('What fruit would you like to add')
streamlit.write('Thank you for adding', add_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")

