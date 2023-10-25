# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:17:46 2023

@author: uurty
"""

import pandas as pd

df = pd.read_excel("C:\\Users\\uurty\\Downloads\\GYH FRACAS TABLOSU_.xlsx")
df = df.iloc[2:]
df.columns = df.iloc[0]

# İlk satırı sildiğinizden emin olun
df = df.iloc[1:]

df = df.reset_index(drop = True)

df = df.dropna(subset=['Mail-Atan\nPersonel'], how='all')
# Veri çerçevesini filtreleyerek, belirli sütun ve değere sahip satırları seçin
print(df.head())
