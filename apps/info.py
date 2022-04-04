# -*- coding:utf-8 -*-
import streamlit as st
import time
from PIL import Image
from content import (dists,
                     phone_note,
                     suggest_note,
                     help_info_summary,
                     questions_v1, 
                     questions_v2, 
                     gov_help_info_dict,
                    )

def app():
    """
    便民信息汇总
    """
    st.info("""
            **恐惧源于未知.  相信科学! 拒绝谣言!**
            
            **疫情并不可怕, 恐慌没有必要.**
             """)
    
    
    st.write("### 💡常见问题解惑")
    st.write("##### 1.检测预防类")
    expanders1 = {}
    for i,data in enumerate(questions_v1):
        expanders1[i] = st.expander(data['question'])
        expanders1[i].markdown(data['answer'])
        if 'image' in data.keys():
            for img in data['image']:
                img = Image.open(img)
                expanders1[i].image(img)
        expanders1[i].info(data['note'])                   
    st.write("---")
    
    st.write("##### 2.密接感染类")
    expanders2 = {}
    for i,data in enumerate(questions_v2):
        expanders2[i] = st.expander(data['question'])
        expanders2[i].markdown(data['answer'])
        if 'image' in data.keys():
            for img in data['image']:
                img = Image.open(img)
                expanders2[i].image(img)
        expanders2[i].info(data['note'])                        
    
    st.write("---")

    ##############################################################
    st.write("### 💡上海各区保障信息汇总")
    
    st.info(help_info_summary)
    
    # 选择小区
    st.write("**选择地区**")
    dist = st.selectbox('', dists,index = 0)
    
    data = gov_help_info_dict[dist] 
    expander1 = st.expander("保障热线电话")
    expander1.write(data['phone_content'])
    for img in data['phone_imgs']:
        img_p1 = Image.open(img)
        expander1.image(img_p1,caption="")
    expander1.info(phone_note)
    
    # st.write("---")
    expander2 = st.expander("问题\建议征集平台")
    img_s1 = Image.open(data['suggest_imgs'][0])
    expander2.image(img_s1,caption="")
    expander2.info(suggest_note)

    
    