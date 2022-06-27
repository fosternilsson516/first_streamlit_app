 
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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("http://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
 
streamlit.header('fruityvice fruit advice')
try:
 fruit_choice = streamlit.text_input('what fruit would you like information about?')
 if not fruit_choice:
   streamlit.error("please select a fruit to get information")
 else:
  back_from_function = get_fruityvice_data(fruit_choice)
  streamlit.dataframe(back_from_function)
  
except url as e:
 streamlit.error()

streamlit.write('The user entered', fruit_choice)

streamlit.header("The fruit list contains")
def get_fruit_load_list():
 with my_cnx.cursor() as my_cur:
  my_cur.execute("select * from fruit_load_list")
  return my_cur.fetchall()
 
 if streamlit.button('get fruit load list'):
  my_cur = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
  def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('from streamlit')")
    return "thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add')
if streamlit.button('add a fruit to the list'):
 my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
 back_from_function = insert_row_snowflake(add_my_fruit)
 streamlit.text(back_from_function)



