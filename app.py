import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Social Media Sentiment Analyzer", page_icon="💬", layout="wide")
st.title("💬 Social Media Sentiment Analyzer")
st.write("A beginner-friendly demo using NLP, TF-IDF, and Logistic Regression.")

DATA_FILE = Path(__file__).parent / "sample_sentiment_data.csv"

@st.cache_resource
def train_model():
    data = pd.read_csv(DATA_FILE)
    model = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42))
    ])
    model.fit(data["text"], data["sentiment"])
    return model, data

model, data = train_model()

st.info(
    f"Demo model trained on {len(data)} short example sentences included with this project. "
    "This small teaching dataset is only for demonstrating the workflow; it is not a research-grade dataset."
)

tab1, tab2, tab3 = st.tabs(["🔎 Analyse a post", "📊 Dataset overview", "🧪 Model demo evaluation"])

with tab1:
    post = st.text_area("Enter a social-media post or comment:", 
                        placeholder="Example: This phone is amazing!")
    if st.button("Analyse sentiment", type="primary"):
        if post.strip():
            prediction = model.predict([post])[0]
            emoji = {"positive": "😊", "negative": "😟", "neutral": "😐"}.get(prediction, "💬")
            st.subheader(f"Predicted sentiment: {emoji} {prediction.title()}")
            st.caption("This is a model prediction, not a guaranteed understanding of the author's feelings.")
        else:
            st.warning("Please type a sentence first.")

with tab2:
    counts = data["sentiment"].value_counts().reindex(["positive", "negative", "neutral"], fill_value=0)
    left, right = st.columns(2)
    with left:
        st.subheader("Examples by sentiment")
        st.bar_chart(counts)
    with right:
        st.subheader("Sample rows")
        st.dataframe(data.sample(min(10, len(data)), random_state=3), use_container_width=True)
    st.caption("The chart describes the included teaching dataset, not real-time social-media opinion.")

with tab3:
    st.write("For an educational demonstration only, this evaluation uses a random holdout split of the small sample dataset.")
    if st.button("Run holdout evaluation"):
        X_train, X_test, y_train, y_test = train_test_split(
            data["text"], data["sentiment"], test_size=0.25, random_state=42, stratify=data["sentiment"]
        )
        eval_model = Pipeline([
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42))
        ])
        eval_model.fit(X_train, y_train)
        y_pred = eval_model.predict(X_test)
        st.metric("Holdout accuracy (small demo dataset)", f"{accuracy_score(y_test, y_pred):.1%}")
        st.text("Classification report:")
        st.code(classification_report(y_test, y_pred, zero_division=0))
        labels = ["positive", "negative", "neutral"]
        cm = confusion_matrix(y_test, y_pred, labels=labels)
        fig, ax = plt.subplots()
        ax.imshow(cm)
        ax.set_xticks(range(3), labels=labels, rotation=25)
        ax.set_yticks(range(3), labels=labels)
        ax.set_xlabel("Predicted label")
        ax.set_ylabel("True label")
        ax.set_title("Confusion matrix")
        for i in range(3):
            for j in range(3):
                ax.text(j, i, cm[i, j], ha="center", va="center")
        st.pyplot(fig)
        st.warning("Do not use this small demo score as a research result. For the paper, evaluate a suitable larger labelled dataset.")

st.divider()
st.caption("Project flow: labelled text → NLP text features (TF-IDF) → ML classifier → sentiment prediction → analytics.")
