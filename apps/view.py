import streamlit as st
import json
from PIL import Image
import streamlit.components.v1 as components
import plotly.graph_objects as go

from visual import plot_summary
from utils import load_pickle
from config import info_data,info_contact,mobile_params,pc_params



@st.cache(ttl=3*60*60) # persist=True
def load_summary():
    df_summary = load_pickle("./data/df_summary.pkl")
    return df_summary



def app():
    # 载入数据
    df_summary = load_summary()
    map_width,map_height,graph_width,graph_height = mobile_params
    map_width,map_height,graph_width,graph_height = pc_params    
    
    st.write("## 上海疫情实时动态") 
    st.write("---")
    st.write("### 疫情走势")
    

    
    fig = plot_summary(df_summary,graph_width,graph_height)
    st.plotly_chart(fig)

    st.write("---")
    st.write("### 疫情位置分布")
    st.info("""
            - 展示过去7天，上海感染社区分布.
            - 点击标记点，可查看对应社区名称.
            """)

    HtmlFile = open("./files/latest_week.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    # print(source_code)
    components.html(source_code,width=map_width,height=map_height)

    st.write("---")
    # 项目说明
    expander = st.expander("数据说明")
    expander.write(info_data)

    expander = st.expander("联系方式")
    expander.write(info_contact)