import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.title("Plotting")
chart_data=pd.DataFrame(np.random.randn(20,3),columns=["line-1","line-2","line-3"])
st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)


st.header("Data visualization using matplotlib and seaborn")
st.subheader("Loading DataFrame")
df=pd.read_csv("iris.csv")
st.dataframe(df)

st.subheader("Distribution plot with matplotlib")
fig=plt.figure(figsize=(15,8))
df["species"].value_counts().plot(kind="bar")
st.pyplot(fig)

st.subheader("Distribution plot with seaborn")
fig=plt.figure(figsize=(15,8))
sns.distplot(df["sepal_length"])
st.pyplot(fig)

st.header("Multiple graphs")
st.subheader("Distribution plot with seaborn")

col1,col2 =st.columns(2)
with col1:
    col1.header="KDE=False"
    fig1=plt.figure()
    sns.distplot(df["sepal_length"],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header="Hist=False"
    fig2=plt.figure()
    sns.distplot(df["sepal_length"],hist=False)
    st.pyplot(fig2)

st.header("Changing Style")
col1,col2 =st.columns(2)
with col1:
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    col1.header="KDE=False"
    fig1=plt.figure()
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig1)
with col2:
    col2.header="Hist=False"
    sns.set_theme(context="poster",style="darkgrid")
    fig2=plt.figure()
    sns.distplot(df["petal_length"],hist=False)
    st.pyplot(fig2)

st.header("exploring diffrent graphs")
st.subheader("sactter plot")
fig,ax=plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("count plot")
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x="species")
st.pyplot(fig)

st.subheader("Box plot")
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x="species",y="petal_length")
st.pyplot(fig)


st.subheader("Violin plot")
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x="species",y="petal_length")
st.pyplot(fig)
