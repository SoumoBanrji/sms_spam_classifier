import pickle
import streamlit as st
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer



ps = PorterStemmer()


def transform_text(text):
    '''prepocessing the input text'''
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
            
    return " ".join(y)


with open('vectorizer.pkl','rb') as f:
    tfidf = pickle.load(f)

with open('model.pkl','rb') as f:
    model = pickle.load(f)


st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    # a. prepocessing
    transform_sms = transform_text(input_sms)
    # b. vectorizing
    vector_input = tfidf.transform([transform_sms])
    # c. predicting
    result = model.predict(vector_input)[0]
    # d. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

