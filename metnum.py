import pandas as pd
import json
import streamlit as st
import time
import matplotlib.pyplot as pyl
import math as mat
from tabulate import tabulate
import altair as alt


def analitik():
    g = 9.81 #m/s^2
    C1 = 10 #kg/s
    C2 = 12.5 #kg/s
    C3 = 15 #kg/s
    m = 68.1 #kg

    if nilai_C == "C1":
        C = C1
    elif nilai_C == "C2":
        C = C2
    elif nilai_C == "C3":
        C = C3


    VeloAnalitik = ((g*m)/C) * (1-mat.exp(-(C/m)*t1))

    return VeloAnalitik

def numerik():
    g = 9.81 #m/s^2
    C1 = 10 #kg/s
    C2 = 12.5 #kg/s
    C3 = 15 #kg/s
    m = 68.1 #kg

    if nilai_C == "C1":
        C = C1
    elif nilai_C == "C2":
        C = C2
    elif nilai_C == "C3":
        C = C3


    VeloNumerik = (((g*m)/C) * (1-mat.exp(-(C/m)*ti))) + (g - ((C/m)*((g*m)/C) * (1-mat.exp(-(C/m)*ti))))*(t2 - ti)

    return VeloNumerik

pilihan_C = ["C1", "C2", "C3"]


nilai_C = st.selectbox("Pilih nilai C yang diinginkan ", (pilihan_C))
banyak_t = st.slider(label = "Banyaknya waktu ke-t", min_value = 1, max_value = 200) + 1
selisih_t  = st.slider(label = "Step-size diinginkan", min_value = 1, max_value = 200)

    

yanalit = []
xnum = []
ynum = []
datanum = []
dataanalit = []
DataNumerik = []
DataAnalitik = []
t1 = 0
t2 = 0
ti = 0 
for nilai_t in range(banyak_t):
    if nilai_t > 0:
        t1 += selisih_t
    dataanalit = (t1, analitik())
    DataAnalitik.append(dataanalit)
    yanalit.append(analitik())

    if nilai_t > 0:
        t2 += selisih_t
        ti = t2 - selisih_t
    datanum = (t2, numerik())
    DataNumerik.append(datanum)
    xnum.append(t2)
    ynum.append(numerik())


fig_1, ax1 = pyl.subplots()
ax1.plot(xnum, ynum)
ax1.set_title('Nilai t dan V dalam metode Numerik')
st.pyplot(fig_1)

fig_2, ax2 = pyl.subplots()
ax2.plot(xnum, yanalit)
ax2.set_title('Nilai t dan V dalam metode Analitik')
st.pyplot(fig_2)


header = ["Nilai-t", "Nilai-V"]

tabelNumerik = pd.DataFrame(DataNumerik, columns= header)
st.table(tabelNumerik)

tabelAnalitik = pd.DataFrame(DataAnalitik, columns= header)
st.table(tabelAnalitik)

