import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv("restaurant_feedback.csv")

st.title("Restaurant Feedback Dashboard")

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# General Info
st.subheader("Basic Statistics")
st.write(df.describe())

# Gender Distribution
st.subheader("Gender Distribution")
st.bar_chart(df['Gender'].value_counts())

# Age Distribution
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Age'], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# Ratings Overview
st.subheader("Average Ratings")
st.write(df[['Food_Rating', 'Service_Rating', 'Ambience_Rating']].mean())

# Recommendation vs Ratings
st.subheader("Impact of Ratings on Recommendation")
fig, ax = plt.subplots()
sns.boxplot(x='Will_Recommend', y='Food_Rating', data=df, ax=ax)
st.pyplot(fig)

# Optional: Feedback Comments Word Cloud
# st.subheader("Feedback Word Cloud")
# [Add code for wordcloud if text is available]

# Filter-based View
st.subheader("Filter by Gender")
gender_filter = st.selectbox("Select Gender", options=df['Gender'].unique())
st.dataframe(df[df['Gender'] == gender_filter])
