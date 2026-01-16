from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import streamlit as st
import os

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize OPEN AI's openai_model
openai_model = ChatOpenAI(model = "gpt-5-mini")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | openai_model


st.header("Tweet Generator - RAGHAVA")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic})
    st.write(tweets.content)
    
