'''
文本图大模型
'''
import streamlit as st
from sqlalchemy.sql.functions import user
from zhipuai import ZhipuAI

model = ZhipuAI(api_key="b7921e19021e06404866feab60a58ebb.h7VY6bgWCfS0EUxa") # 填写您自己的APIKey
st.title("设计大师")

if "cache" not in st.session_state:
    st.session_state.cache = []
else:
    for message in st.session_state.cache:
        if message['role'] == 'user':
            with st.chat_message(message['role']):
                 st.write(message["content"])
        else:
            with st.chat_message(message['role']):
                 st.image(message["content"],width=300)
#创建一个输入框
desc = st.chat_input("请输入图片的描述")
if desc:
    #将用户输入的内容以用户角色输出到界面上
    with st.chat_message("user"):
        st.write(desc)
    st.session_state.cache.append({"role":"user","content":desc})
    #调用智谱AI的文生图大模型生成图片
    response = model.images.generations(
        model="cogview-3-plus",  #填写需要调用的模型编码
        prompt=desc,
    )
    #以AI的角色展示图片
    with st.chat_message("assistant"):
        st.image(response.data[0].url,width=300)
    st.session_state.cache.append({"role":"assistant","content":response.data[0].url})
