import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff


st.title("Working with csv file and try to visualise ")
st.header("Altair scatter plot")
chart_data=pd.DataFrame(np.random.randn(500,5),columns=["a","b","c","d","e"])
chart=alt.Chart(chart_data).mark_circle().encode(x="a",y="b",size="c",tooltip=["a","b","c","d","e"])
st.altair_chart(chart)


st.header("Interactive chart")
st.subheader("Line chart")
df=pd.read_csv("lang_data.csv")
lang_list=df.columns.tolist()
lang_choices=st.multiselect("choose your language",lang_list)
new_df=df[lang_choices]
st.line_chart(new_df)

st.subheader("Area Chart")
st.area_chart(new_df)


st.header("Data visualization with Plotly")
st.subheader("Displaying the Tips dataset")
df=pd.read_csv("tips.csv")
st.dataframe(df.head())

st.subheader("Pie Chart")
fig = px.pie(df,values="total_bill",names="day")
st.plotly_chart(fig)

st.subheader("Pie Chart with multiple parameters")
fig = px.pie(df,values="total_bill",names="day",opacity=.9)
st.plotly_chart(fig)

st.subheader("Histogram")
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)

hist_data=[x1,x2,x3]
group_labels=["G1","G2","G3"]
fig=ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)
