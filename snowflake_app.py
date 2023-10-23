import streamlit
import pandas
import snowflake.connector

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('1')
streamlit.text('2')
streamlit.text('3')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('From Streamlit')")
my_data_row = my_cur.fetchone()
streamlit.text("Fruit List from Snowflake:")
streamlit.text(my_data_row)
