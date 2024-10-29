'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("AI大模型应用产品网")
col, col1 = st.columns(2)
with col:
    st.image("https://ww3.sinaimg.cn/mw690/7efc371bgy1hq5k7d28j5j20wh0vqad9.jpg", use_column_width=True)
    flag = st.button("lt绘言", use_container_width=True)
    if flag:
        st.switch_page("pages/demo1.py")
with col1:
    st.image("https://ww3.sinaimg.cn/mw690/7efc371bgy1hq5k7d28j5j20wh0vqad9.jpg", use_column_width=True)
    flag = st.button("lt绘图", use_container_width=True)
    if flag:
        st.switch_page("pages/testToImage.py")


c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    flag = st.button("基础版")
    if flag:
        st.switch_page("pages/demo.py")

with c2:
    flag1 = st.button("进阶版1")
    if flag1:
        st.switch_page("pages/demo1.py")

with c3:
    flag2 = st.button("进阶版2")
    if flag2:
        st.switch_page("pages/demo2.py")

with c4:
    flag3 = st.button("最终版")
    if flag3:
        st.switch_page("pages/demo3.py")
with c5:
    flag4 = st.button("文本图片")
    if flag4:
        st.switch_page("pages/testToImage.py")
