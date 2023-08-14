import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 15, 13, 17]
}
df = pd.DataFrame(data)

# Set a title
st.title('Interactive Data Exploration with Streamlit')

# Show the DataFrame
st.write('Sample Data:')
st.write(df)

# Interactive chart using Seaborn
st.write('Interactive Chart:')
chart_type = st.selectbox('Select chart type', ['Line', 'Bar'])
if chart_type == 'Line':
    plt.figure()
    sns.lineplot(data=df, x='x', y='y')
    st.pyplot()
else:
    plt.figure()
    sns.barplot(data=df, x='x', y='y')
    st.pyplot()
