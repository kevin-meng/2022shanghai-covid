import streamlit as st
import json
from PIL import Image
import pandas as pd
import streamlit.components.v1 as components
import plotly.graph_objects as go
from streamlit_folium import folium_static
from visual import plot_summary,load_point2layer,plot_map
from utils import load_pickle
from config import MODE, mobile_params,pc_params
from content import info_data,info_contact
from database import df_summary


@st.cache(ttl=3*60*60) # persist=True
def load_summary():
    point_json = load_pickle("./data/last_week.pkl")
    return point_json



def app():
    
    if MODE == 'mobile':
        params = mobile_params
    else:
        params = pc_params
    
    map_width, map_height, graph_width, graph_height, use_icon = params
    
    st.write("## 上海疫情实时动态") 
    # 项目说明
    expander = st.expander("数据说明")
    expander.write(info_data)

    expander = st.expander("联系方式")
    expander.write(info_contact)
    st.write("---")
    st.write("### 疫情走势")
    

    
    fig = plot_summary(df_summary)
    st.plotly_chart(fig,use_container_width=True)
    
    st.write("---")
    st.write("### 疫情位置分布")
    st.info("""
            - 展示过去3天，上海感染社区分布.
            - 点击标记点，可查看对应社区名称.
            """)
    # 载入数据
    point_json = load_summary()
    point_layer = load_point2layer(point_json)
    sh_map = plot_map(point_layer)
    folium_static(sh_map,width=map_width,height=map_height)    

    st.write("---")

