import streamlit as st
import json
from PIL import Image
import streamlit.components.v1 as components
import plotly.graph_objects as go
from streamlit_folium import folium_static
from visual import plot_summary,load_point2layer,plot_map
from utils import load_pickle
from config import MODE, mobile_params,pc_params
from content import info_data,info_contact



@st.cache(ttl=3*60*60) # persist=True
def load_summary():
    df_summary = load_pickle("./data/df_summary.pkl")
    point_json = load_pickle("./data/last_week.pkl")
    
    return df_summary,point_json



def app():
    # 载入数据
    df_summary,point_json = load_summary()
    
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
    point_layer = load_point2layer(point_json)
    sh_map = plot_map(point_layer)
    folium_static(sh_map,width=map_width,height=map_height)    
    # HtmlFile = open("./files/latest_week.html", 'r', encoding='utf-8')
    # source_code = HtmlFile.read() 
    # print(source_code)
    # components.html(source_code,width=map_width,height=map_height)

    st.write("---")

