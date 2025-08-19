# Medical Data Visualizer


## Overview
**Medical Data Visualizer** is a Python project for exploring, analyzing, and visualizing medical examination data. The dataset includes body measurements, blood tests, and lifestyle factors. The project focuses on identifying patterns related to cardiovascular disease and key health indicators.

---

## Features

- **BMI Calculation & Overweight Detection:** Computes BMI and flags overweight patients (BMI > 25).  
- **Data Normalization:** Cholesterol and glucose values normalized (0 = good, 1 = bad).  
- **Categorical Bar Plots:** Visualizes counts of cholesterol, glucose, smoking, alcohol, activity, and overweight status by cardiovascular disease presence.  
- **Correlation Heatmap:** Cleans data and shows correlations between all variables to highlight risk factors.

---

## Dataset

The dataset `medical_examination.csv` contains:

| Feature | Description |
|---------|-------------|
| age | Age in days |
| height | Height in cm |
| weight | Weight in kg |
| gender | 1 = male, 2 = female |
| ap_hi | Systolic blood pressure |
| ap_lo | Diastolic blood pressure |
| cholesterol | 1: normal, 2: above normal, 3: well above normal |
| gluc | 1: normal, 2: above normal, 3: well above normal |
| smoke | Binary indicator of smoking |
| alco | Binary indicator of alcohol intake |
| active | Binary indicator of physical activity |
| cardio | Binary target variable for cardiovascular disease |
| overweight | Computed from BMI (0 = not overweight, 1 = overweight) |

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer
