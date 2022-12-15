#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the file containing code for EDA of the original dataset. 

@author: Qiyuan Zhou
"""

"""
EDA
"""
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from pandas.plotting import table
import seaborn as sns 

path = "/Users/Toor/Desktop/dataset2.csv"
df = pd.read_csv(path)
#%%
"""
distribution plots by 16 category 
"""
types = (df['type'].value_counts()).to_frame()
# calculate percentages 
types['percent'] = round((types['type'] / types['type'].sum()) * 100,2)

colors = ['#fee6ce','#fdd0a2','#fdae6b','#fd8d3c','#f16913','#d94801','#a63603','#7f2704',
          '#9c2224','#c42d25','#e23f30','#ef5d41','#f38d4e','#f59a3a','#fabf58','#fccfa0']


plt.figure(figsize=(40,50))
ax1 = plt.subplot(121, aspect="equal")
types.plot.pie(y='type', figsize=(5, 5),colors = colors,ax=ax1)
ax1.get_legend().remove()

ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, types, loc='center')
tbl.auto_set_font_size(True)
#tbl.set_fontsize(12)
plt.show()

#%%
"""
distribution plots by 4 category 
"""

types.reset_index(inplace=True) # can only run once, need to initialize everytime 
types.columns = ['type','count','percentage']

type_pos = {'I':0,'E':0,'N':1,'S':1,'F':2,'T':2,'P':3,'J':3}

def get_count(letter):
    count = 0
    for i in range(len(types)):
        if types['type'][i][type_pos[letter]] == letter:
            count += types['count'][i]
    return count 

cat_df = pd.DataFrame()
cat_df['category'] = type_pos.keys()
counts = []
for i in type_pos.keys():
    counts.append(get_count(i))

# create a dataframe for 4 positions 
cat_df['count'] = counts
cat_df['percent'] = round((cat_df['count'] / cat_df['count'].sum()) * 100,2)

cat_df2 = pd.DataFrame()
cat_df2['category'] = ['I/E','N/S','F/T','P/J']
l = [cat_df['count'][0]+cat_df['count'][1],cat_df['count'][2]+cat_df['count'][3],
     cat_df['count'][4]+cat_df['count'][5],cat_df['count'][6]+cat_df['count'][7]]
cat_df2['count'] = l

#%%
plt.figure(figsize=(8, 8))
labels = cat_df2['category']
sizes = cat_df2['count']
colors = ['#B36A5E', '#C97C5D','#C89F9C','#EED7C5'] # 
labels_subgroup = cat_df['category']
sizes_subgroup = cat_df['count']
colors_subgroup = ['#CF9086','#DFB2AB','#D39F8A','#DFB6A5','#D4BBBA','#D8C9C8','#F5E5D8','#F7EBE2']
outside_donut = plt.pie(sizes, labels=labels, colors=colors,
                        startangle=90, frame=True,
                        autopct='%.2f%%',
                        pctdistance =0.85)
inside_donut = plt.pie(sizes_subgroup, labels=labels_subgroup,
                       colors=colors_subgroup, radius=0.7,
                       startangle=90, labeldistance=0.6,
                       autopct='%.2f%%',pctdistance =0.4)
centre_circle = plt.Circle((0, 0), 0.4, color='white', linewidth=0)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
 
plt.axis('equal')

plt.title('distribution by 4 categories')
plt.tight_layout()
plt.show()

