import streamlit

streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('1')
streamlit.text('2')
streamlit.text('3')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list 
streamlit.multiselect("Pick some fruits - ", list(my_fruit_list.index))

#display the table on page
streamlit.dataframe(my_fruit_list)

