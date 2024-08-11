# import streamlit as st
#
# # Title and header
# st.title('Welcome to NLP Application')
# st.header('''
# A Web app with various NLP features such as:
#
#     1. Overview of NLP
#     2. Spam Classification
#     3. News Category Classification
#     4. Named Entity Recognition
#     5. QnA Systems
#     6. Text Summarization
#     7. Sentiment Analysis
# ''')
# st.markdown('---')
#
#
#
# explore = st.button("Let's Explore")
# list1 = ("What is NLP?","Sentiment Analysis","Text Summarization")
# while(explore):
#     option = st.sidebar.selectbox("How can we assist you ",list1)
#     if(option == "Sentiment Analysis"):
#
#         st.subheader("Sentiment Analysis")
#         st.textbox('Enter Your Sentiment ')
#
#     elif(option == "What is NLP?"):
#         st.image('NLP.png', caption='NLP Use Cases', width=550)
#
import streamlit as st
import pickle


model = pickle.load(open('model.pkl', 'rb'))

# Title and header
st.title('Welcome to NLP Application')
st.header('''
A Web app with various NLP features such as:

    1. Overview of NLP
    2. Spam Classification
    3. News Category Classification
    4. Named Entity Recognition
    5. QnA Systems
    6. Text Summarization
    7. Sentiment Analysis
''')
st.markdown('---')

# Sidebar selectbox for user options with unique key
options = ("What is NLP?", "Sentiment Analysis", "Text Summarization")
selected_option = st.sidebar.selectbox("How can we assist you?", options, key="main_selectbox")

if selected_option == "Sentiment Analysis":
    st.subheader("Sentiment Analysis")
    sentiment_input = st.text_area('Enter Your Sentiment:', key="sentiment_input")
    if sentiment_input:
        trans = pickle.load(open('trans.pkl','rb'))
        model = pickle.load(open('model.pkl','rb'))
        vc = pickle.load(open('vectorizer.pkl','rb'))
        sentiment_input = trans(sentiment_input)
        inp = vc.transform(sentiment_input)
        predict = st.button('Predict')
        if(predict):
            ans = model.predict(inp)

            if(ans==1):
                st.write('Positive Sentiment')
            else:
                st.write('Negative Sentiment')



elif selected_option == "What is NLP?":
    st.image('NLP.png', caption='NLP Use Cases', width=550)

elif selected_option == "Text Summarization":
    st.subheader("Text Summarization")
    text_input = st.text_area('Enter text to summarize:', key="text_area_input")
    if text_input:
        st.write(f"Text to summarize: {text_input}")

# Add additional elif blocks for other options as needed
