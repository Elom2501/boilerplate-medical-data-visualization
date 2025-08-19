# medical_data_visualizer.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize data: 0 = good, 1 = bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4-8. Draw the Categorical Plot
def draw_cat_plot():
    # 5. Melt DataFrame for cat plot
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6. Group and reformat the data to show counts
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']) \
                   .size() \
                   .reset_index(name='total')
    
    # 7-8. Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig
    
    return fig

# 10-14. Draw the Heat Map
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ].copy()
    
    # Drop BMI column before heatmap to match test expectations
    if 'BMI' in df_heat.columns:
        df_heat = df_heat.drop(columns=['BMI'])
    
    # 12. Calculate the correlation matrix
    corr = df_heat.corr()
    
    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # 15. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=.5, square=True, cbar_kws={"shrink": .5}, ax=ax)
    
    return fig
    