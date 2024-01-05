import pandas as pd
import plotly.express as px
import folium
import random
import streamlit as st
import streamlit_folium as st_folium
from folium.plugins import MarkerCluster


@st.experimental_memo
def load_data(file_name):
    data = pd.read_csv(file_name)
    data = data.dropna()
    return data

data_2021 = load_data("LA_Crime_Data_2021.csv")
data_2022 = load_data("LA_Crime_Data_2022.csv")
data_2023 = load_data("LA_Crime_Data_2023.csv")

@st.experimental_memo
def map_2021():
    #2021_犯罪地區分布(隨機抽查30000)
    # Randomly sample a small portion of the data to avoid performance issues
    sampled_data = data_2021.sample(n=30000, random_state=1)
    # Create a map centered around an average location in the dataset
    mean_lat, mean_lon = data_2021['LAT'].mean(), data_2021['LON'].mean()
    map_2021 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Using a marker cluster to manage the markers
    marker_cluster = MarkerCluster().add_to(map_2021)
    # Add markers to the map
    for idx, row in sampled_data.iterrows():
        folium.Marker(location=[row['LAT'], row['LON']]).add_to(marker_cluster)
    st_folium.folium_static(map_2021)

@st.experimental_memo
def map_2022():
    #2022_犯罪地區分布(隨機抽查30000)
    # Randomly sample a small portion of the data to avoid performance issues
    sampled_data = data_2022.sample(n=30000, random_state=1)
    # Create a map centered around an average location in the dataset
    mean_lat, mean_lon = data_2022['LAT'].mean(), data_2022['LON'].mean()
    map_2022 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Using a marker cluster to manage the markers
    marker_cluster = MarkerCluster().add_to(map_2022)
    # Add markers to the map
    for idx, row in sampled_data.iterrows():
        folium.Marker(location=[row['LAT'], row['LON']]).add_to(marker_cluster)
    st_folium.folium_static(map_2022)

@st.experimental_memo
def map_2023():
    #2023_犯罪地區分布(隨機抽查30000)
    # Randomly sample a small portion of the data to avoid performance issues
    sampled_data = data_2023.sample(n=30000, random_state=1)
    # Create a map centered around an average location in the dataset
    mean_lat, mean_lon = data_2023['LAT'].mean(), data_2023['LON'].mean()
    map_2023 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Using a marker cluster to manage the markers
    marker_cluster = MarkerCluster().add_to(map_2023)
    # Add markers to the map
    for idx, row in sampled_data.iterrows():
        folium.Marker(location=[row['LAT'], row['LON']]).add_to(marker_cluster)
    st_folium.folium_static(map_2023)

@st.experimental_memo
def aggregated_map_2021():
    #2021_犯罪地區分布(各區總計)
    # Recalculating the mean latitude and longitude
    mean_lat = data_2021['LAT'].mean()
    mean_lon = data_2021['LON'].mean()
    # Aggregating data by area name
    area_crime_counts = data_2021.groupby('AREA NAME').size().reset_index(name='Crime Count')
    # Merging with the original data to get the latitude and longitude for each area
    # Here, we use the mean latitude and longitude for each area
    area_location = data_2021.groupby('AREA NAME')[['LAT', 'LON']].mean().reset_index()
    aggregated_data = pd.merge(area_crime_counts, area_location, on='AREA NAME')
    # Create a map
    aggregated_map_2021 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Add markers for each area with the crime count
    for idx, row in aggregated_data.iterrows():
        folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=f"{row['AREA NAME']}: {row['Crime Count']} crimes",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(aggregated_map_2021)
    st_folium.folium_static(aggregated_map_2021)

@st.experimental_memo
def aggregated_map_2022():
    #2022_犯罪地區分布(各區總計)
    # Recalculating the mean latitude and longitude
    mean_lat = data_2022['LAT'].mean()
    mean_lon = data_2022['LON'].mean()
    # Aggregating data by area name
    area_crime_counts = data_2022.groupby('AREA NAME').size().reset_index(name='Crime Count')
    # Merging with the original data to get the latitude and longitude for each area
    # Here, we use the mean latitude and longitude for each area
    area_location = data_2022.groupby('AREA NAME')[['LAT', 'LON']].mean().reset_index()
    aggregated_data = pd.merge(area_crime_counts, area_location, on='AREA NAME')
    # Create a map
    aggregated_map_2022 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Add markers for each area with the crime count
    for idx, row in aggregated_data.iterrows():
        folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=f"{row['AREA NAME']}: {row['Crime Count']} crimes",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(aggregated_map_2022)
    st_folium.folium_static(aggregated_map_2022)

@st.experimental_memo
def aggregated_map_2023():
    #2023_犯罪地區分布(各區總計)
    # Recalculating the mean latitude and longitude
    mean_lat = data_2023['LAT'].mean()
    mean_lon = data_2023['LON'].mean()
    # Aggregating data by area name
    area_crime_counts = data_2023.groupby('AREA NAME').size().reset_index(name='Crime Count')
    # Merging with the original data to get the latitude and longitude for each area
    # Here, we use the mean latitude and longitude for each area
    area_location = data_2023.groupby('AREA NAME')[['LAT', 'LON']].mean().reset_index()
    aggregated_data = pd.merge(area_crime_counts, area_location, on='AREA NAME')
    # Create a map
    aggregated_map_2023 = folium.Map(location=[mean_lat, mean_lon], zoom_start=10)
    # Add markers for each area with the crime count
    for idx, row in aggregated_data.iterrows():
        folium.Marker(
        location=[row['LAT'], row['LON']],
        popup=f"{row['AREA NAME']}: {row['Crime Count']} crimes",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(aggregated_map_2023)
    st_folium.folium_static(aggregated_map_2023)

@st.experimental_memo
def fig_2021():
    #2021_犯罪數趨勢圖
    # 確保 'DATE OCC' 是 datetime 類型
    data_2021['DATE OCC'] = pd.to_datetime(data_2021['DATE OCC'])
    # 創建一個按日期分組的數據框，計算每天的犯罪事件數
    crime_counts_by_date = data_2021['DATE OCC'].value_counts().sort_index().reset_index()
    crime_counts_by_date.columns = ['Date', 'Number of Crimes']
    # 使用 Plotly 創建折線圖
    fig_2021 = px.line(crime_counts_by_date, x='Date', y='Number of Crimes', title='Number of Crimes Over Time')
    fig_2021.update_xaxes(title_text='Date')
    fig_2021.update_yaxes(title_text='Number of Crimes')
    st.plotly_chart(fig_2021)

@st.experimental_memo
def fig_2022():
    #2022_犯罪數趨勢圖
    # 確保 'DATE OCC' 是 datetime 類型
    data_2022['DATE OCC'] = pd.to_datetime(data_2022['DATE OCC'])
    # 創建一個按日期分組的數據框，計算每天的犯罪事件數
    crime_counts_by_date = data_2022['DATE OCC'].value_counts().sort_index().reset_index()
    crime_counts_by_date.columns = ['Date', 'Number of Crimes']
    # 使用 Plotly 創建折線圖
    fig_2022 = px.line(crime_counts_by_date, x='Date', y='Number of Crimes', title='Number of Crimes Over Time')
    fig_2022.update_xaxes(title_text='Date')
    fig_2022.update_yaxes(title_text='Number of Crimes')
    st.plotly_chart(fig_2022)

@st.experimental_memo
def fig_2023():
    #2023_犯罪數趨勢圖
    # 確保 'DATE OCC' 是 datetime 類型
    data_2023['DATE OCC'] = pd.to_datetime(data_2023['DATE OCC'])
    # 創建一個按日期分組的數據框，計算每天的犯罪事件數
    crime_counts_by_date = data_2023['DATE OCC'].value_counts().sort_index().reset_index()
    crime_counts_by_date.columns = ['Date', 'Number of Crimes']
    # 使用 Plotly 創建折線圖
    fig_2023 = px.line(crime_counts_by_date, x='Date', y='Number of Crimes', title='Number of Crimes Over Time')
    fig_2023.update_xaxes(title_text='Date')
    fig_2023.update_yaxes(title_text='Number of Crimes')
    st.plotly_chart(fig_2023)

@st.experimental_memo
def sex_2021():
    #2021_依照日期_受害人性別
    # 確保 'DATE OCC' 是 datetime 類型
    data_2021['DATE OCC'] = pd.to_datetime(data_2021['DATE OCC'])
    # 對 'Vict Sex' 和 'DATE OCC' 進行分組並計數
    grouped_data_sex_date = data_2021.groupby(['DATE OCC', 'Vict Sex']).size().reset_index(name='Count')
    # 創建動態折線圖
    sex_2021 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Vict Sex', 
              title='Victim Sex Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Victims', 'Vict Sex': 'Victim Sex'})
    st.plotly_chart(sex_2021)

@st.experimental_memo
def sex_2022():
    #2022_依照日期_受害人性別
    # 確保 'DATE OCC' 是 datetime 類型
    data_2022['DATE OCC'] = pd.to_datetime(data_2022['DATE OCC'])
    # 對 'Vict Sex' 和 'DATE OCC' 進行分組並計數
    grouped_data_sex_date = data_2022.groupby(['DATE OCC', 'Vict Sex']).size().reset_index(name='Count')
    # 創建動態折線圖
    sex_2022 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Vict Sex', 
              title='Victim Sex Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Victims', 'Vict Sex': 'Victim Sex'})
    st.plotly_chart(sex_2022)

@st.experimental_memo
def sex_2023():
    #2023_依照日期_受害人性別
    # 確保 'DATE OCC' 是 datetime 類型
    data_2023['DATE OCC'] = pd.to_datetime(data_2023['DATE OCC'])
    # 對 'Vict Sex' 和 'DATE OCC' 進行分組並計數
    grouped_data_sex_date = data_2023.groupby(['DATE OCC', 'Vict Sex']).size().reset_index(name='Count')
    # 創建動態折線圖
    sex_2023 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Vict Sex', 
              title='Victim Sex Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Victims', 'Vict Sex': 'Victim Sex'})
    st.plotly_chart(sex_2023)

@st.experimental_memo
def sex_2021_total():
    #2021_受害者性別總計
    # 統計受害者性別 (Vict Sex)
    vict_sex_counts_full = data_2021['Vict Sex'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    sex_2021_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Victim Sex', 'y': 'Count'}, title='Victim Sex Distribution')
    st.plotly_chart(sex_2021_total)

@st.experimental_memo
def sex_2022_total():
    #2022_受害者性別總計
    # 統計受害者性別 (Vict Sex)
    vict_sex_counts_full = data_2022['Vict Sex'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    sex_2022_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Victim Sex', 'y': 'Count'}, title='Victim Sex Distribution')
    st.plotly_chart(sex_2022_total)

@st.experimental_memo
def sex_2023_total():
    #2023_受害者性別總計
    # 統計受害者性別 (Vict Sex)
    vict_sex_counts_full = data_2023['Vict Sex'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    sex_2023_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Victim Sex', 'y': 'Count'}, title='Victim Sex Distribution')
    st.plotly_chart(sex_2023_total)

@st.experimental_memo
def Status_Desc_2021():
    #2021_依照日期_受害事件
    # 確保 'DATE OCC' 是 datetime 類型
    data_2021['DATE OCC'] = pd.to_datetime(data_2021['DATE OCC'])
    grouped_data_sex_date = data_2021.groupby(['DATE OCC', 'Status Desc']).size().reset_index(name='Count')
    # 創建動態折線圖
    Status_Desc_2021 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Status Desc', 
              title='Status Desc Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Status Desc', 'Status Desc': 'Status Desc'})
    st.plotly_chart(Status_Desc_2021)

@st.experimental_memo
def Status_Desc_2022():
    #2022_依照日期_受害事件
    # 確保 'DATE OCC' 是 datetime 類型
    data_2022['DATE OCC'] = pd.to_datetime(data_2022['DATE OCC'])
    grouped_data_sex_date = data_2022.groupby(['DATE OCC', 'Status Desc']).size().reset_index(name='Count')
    # 創建動態折線圖
    Status_Desc_2022 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Status Desc', 
              title= 'Status Desc Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Status Desc', 'Status Desc': 'Status Desc'})
    st.plotly_chart(Status_Desc_2022)

@st.experimental_memo
def Status_Desc_2023():
    #2023_依照日期_受害事件
    # 確保 'DATE OCC' 是 datetime 類型
    data_2023['DATE OCC'] = pd.to_datetime(data_2023['DATE OCC'])
    grouped_data_sex_date = data_2023.groupby(['DATE OCC', 'Status Desc']).size().reset_index(name='Count')
    # 創建動態折線圖
    Status_Desc_2023 = px.line(grouped_data_sex_date, x='DATE OCC', y='Count', color='Status Desc', 
              title= 'Status Desc Count Over Time by Date',
              labels={'DATE OCC': 'Date', 'Count': 'Number of Status Desc', 'Status Desc': 'Status Desc'})
    st.plotly_chart(Status_Desc_2023)

@st.experimental_memo
def Status_Desc_2021_total():
    #2021_受害事件總計
    vict_sex_counts_full = data_2021['Status Desc'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    Status_Desc_2021_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Status Desc', 'y': 'Count'}, title= 'Status Desc Distribution')
    st.plotly_chart(Status_Desc_2021_total)

@st.experimental_memo
def Status_Desc_2022_total():
    #2022_受害事件總計
    vict_sex_counts_full = data_2022['Status Desc'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    Status_Desc_2022_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Status Desc', 'y': 'Count'}, title='Status Desc Distribution')
    st.plotly_chart(Status_Desc_2022_total)

@st.experimental_memo
def Status_Desc_2023_total():
    #2023_受害事件總計
    vict_sex_counts_full = data_2023['Status Desc'].value_counts()
    # 使用 Plotly 繪製動態長條圖
    Status_Desc_2023_total = px.bar(vict_sex_counts_full, x=vict_sex_counts_full.index, y=vict_sex_counts_full.values, 
             labels={'x': 'Victim Sex', 'y': 'Count'}, title='Status Desc Distribution')
    st.plotly_chart(Status_Desc_2023_total)

@st.experimental_memo
def bar_age_2021():
    #2021_害者年齡區間
    age_bins = range(0, 120, 10)
    data_2021['Age Range'] = pd.cut(data_2021['Vict Age'], bins=age_bins)
    # 将 Interval 类型转换为字符串
    data_2021['Age Range'] = data_2021['Age Range'].astype(str)
    # 數據匯總
    age_range_counts = data_2021['Age Range'].value_counts().sort_index()
    # 創建動態長條圖
    bar_age_2021 = px.bar(age_range_counts, x=age_range_counts.index, y=age_range_counts.values, labels={'y': 'Number of Crimes', 'index': 'Age Range'})
    bar_age_2021.update_layout(title='Number of Crimes per Age Range in 2021', xaxis_title='Age Range', yaxis_title='Number of Crimes')
    st.plotly_chart(bar_age_2021)

@st.experimental_memo
def bar_age_2022():
    #2022_受害者年齡區間
    age_bins = range(0, 120, 10)
    data_2022['Age Range'] = pd.cut(data_2022['Vict Age'], bins=age_bins)
    # 将 Interval 类型转换为字符串
    data_2022['Age Range'] = data_2022['Age Range'].astype(str)
    # 數據匯總
    age_range_counts = data_2022['Age Range'].value_counts().sort_index()
    # 創建動態長條圖
    bar_age_2022 = px.bar(age_range_counts, x=age_range_counts.index, y=age_range_counts.values, labels={'y': 'Number of Crimes', 'index': 'Age Range'})
    bar_age_2022.update_layout(title='Number of Crimes per Age Range in 2022', xaxis_title='Age Range', yaxis_title='Number of Crimes')
    st.plotly_chart(bar_age_2022)

@st.experimental_memo
def bar_age_2023():
    #2023_受害者年齡區間
    age_bins = range(0, 120, 10)
    data_2023['Age Range'] = pd.cut(data_2023['Vict Age'], bins=age_bins)
    # 将 Interval 类型转换为字符串
    data_2023['Age Range'] = data_2023['Age Range'].astype(str)
    # 數據匯總
    age_range_counts = data_2023['Age Range'].value_counts().sort_index()
    # 創建動態長條圖
    bar_age_2023 = px.bar(age_range_counts, x=age_range_counts.index, y=age_range_counts.values, labels={'y': 'Number of Crimes', 'index': 'Age Range'})
    bar_age_2023.update_layout(title='Number of Crimes per Age Range in 2023', xaxis_title='Age Range', yaxis_title='Number of Crimes')
    st.plotly_chart(bar_age_2023)

@st.experimental_memo
def line_age_2021():
    #2021_受害者年齡區間_依照日期
    # 確保日期和年齡字段的正確格式
    data_2021['DATE OCC'] = pd.to_datetime(data_2021['DATE OCC'])
    data_2021['Vict Age'] = pd.to_numeric(data_2021['Vict Age'], errors='coerce')  # 轉換為數字，非數字轉為 NaN
    # 計算每個日期的受害者平均年齡
    average_age_by_date = data_2021.groupby('DATE OCC')['Vict Age'].mean().reset_index()
    # 創建折線圖
    line_age_2021 = px.line(average_age_by_date, x='DATE OCC', y='Vict Age', title='Average Victim Age by Date',
                   labels={'DATE OCC': 'Date of Occurrence', 'Vict Age': 'Average Victim Age'})
    st.plotly_chart(line_age_2021)

@st.experimental_memo
def line_age_2022():
    #2022_受害者年齡區間_依照日期
    # 確保日期和年齡字段的正確格式
    data_2022['DATE OCC'] = pd.to_datetime(data_2022['DATE OCC'])
    data_2022['Vict Age'] = pd.to_numeric(data_2022['Vict Age'], errors='coerce')  # 轉換為數字，非數字轉為 NaN
    # 計算每個日期的受害者平均年齡
    average_age_by_date = data_2022.groupby('DATE OCC')['Vict Age'].mean().reset_index()
    # 創建折線圖
    line_age_2022 = px.line(average_age_by_date, x='DATE OCC', y='Vict Age', title='Average Victim Age by Date',
                   labels={'DATE OCC': 'Date of Occurrence', 'Vict Age': 'Average Victim Age'})
    st.plotly_chart(line_age_2022)

@st.experimental_memo
def line_age_2023():
    #2023_受害者年齡區_依照日期
    # 確保日期和年齡字段的正確格式
    data_2023['DATE OCC'] = pd.to_datetime(data_2023['DATE OCC'])
    data_2023['Vict Age'] = pd.to_numeric(data_2023['Vict Age'], errors='coerce')  # 轉換為數字，非數字轉為 NaN
    # 計算每個日期的受害者平均年齡
    average_age_by_date = data_2023.groupby('DATE OCC')['Vict Age'].mean().reset_index()
    # 創建折線圖
    line_age_2023 = px.line(average_age_by_date, x='DATE OCC', y='Vict Age', title='Average Victim Age by Date',
                   labels={'DATE OCC': 'Date of Occurrence', 'Vict Age': 'Average Victim Age'})
    st.plotly_chart(line_age_2023)

# Streamlit介面         
#狀態列
st.sidebar.title('選單')
options = st.sidebar.selectbox('選擇年分:', ['2021','2022', '2023'])     
if options == '2021':
    st.subheader("2021洛杉磯犯罪數據")
    fig = st.selectbox("選擇圖表", ["犯罪地區分布(隨機抽查30000)", "犯罪地區分布(各區總計)","犯罪數趨勢圖","依照日期_受害人性別","受害者性別總計","依照日期_受害事件","受害事件總計","受害者年齡區間","受害者年齡區間_依照日期"])
    if fig == "犯罪地區分布(隨機抽查30000)":
        st.subheader("2021洛杉磯犯罪地區分布(隨機抽查30000)")
        map_2021()
    elif fig == "犯罪地區分布(各區總計)":
        st.subheader("2021洛杉磯犯罪地區分布(各區總計)")
        aggregated_map_2021()
    elif fig == "犯罪數趨勢圖":
        st.subheader("2021洛杉磯犯罪趨勢圖")
        fig_2021()
    elif fig == "依照日期_受害人性別":
        st.subheader("2021洛杉磯犯罪_受害者性別(依照日期)")
        sex_2021()
    elif fig == "受害者性別總計":
        st.subheader("2021洛杉磯犯罪_受害者性別總計")
        sex_2021_total()
    elif fig == "依照日期_受害事件":
        st.subheader("2021洛杉磯犯罪_受害事件(依照日期)")
        Status_Desc_2021()
    elif fig == "受害事件總計":
        st.subheader("2021洛杉磯犯罪_受害事件總計")
        Status_Desc_2021_total()
    elif fig == "受害者年齡區間":
        st.subheader("2021洛杉磯犯罪_受害者年齡區間")
        bar_age_2021()
    elif fig == "受害者年齡區間_依照日期":
        st.subheader("2021洛杉磯犯罪_受害者年齡區間(依照日期)")
        line_age_2021()

elif options == '2022':
    st.subheader("2022洛杉磯犯罪數據")
    fig = st.selectbox("選擇圖表", ["犯罪地區分布(隨機抽查30000)", "犯罪地區分布(各區總計)","犯罪數趨勢圖","依照日期_受害人性別","受害者性別總計","依照日期_受害事件","受害事件總計","受害者年齡區間","受害者年齡區間_依照日期"])
    if fig == "犯罪地區分布(隨機抽查30000)":
        st.subheader("2022洛杉磯犯罪地區分布(隨機抽查30000)")
        map_2022()
    elif fig == "犯罪地區分布(各區總計)":
        st.subheader("2022洛杉磯犯罪地區分布(各區總計)")
        aggregated_map_2022()
    elif fig == "犯罪數趨勢圖":
        st.subheader("2022洛杉磯犯罪趨勢圖")
        fig_2022()
    elif fig == "依照日期_受害人性別":
        st.subheader("2022洛杉磯犯罪_受害者性別(依照日期)")
        sex_2022()
    elif fig == "受害者性別總計":
        st.subheader("2022洛杉磯犯罪_受害者性別總計")
        sex_2022_total()
    elif fig == "依照日期_受害事件":
        st.subheader("2022洛杉磯犯罪_受害事件(依照日期)")
        Status_Desc_2022()
    elif fig == "受害事件總計":
        st.subheader("2022洛杉磯犯罪_受害事件總計")
        Status_Desc_2022_total()
    elif fig == "受害者年齡區間":
        st.subheader("2022洛杉磯犯罪_受害者年齡區間")
        bar_age_2022()
    elif fig == "受害者年齡區間_依照日期":
        st.subheader("2022洛杉磯犯罪_受害者年齡區間(依照日期)")
        line_age_2022()
        
elif options == '2023':
    st.subheader("2023洛杉磯犯罪數據")
    fig = st.selectbox("選擇圖表", ["犯罪地區分布(隨機抽查30000)", "犯罪地區分布(各區總計)","犯罪數趨勢圖","依照日期_受害人性別","受害者性別總計","依照日期_受害事件","受害事件總計","受害者年齡區間","受害者年齡區間_依照日期"])
    if fig == "犯罪地區分布(隨機抽查30000)":
        st.subheader("2023洛杉磯犯罪地區分布(隨機抽查30000)")
        map_2023()
    elif fig == "犯罪地區分布(各區總計)":
        st.subheader("2023洛杉磯犯罪地區分布(各區總計)")
        aggregated_map_2023()
    elif fig == "犯罪數趨勢圖":
        st.subheader("2023洛杉磯犯罪趨勢圖")
        fig_2023()
    elif fig == "依照日期_受害人性別":
        st.subheader("2023洛杉磯犯罪_受害者性別(依照日期)")
        sex_2023()
    elif fig == "受害者性別總計":
        st.subheader("2023洛杉磯犯罪_受害者性別總計")
        sex_2023_total()
    elif fig == "依照日期_受害事件":
        st.subheader("2023洛杉磯犯罪_受害事件(依照日期)")
        Status_Desc_2023()
    elif fig == "受害事件總計":
        st.subheader("2023洛杉磯犯罪_受害事件總計")
        Status_Desc_2023_total()
    elif fig == "受害者年齡區間":
        st.subheader("2023洛杉磯犯罪_受害者年齡區間")
        bar_age_2023()
    elif fig == "受害者年齡區間_依照日期":
        st.subheader("2023洛杉磯犯罪_受害者年齡區間(依照日期)")
        line_age_2023()
