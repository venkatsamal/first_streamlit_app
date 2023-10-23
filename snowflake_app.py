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
fruit_choice = streamlit.text_input('What fruit')
streamlit.write('user entered', fruit_choice) 


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("Fruit List from Snowflake:")
streamlit.dataframe(my_data_row)

streamlit.stop()
