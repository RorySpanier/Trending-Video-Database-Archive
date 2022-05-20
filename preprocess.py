# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 17:59:13 2021

@author: Rory Spanier
"""

import pandas as pd
catIDs=pd.read_csv('category_ids.csv')
catIDs=catIDs.set_index('catID')

BRdata=pd.read_csv('BR_youtube_trending_data.csv')
BRdata['CountryCode']='BR'
BRdata['CountryName']='Brazil'

CAdata=pd.read_csv('CA_youtube_trending_data.csv')
CAdata['CountryCode']='CA'
CAdata['CountryName']='Canada'

DEdata=pd.read_csv('DE_youtube_trending_data.csv')
DEdata['CountryCode']='DE'
DEdata['CountryName']='Germany'

FRdata=pd.read_csv('FR_youtube_trending_data.csv')
FRdata['CountryCode']='FR'
FRdata['CountryName']='France'

GBdata=pd.read_csv('GB_youtube_trending_data.csv')
GBdata['CountryCode']='GB'
GBdata['CountryName']='Great Britain'

INdata=pd.read_csv('IN_youtube_trending_data.csv')
INdata['CountryCode']='IN'
INdata['CountryName']='India'

JPdata=pd.read_csv('JP_youtube_trending_data.csv')
JPdata['CountryCode']='JP'
JPdata['CountryName']='Japan'

KRdata=pd.read_csv('KR_youtube_trending_data.csv')
KRdata['CountryCode']='KR'
KRdata['CountryName']='South Korea'

MXdata=pd.read_csv('MX_youtube_trending_data.csv')
MXdata['CountryCode']='MX'
MXdata['CountryName']='Mexico'

RUdata=pd.read_csv('RU_youtube_trending_data.csv')
RUdata['CountryCode']='RU'
RUdata['CountryName']='Russia'

USdata=pd.read_csv('US_youtube_trending_data.csv')
USdata['CountryCode']='US'
USdata['CountryName']='USA'

df=pd.concat([BRdata,CAdata,DEdata,FRdata,GBdata,INdata,JPdata,KRdata,MXdata,RUdata,USdata],ignore_index=True)

temp=catIDs.loc[df['categoryId']]
temp.reset_index(inplace=True,drop=True)
df['category']=temp

print(df.nunique())
print(df['comments_disabled'].value_counts())

df.to_csv('youtube_trending_data.csv')