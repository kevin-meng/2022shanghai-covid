# -*- coding:utf-8 -*-
# 疫情终将过去, 让我们共同守"沪"，上海加油!!!
import time
import streamlit as st
import pickle
import json
from PIL import Image
from streamlit_option_menu import option_menu
from apps import search, view, info, love 
from utils import load_pickle
from config import MODE,mobile_params,pc_params


if MODE == 'mobile':
    params = mobile_params
else:
    params = pc_params
    
# 导航是否使用 icon
use_icon = params[4]
use_icon = True

st.set_page_config(page_title="共同守沪", page_icon="💗", layout="centered")

image = Image.open("./files/banner-2.png")
st.image(image,caption="",use_column_width='always')  

st.markdown("""
<script>
document.write('<script src="//sharebutton.net/plugin/sharebutton.php?type=vertical&u=' + encodeURIComponent(document.location.href) + '"></scr' + 'ipt>');
</script>
""",unsafe_allow_html=True)


apps = [
    
    {"func": info.app, "title": "便民信息", "icon": "list-task"},
    {"func": love.app, "title": "温暖瞬间", "icon": "sun"},
    {"func": search.app, "title": "社区情况", "icon": "house"},
    {"func": view.app, "title": "疫情走势", "icon": "map"},
]

titles = [app["title"] for app in apps]

if use_icon :
    icons = [app["icon"] for app in apps]
else:
    icons = ['empty' for app in apps]  # 仅占位

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles.index(params["page"][0].lower()))
else:
    default_index = 0
    
selected = option_menu(
            None,  #　 "Main Menu",
            options=titles,
            icons=icons,
            menu_icon="cast",
            default_index=default_index,
            orientation="horizontal",
            styles={# "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"font-size": "14px", "margin":"0px",},  # "color": "orange", 
                    "nav-link": {"font-size": "14px", "text-align": "center", "margin":"0px",
                                 "padding":"10px 0px 10px 0px", },  # "--hover-color": "#eee"
                    # "nav-link-selected": {"background-color": "green"},
                    }
        )



for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
    
