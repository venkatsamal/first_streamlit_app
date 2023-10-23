import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('1')
streamlit.text('2')
streamlit.text('3')

streamlit.header("Fruityvice Fruit choice")
def get_fruit_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()

if streamlit.button('Get Fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_list()
  streamlit.dataframe(my_data_rows)

def insert_row(new_fruit):
  with my_cnx.cursor() as my_curi:
       my_curi.execute("insert into fruit_load_list values ('from streamlit')")
       return 'New record Added' + new_fruit

add_my_fruit = streamlit.text_input('Please add fruit here')
if streamlit.button('Add Fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row(add_my_fruit)
  streamlit.text(back_from_function)
