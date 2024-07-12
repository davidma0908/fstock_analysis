import streamlit as st
import finlab
from finlab import data
import io
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


finlab.login('KIOiTEAqdE46cyyUB5JKOzcApIjBbG+w5VAz7MgR1wuw7LzQn0RXWD9bCJPAzLgK#vip_m')
close = data.get("price:收盤價")
st.dataframe(close)
