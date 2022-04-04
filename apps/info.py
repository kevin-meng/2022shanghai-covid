import streamlit as st
from PIL import Image


def app():
    """
    便民信息汇总
    """
    dists = ["浦东新区","黄浦区","静安区","徐汇区","长宁区","普陀区","松江区","奉贤区",
         "虹口区","杨浦区","宝山区","闵行区","嘉定区","金山区","崇明区","青浦区"] 

    ##############################################################
    st.write("## 上海各区保障信息汇总")
    
    st.info("""
             面对严峻复杂的疫情防控形势，官方在全市各区分别设立了两个平台
             -  **1. 保障热线**。

                 保障居民的基本生活需求,做到及时响应。
                 
             -  **2. 疫情防控工作问题\建议征集平台**。

                 大家可踊跃反映问题，提出意见建议，更好推进疫情防控工作。
             """)
    
    st.write("--- ")
    # 选择小区
    st.write("**选择地区**")
    dist = st.selectbox('', dists,index = 0)
    st.write("---")
    
    if dist == '浦东新区':
        # expander = st.expander("热线电话")
        # expander.write(info_data)
        
        st.write("""
        #### 热线电话
        浦东新区的居民可以通过以下渠道采购主副食品或咨询：

        1、关注各街镇官方微信公众号，将持续推送各类线上“云买菜”攻略和线下团购套餐清单。你可选择线上下单、线下配送到小区收货点，或组织社区团购，向供货商集中下单后配送至小区收货点。

        2、拨打各街镇生活保障热线，或联系村（居）委会、志愿者，我们将为你提供物资保障、信息告知等服务。
        （注：以下热线电话仅限3月28日5点至4月1日5点期间使用）
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.jpeg")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "黄浦区":
        st.write("""
        #### 热线电话
        为全力做好疫情防控工作，有效减少人员聚集，更好满足疫情期间居家生活和就医服务需求，切实保障人民群众生命安全和身体健康，现将黄浦区疫情防控期间为民服务热线电话公告如下：
        - 黄浦区24小时服务热线电话：63130821
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "静安区":
        st.write("""
        #### 热线电话
            - 区城运中心24小时服务热线电话：33094207
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "徐汇区":
        st.write("""
        #### 热线电话
        居民朋友们，为全力做好疫情防控工作，有效减少人员聚集，更好地满足疫情期间居家生活和就医服务需求，现将徐汇区疫情防控期间，为民服务热线电话公告如下：
         - 24小时服务热线电话 58910910
        """)

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "长宁区":
        st.write("""
        #### 热线电话
        - 区城运中心24小时服务热线电话：60715191
        - **各街道（镇）24小时服务热线电话**
        """)

        img_p1 = Image.open(f"./files/{dist}-phone-1.jpeg")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "普陀区":
        st.write("""
        #### 热线电话
        为全力做好疫情防控工作，有效减少人员聚集，更好满足疫情期间居家生活和就医服务需求，切实保障人民群众生命安全和身体健康，现将普陀区疫情防控期间为民服务热线电话公告如下：
         - 普陀区24小时服务热线电话：52560990
         - 普陀区各街道、镇 2022年4月1日—4月5日期间24小时服务热线电话
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")    

    elif dist == "松江区":
        st.write("""
            松江区的居民可通过以下渠道采购主副食品：

            1、叮咚买菜、每日优鲜、饿了么、美团买菜、Yh永辉生活、盒马鲜生、大润发优鲜、京东等电商平台，大润发、永辉超市、物美、联华等超市平台，森活蔬叔、春强农业、蜀海公司、千囷农业、绿和园艺等生鲜蔬果提供方，“小鹿菜菜”微信小程序等为广大市民提供及时可靠的采购渠道。

            2、在“上海松江”微信公众号等多个渠道公布农产品保供合作社名单，小区可与合作社联系，确定蔬菜供应套餐内容和数量，在确保防疫要求的前提下，直送到点，保证居民蔬菜供应不断档。

            ３、老人、残疾人等特殊群体，可直接与属地联系，由属地志愿者代为采购。
            #### 热线电话
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")    

    elif dist == "奉贤区":
        st.write("""
            奉贤区的居民可通过以下渠道采购主副食品：

            1、 叮咚买菜、每日优鲜、饿了么、美团买菜、多多买菜、京东等电商平台，大润发、世纪联华超市、盒马等超市线上平台，为广大市民提供及时可靠的采购渠道。

            2、田头-村居直通车，在“奉贤三农”微信公众号等多个渠道公布农产品保供合作社名单，小区可与合作社联系，确定蔬菜供应套餐内容和数量，在确保防疫要求的前提下，直送到点，保证居民蔬菜供应不断档。

            3、登入“随申办”奉贤区旗舰店选择“贤农益起送”服务，预约团购套餐，选择预约时段、蔬菜套餐，提供多种套餐供市民线上选择。

            4、老人、残疾人等特殊群体，可直接与村居联系，由村居志愿者代为采购。 
            #### 热线电话
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.jpeg")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")    

    elif dist == "虹口区":
        st.write("""
            为全力做好疫情防控工作，更好地满足疫情期间市民居家生活和服务保障需求，切实保障人民群众生命健康，现将虹口区疫情防控期间为民服务热线电话公告如下：
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")    

    elif dist == "杨浦区":
        st.write("""
        #### 热线电话
        为全力做好疫情防控工作，有效减少人员聚集，更好地满足疫情期间，居家生活和就医服务需求，现将杨浦区疫情防控期间为民服务热线电话公告如下:
        - 区城运中心24小时服务热线电话：25033259
        - 各街道24小时服务热线电话

        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")


    elif dist == "宝山区":

        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        st.write("""
        #### 热线电话
            - 各街镇24小时服务热线电话
        """)
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")


    elif dist == "闵行区":
        st.write("""
        #### 热线电话
            - 区城运中心24小时服务热线电话：962000
            - 各街镇（莘庄工业区）服务热线电话
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    elif dist == "嘉定区":
        st.write("""
        疫情封控期间如何申请代配药？突发疾病，如何转诊治疗？一旦出现发热，要和谁联系？有心理咨询需求，能打哪条热线？为服务保障疫情封控期间广大居民医疗健康基本需求，嘉定区推出三项服务举措，具体安排如下↓
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")    



    elif dist == "金山区":
        st.write("""
            #### 热线电话
            - 各街镇生活服务热线电话
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")


    elif dist == "崇明区":
        st.write("""

            崇明区的居民可通过村居生活物资保供热线向所在村居下订单采购主副食品，村居志愿者会将订单需求整理汇总到所属乡镇，由乡镇统一向保供企业代为采购、统一安排志愿者配送。居民朋友们也可以在保供企业提供的套餐中进行选择，以便进一步提高效率。

            同时i百联等超市线上平台也为居民朋友们提供了及时可靠的采购渠道。 
            #### 热线电话
            - **崇明区各乡镇生活物资保供热线电话**
             (★热线电话仅限3月28日5点到4月1日5点期间使用)
        """)
        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")

        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")


    elif dist == "青浦区":

        img_p1 = Image.open(f"./files/{dist}-phone-1.png")
        st.image(img_p1,caption="")
        st.write("""
            #### 热线电话
        """)    
        img_p2 = Image.open(f"./files/{dist}-phone-2.png")
        st.image(img_p2,caption="")    
        st.write("---")
        st.write("""#### 问题\建议征集平台 """)
        img_s1 = Image.open(f"./files/{dist}-suggest-1.png")
        st.image(img_s1,caption="")

    else:
        pass

    st.write("---")
    st.info("""
        注:以上信息整理自公众号:青春上海 [3月27日](https://mp.weixin.qq.com/s/VMKQDJVuiLV3wrPmK9Ehew)和[3月29日](https://mp.weixin.qq.com/s/FxecuuiU5ghybTMbklo1eQ)推文.
    """)


# if __name__ == "__main__":
#     with open("./app/data.pkl",'rb') as f:
#         data = pickle.load(f)
#     app(data)