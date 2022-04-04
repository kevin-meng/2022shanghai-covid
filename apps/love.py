import streamlit as st
import random
from PIL import Image
from content import warmly_moments_list


def app():
    """
    汇集温暖瞬间
    """

    ##############################################################
    st.write("## 💝汇聚温心瞬间")
    
    st.info("""
             **人与人之间互传播的还有温暖和感动.**
             
             感谢疫情以来, 每一位奋战在一线的平凡而伟大的工作人员、志愿者们. 你们辛苦了!
             
             疫情阶段很多感动的瞬间, 值得被传递. 让我们多些理解,多方配合,相信疫情很快就会过去.
             
             """)
    st.write(".")
    select_data = random.sample(warmly_moments_list, 10)
    
    
    def random_sample_list(num=10):
        global select_data
        select_data = random.sample(warmly_moments_list, num) 

    st.error(f"**累计收集: {len(warmly_moments_list)} 个暖心瞬间❤️.**")

    st.write('---')
    st.write("*随机呈现10个瞬间")
    st.button("换一组",key=0,on_click=random_sample_list)
    
    st.empty()
    for data in select_data:
        with st.container():
            img = Image.open(data['images'])
            st.image(img)
            # expander = st.expander(data['content'][:50])
            st.warning(data['content'])
        st.write('---')
    
    st.button("换一组",key=1,on_click=random_sample_list)    


