# import required libs
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Foodtruck')
st.header('FoodTruck')
st.subheader('loads of food options')

### --- LOAD DATAFRAME
df = pd.read_csv("https://data.sfgov.org/api/views/rqzj-sfat/rows.csv")
food_df=df[['Latitude','Longitude','Location','locationid','Applicant','FacilityType','cnn','LocationDescription','Address','Zip Codes','FoodItems']]

#Data cleaning
food_df.dropna(inplace=True)
#zip code validation
food_df['Zip Codes'] = food_df['Zip Codes'].astype(int).astype(str).str.zfill(5)
#st.dataframe(df)


#SIDEBAR

st.sidebar.header('Select what to display')
facility = food_df['FacilityType'].unique().tolist()
type1 = st.sidebar.multiselect('FacilityType', facility, facility)

zips = food_df['Zip Codes'].unique().tolist()
type2 = st.sidebar.multiselect('Zip Codes', zips, zips)
nb_item = food_df['FoodItems'].value_counts()
nb_trucks = st.sidebar.slider("Number of FoodItems", int(nb_item.min()), int(nb_item.max()), (int(nb_item.min()), int(nb_item.max())), 1)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (food_df['Zip Codes'].isin(type2)) & (food_df['FacilityType'].isin(type1))
number_of_result = food_df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = food_df[mask].groupby(by=['Zip Codes']).count()[['FacilityType']]
df_grouped = df_grouped.reset_index()

st.subheader('Items available')

st.dataframe(food_df[mask]) 
#st.dataframe(df_grouped) #check

zip_df1=food_df[mask].groupby(['FacilityType','Zip Codes']).size()
#st.dataframe(zip_df1) #check
group_df1=pd.DataFrame(zip_df1,columns=['count'])
group_df1 = group_df1.reset_index()
#st.dataframe(group_df1) #check
group_df1.sort_values('count', ascending=False)

#FILTER TACO DATA # PLOT TABLE

taco1=food_df[mask].groupby(['FoodItems','FacilityType','Zip Codes','Applicant','Address']).size()
group_df3=pd.DataFrame(taco1,columns=['count'])
group_df3 = group_df3.reset_index()
group_df3.sort_values('count', ascending=False)

st.subheader('Tacos available')
taco_df=group_df3[['FoodItems','FacilityType','Zip Codes','Applicant','Address']]
mask1= taco_df['FoodItems'].str.contains('tacos', case=False)
st.table(taco_df[mask1])



# PLOT PIE CHART 1
pie_chart=px.pie(group_df1,
                 title='Total No. of FacilityType per zipcode',
                 values='count',
                names='FacilityType')
st.plotly_chart(pie_chart)

item_df=food_df[mask].groupby(['FoodItems','FacilityType']).size()
group_df2=pd.DataFrame(item_df,columns=['Itemcount'])
group_df2 = group_df2.reset_index()
group_df2.sort_values('Itemcount', ascending=False)

# --- PLOT BAR CHART
bar_chart = px.bar(group_df2,
                   x='FoodItems',
                   y='Itemcount',
                   text='Itemcount',
                   color_discrete_sequence = ['#F63366']*len(group_df2),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)


st.subheader('Food Items visual')
#pie2 check
truck_df1=food_df[mask].groupby(['FoodItems','Zip Codes']).size()
group_df=pd.DataFrame(truck_df1,columns=['count'])
group_df = group_df.reset_index()
group_df.sort_values('count', ascending=False)


# PLOT PIE CHART 2
pie_chart=px.pie(group_df,
                 title='Total No. of FoodItems',
                 values='count',
                names='FoodItems')
st.plotly_chart(pie_chart)

#end check

#end check


st.subheader('JSON result')

#JSON file return

json_output = df_grouped.to_json(orient="columns")
st.json(json_output)