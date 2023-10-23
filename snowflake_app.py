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

def get_fruityvise_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized =  pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit choice")
def get_fruit_list():
  with my_cnx.cursor() as my_cur:
       my_cur.execute("select * from fruit_load_list")
       return my_cur.fetchall()

if streamlit.button('Get Fruit list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_list()
  streamlit.dataframe(my_data_rows)

