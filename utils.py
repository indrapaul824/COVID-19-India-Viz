import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


df = pd.read_csv("state_wise.csv")

Tot_Con = df['Confirmed'][0]
print(Tot_Con)

df['Date'] = df['Last_Updated_Time'].astype('datetime64[ns]')

print(df['Date'].head())
