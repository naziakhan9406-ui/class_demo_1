import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Cars_cleaned.csv')
st.table(df.head())
