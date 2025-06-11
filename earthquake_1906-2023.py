import streamlit as st
import pandas as pd
import plotly.express as px

def home(dataframe):
    st.markdown("### :round_pushpin: Data")
    st.write(df)

def stats(dataframe):
    st.markdown("### :round_pushpin: Data statistics")
    st.write(dataframe.describe())

def header(dataframe):
    st.markdown("### :round_pushpin: Data header")
    st.write(df.head())

def plot(dataframe):
    st.markdown("### :round_pushpin: Interactive plots")
    x_axis=st.selectbox("select X-axis value", options=df.columns)
    y_axis=st.selectbox("select Y-axis value", options=df.columns)
    col=st.color_picker("Select a color for plot")
    sc_plot=px.scatter(dataframe, x=x_axis, y=y_axis)
    sc_plot.update_traces(marker=dict(color=col))
    st.plotly_chart(sc_plot, use_container_width=True)

def global_distribution(self):
    st.markdown("### :round_pushpin: Global earthquake distribution.")
    st.text("Place your cursor to get details of the magnitude for repsective points")
    col=st.color_picker("Select a color for plot")
    fig=px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="mag", zoom=1)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_traces(marker=dict(color=col))
    st.plotly_chart(fig, use_container_width=True)

 
st.title(":point_right: Global earthquake EDA 1906-2023")

upload_file=st.sidebar.file_uploader("Upload file", type=["csv", "txt", "xlsx", "xls"])
options=st.sidebar.radio("Pages", options=["Home", "Data statistics", "Data header", "Interactive plots", "Map view"])
if upload_file:
    df=pd.read_csv(upload_file)
try:
    if options=="Home":
        st.markdown("### This is a web app to explore earthquake data")
        home(df)
    elif options=="Data statistics":
        stats(df)
    elif options=="Data header":
        header(df)
    elif options=="Interactive plots":
        plot(df)
    elif options=="Map view":
        global_distribution(df)
        
except: st.markdown("## Upload global eathquake data")

    


