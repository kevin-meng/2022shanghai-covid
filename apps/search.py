import pickle
import jinja2
import json
import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
from PIL import Image
import streamlit.components.v1 as components
import plotly.graph_objects as go
from utils import load_pickle,distinct
from visual import add_point,plot_maker,plot_map
from config import MODE, mobile_params,pc_params
from content import info_data,info_contact
from database import eare_ls,latest_date,date_range,dist_info

@st.cache(ttl=3*60*60) # persist=True
def load_data():
    data = load_pickle("./data/df_address_week.pkl")
    # print(data.shape)  # 必须
    return data 


def app():
    """
    查询被感染社区信息,以及周边情况.
    """

    # ###################################################################
    if MODE == 'mobile':
        params = mobile_params
    else:
        params = pc_params
    map_width, map_height, graph_width, graph_height, use_icon = params
    
    
    st.write("## 疫情信息查询")
    
    st.info("""
            **恐惧源于未知.  相信科学! 拒绝谣言!**
            
            **知道的越多,恐惧的越少**
            
            **疫情并不可怕, 恐慌没有必要.**
            
            这里有一份覆盖疫情检测\治疗\买菜\买药看病等各方面的笔记:
            **[疫情期间生活指南](https://www.wolai.com/6TLbKJYT1JTq3cFqXTWVXC)**
            希望对你有帮助.
             """)
    
    
    st.write('---')
    st.write("### 社区感染情况")
    st.info(f"""
    - 数据最新日期:{latest_date}
    - 目前仅支持已被通报的社区查询.
    """)

    st.write("**输入关键字搜索**")


    # 选择小区
    target_area = st.selectbox('', eare_ls+[""],index = len(eare_ls))
    
    
    if target_area in eare_ls:


        # 选择小区的位置
        target_long = dist_info.get(target_area,dict()).get('longitude',0)
        target_lat = dist_info.get(target_area,dict()).get('latitude',0)
        target_date_ls = dist_info.get(target_area,dict()).get('日期',[])
        
        # 载入数据
        data = load_data() 
        # print(data.shape)
        # print("data init shape:",data[data['日期']=='2022-04-06'].shape)
        # data_target = data[data['详细地址']==target_area].sort_values('日期')[['详细地址','日期']].reset_index(drop=True)
        data_target = pd.DataFrame(data = target_date_ls,columns=['日期']).sort_values('日期')
        data_target['社区'] = target_area
        
        st.empty()
        st.write("**从3月1日至今的疫情通报记录:**")
        if len(data_target)==0:
            st.write("这段时间内,未查询到该小区的疫情通报信息. 请进一步核实.")
        else:
            st.table(data_target)

        st.write("### 小区周边疫情情况:")
        st.write("*默认显示周边**3公里**信息")
        # 获取小区经纬度
        st.empty()
        st.write("**选择查询日期范围**")
        date_lower, date_upper = st.select_slider(
             '',
             options=date_range[-3:],
             value=(date_range[-2], date_range[-1]))
        
        data_sub = data[(data['日期']>=date_lower)&(data['日期']<=date_upper)&\
                         (data['longitude']>=(target_long-0.035))&(data['longitude']<=(target_long+0.035))&\
                         (data['latitude']>=(target_lat-0.035))&(data['latitude']<=(target_lat+0.035))]
        df_sub = data_sub.groupby('详细地址').agg({'longitude':max,'latitude':max,'日期':distinct}).reset_index()
        # print(date_lower, date_upper)
        # print(data_sub[data_sub['日期']==date_upper].shape)
        # print(df_sub[df_sub['详细地址']==target_area])
        st.write("")
        sh_sub_map= plot_map(add_point(df_sub,ratio=2,color_index=1),
                         center=(target_lat,target_long),
                         zoom_start=13,fig_type=1)
        marker = plot_maker(target_lat,target_long,target_area)
        marker.add_to(sh_sub_map)
        folium_static(sh_sub_map,width=map_width,height=map_height)   

    st.write('---')

    # 项目说明
    expander = st.expander("数据说明")
    expander.write(info_data)

    expander = st.expander("联系方式")
    expander.write(info_contact)
