#from dotenv import load_dotenv
import getpass
import os
# import streamlit as st
import time

#load_dotenv(override=True) 

# print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
# print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

# Complete방식
# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("hi! today's weather")
# print(result)

# Chat 방식
# #from langchain.chat_models import ChatOpenAI   --> old
# #from langchain_community.chat_models import ChatOpenAI   -old
# from langchain_openai import ChatOpenAI
# chat_model = ChatOpenAI()
# #result = chat_model.predict("hi! today's weather")   --> old
# result = chat_model.invoke("hi! today's weather")

# Chat 방식
#from langchain_openai import ChatOpenAI
#from langchain.chat_models import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.globals import set_verbose
set_verbose(True)

chat_model = ChatOpenAI()

content = "코딩"
#result = chat_model.invoke(content + "에 대해 시를 써줘")

#print(result.content)

import streamlit as st

st.title("인공지능 시인")
content = st.text_input("시의 주제를 제세해주세요!")

if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중"):
        result = chat_model.invoke(content + "에 대해 시를 써줘")
#        result = chat_model.predict(content + "에 대해 시를 써줘")        
        st.write(result.content)


