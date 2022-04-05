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
            
            **知道的越多,恐惧的越少**
            
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
    st.write("##### 3. 感染者经历分享")
    st.info("""
        如果被通知核酸异常或者抗原检测阳性时,一定不要慌张. 下面这位无症状感染者申先生的经历和他总结的自助手册也许对你有所帮助.
        
    """)
    expander4 = st.expander("申先生的经历")
    expander4.write("""
    [我是一名无症状感染者，我的经历也许能帮到很多人](https://mp.weixin.qq.com/s/Tt3xro5pKYvm7PmnEf7xuw)
    
    [核酸检测异常自助手册](https://mp.weixin.qq.com/s/op7_2tXYfOTr1Td4YPoA2Q)
    """)

    st.write("---")
    
    ##############################################################    
    st.write("### 💡上海疫情期间买菜指南")
    st.info("""
        汇总各大平台及时买菜信息,更新4月1日版,欢迎进去进一步更新补充.
    """)
    expander0 = st.expander("买菜指南")
    expander0.write("""[完整页面跳转](https://www.wolai.com/6TLbKJYT1JTq3cFqXTWVXC)""")
    img = Image.open("./files/vegetable.png")
    expander0.image(img)
    st.write("---")
    ##############################################################    
    st.write("### 💡 医院停开诊情况查询")
    st.info("""
        本市部分医疗机构因配合疫情协查工作,暂停部分医疗服务. 就诊前建议先查询.
    """)
    expander0 = st.expander("当日医院情况查询")
    expander0.write("""微信小程序-随申办""")
    img = Image.open("./files/hospital.png")
    expander0.image(img)
    st.write("---")
    ##############################################################
    st.write("### 💡上海各区保障电话信息汇总")
    
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

    
    