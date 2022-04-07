import streamlit as st
import pickle
import json
import folium
from streamlit_folium import folium_static
from utils import load_pickle,dump_pickle,distinct
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


def add_point(df,ratio=1,color_index=0,opacity=0.5,fill_opacity=0.8):
    layer_name = '通报小区'
    color_ls = ["#f4e925","#b62020"]
    line_color=color_ls[color_index]
    fill_color=color_ls[color_index]
    
    
    fg = folium.FeatureGroup(name=layer_name)

    for point in df.iterrows():
        fg.add_child(
            folium.CircleMarker(
                (point[1]['latitude'],point[1]['longitude']),
                radius=point[1]['日期']*ratio,
                color=line_color,
                opacity=opacity,
                fill_opacity=fill_opacity,
                fill_color=fill_color,
                popup=(folium.Popup(f"{point[1]['详细地址']} 通报 {point[1]['日期']} 次",max_width=300)),
            )
        )
    return fg

def plot_maker(target_lat,target_long,target_area):
    marker = folium.Marker([target_lat,target_long],popup=(folium.Popup(target_area,max_width=200)))
    return marker

def plot_map(node_layer=None,center = [31.251737,121.422300],zoom_start=9,fig_type=0):
    if fig_type == 0:
        sh_map = folium.Map(center,
                   tiles='http://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/{z}/{y}/{x}',
                   attr='蓝黑版',
                   zoom_start=zoom_start,
                   left='0%',
                   min_lat=30,
                   max_lat=32,
                   min_lon=120,
                   max_lon=122.5,                 
                   min_zoom = 9,  
                   # width='60%',
                   # height='60%'
                  )
    else:
        sh_map = folium.Map(center,
          tiles = 'http://webst02.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&style=7',
          attr='default',
           zoom_start=zoom_start,
           left='0%',
           min_lat=30,
           max_lat=32,
           min_lon=120,
           max_lon=122.5,                 
           min_zoom = 11,                              
           # width='60%',
           # height='60%'
          )
    if node_layer is not None:
        sh_map.add_child(node_layer)

    return sh_map


def load_point2layer(point_json):
    """
    加载保存的数据点.
    """
    point_layer = folium.GeoJson(point_json, name='标记点', show=False,
                             tooltip=folium.GeoJsonTooltip(
                                 fields=['详细地址','日期'],
                                 aliases=['社区:','次数:'],
                                 localize=True),
                                 marker = folium.CircleMarker(  radius=1,
                                                                color="#f4e925",
                                                                opacity=0,
                                                                fill_opacity=0.8,
                                                                fill_color="#f4e925",
                                                            )
                             )
    return point_layer


def plot_summary(df_summary,width=450, height=400,):
    colors = ['rgb(67,67,67)', 'firebrick', 'rgb(49,130,189)','rgb(131, 90, 241)', 'rgb(189,189,189)',]
    fig = go.Figure()

    # fig.add_trace(go.Scatter(x=df_summary['日期'], y=df_summary['确诊'] + df_summary['无症状感染者'], fill='tonexty',
    #                     mode= 'markers+lines',name='合计',line=dict(color=colors[1])))
    fig.add_trace(go.Scatter(x=df_summary['日期'], y=df_summary['确诊'], fill='tozeroy',
                        mode='markers+lines',name='确诊',line=dict(color=colors[1])
                        ))
    fig.add_trace(go.Scatter(x=df_summary['日期'], y=df_summary['无症状感染者'], fill='tonexty',
                        mode= 'markers+lines',name='无症状感染者',line=dict(color=colors[2])))

    fig.update_layout(
        showlegend=True,
        plot_bgcolor='rgba(1,0,0,0)',
        legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01)
    )
    
    fig.update_layout(title='',
                      width=width,
                      height=height,
                      margin=dict(l=10, r=10, t=20, b=10),
                      # paper_bgcolor='rgba(1,0,0,0)',
                      # xaxis_title='日期',
                      # yaxis_title='人数'
                     )
    # 设置拖拽效果
    # https://plotly.com/javascript/reference/#layout-hovermode
    fig.update_layout(hovermode='x unified',dragmode=False)
    return fig
