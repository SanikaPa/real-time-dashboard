import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("restaurant_feedback.csv")

st.set_page_config(page_title="Restaurant Feedback Dashboard", layout="wide")
st.title("📊 Restaurant Feedback Dashboard")

# --- Basic Info ---
st.sidebar.header("Filter Options")
if 'Gender' in df.columns:
    gender_filter = st.sidebar.multiselect("Select Gender", options=df['Gender'].dropna().unique(), default=df['Gender'].unique())
    df = df[df['Gender'].isin(gender_filter)]

# Dataset preview
st.subheader("👀 Dataset Preview")
st.dataframe(df.head())

# --- Demographics Section ---
st.markdown("## 👤 Customer Demographics")

col1, col2 = st.columns(2)

with col1:
    if 'Gender' in df.columns:
        st.markdown("### Gender Distribution")
        st.bar_chart(df['Gender'].value_counts())

with col2:
    if 'Age' in df.columns:
        st.markdown("### Age Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['Age'].dropna(), bins=10, kde=True, ax=ax)
        st.pyplot(fig)

# --- Ratings Overview ---
st.markdown("## ⭐ Ratings Overview")
rating_cols = ['Food_Rating', 'Service_Rating', 'Ambience_Rating']
if all(col in df.columns for col in rating_cols):
    st.write("### Average Ratings")
    st.write(df[rating_cols].mean().round(2))

    st.write("### Rating Distributions")
    fig, ax = plt.subplots(1, 3, figsize=(18, 4))
    for i, col in enumerate(rating_cols):
        sns.histplot(df[col].dropna(), bins=5, ax=ax[i])
        ax[i].set_title(col)
    st.pyplot(fig)

# --- Recommendation Impact ---
if 'Will_Recommend' in df.columns:
    st.markdown("## 👍 Recommendation vs Ratings")
    for col in rating_cols:
        if col in df.columns:
            st.write(f"### {col} vs Willingness to Recommend")
            fig, ax = plt.subplots()
            sns.boxplot(x='Will_Recommend', y=col, data=df, ax=ax)
            st.pyplot(fig)

# --- Insights ---
st.markdown("## 📌 Business Insights")
st.markdown("""
- 👩‍🍳 **Focus on Ratings:** Customers who give high *Food* and *Service* ratings are more likely to recommend. Consider improving areas with lower scores.
- 🧑‍🤝‍🧑 **Target Demographics:** If one gender/age group dominates, explore personalized marketing.
- 📢 **Recommendation = Growth:** Encourage promoters to share positive experiences online.
- 📬 **Collect More Feedback:** Add optional questions like “What did you like most?” or “Any suggestions?”
""")
