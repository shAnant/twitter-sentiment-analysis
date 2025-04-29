import streamlit as st
import pickle

model = pickle.load(open('https://github.com/shAnant/twitter-sentiment-analysis/blob/921cea42f6daecb3839a9dd1ef92aee1ae955a04/finalized_model%20(1).sav', 'rb'))
vectorizer = pickle.load(open('https://github.com/shAnant/twitter-sentiment-analysis/blob/c63ffff1be578ff6a0f73c612c4ca1d84dadde04/vectorizer.sav', 'rb'))
st.set_page_config(page_title="Twitter Sentiment Analyzer", page_icon="🐦")

st.title("🐦 Twitter Sentiment Analyzer")
st.write("Enter a tweet below to predict if it's **Positive** or **Negative**.")

tweet = st.text_area("Enter Tweet", height=150)

if st.button("Predict Sentiment"):
    if tweet.strip() == "":
        st.warning("Please enter some text!")
    else:
        vectorized_text = vectorizer.transform([tweet])
        prediction = model.predict(vectorized_text)[0]
        if prediction == 0 or prediction.lower() == 'negative':
            st.error("🔻 Negative Sentiment")            
        elif prediction.lower() == 'neutral':
            st.success("Neutral Sentiment")
        elif prediction.lower() == 'positive':
            st.success("🔺 Positive Sentiment")
        else:
           st.error("Irrelevant sentiment")

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
