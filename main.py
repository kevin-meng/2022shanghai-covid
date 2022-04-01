# -*- coding:utf-8 -*-
# 疫情终将过去, 让我们共同守"沪"，上海加油!!!
import streamlit as st
import pickle
import json
from PIL import Image
from streamlit_option_menu import option_menu
from apps import search, view, info 
from utils import load_pickle



st.set_page_config(page_title="上海疫情情况查询", page_icon="🩺", layout="centered")

image = Image.open("./files/bannar.png")
st.image(image,caption="")  


apps = [
    {"func": search.app, "title": "社区查询", "icon": "house"},
    {"func": view.app, "title": "疫情走势", "icon": "map"},
    {"func": info.app, "title": "便民信息", "icon": "list-task"},
]

titles = [app["title"] for app in apps]
icons = [app["icon"] for app in apps]

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
            orientation="horizontal"
        )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
    
