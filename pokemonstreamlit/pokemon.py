import pandas as pd
import numpy as np
from sklearn.datasets import images
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,export_graphviz
import streamlit as st




pokemonid=pd.read_csv("pokemonid.csv")
pokemonid.set_index=pokemonid["#"]
pokemonid["Name"]=pokemonid["Name"].str.lower()
pokemonid.index += 1
pokemonid=pokemonid[["Name"]]

combat=pd.read_csv("combats.csv")
y=combat["Winner"]
x=combat.drop("Winner",axis=1)
tree=DecisionTreeClassifier()
model=tree.fit(x,y)


first=st.sidebar.selectbox("Choose your first pokemon",pokemonid)
firstid=pokemonid[pokemonid["Name"]==first].index.values[0]

second=st.sidebar.selectbox("Choose your second pokemon",pokemonid)
secondid=pokemonid[pokemonid["Name"]==second].index.values[0]

st.image("logo.png")
col1,col2,col3=st.columns(3)
with col1:
    if first.endswith(".jpg"):
        st.image(first+".jpg",width=200)
    else:
        st.image(first+".png",width=200)
        button=st.button("Fight")
with col2:
    st.image("channels4_profile.jpg",width=200)
with col3:
    if second.endswith(".jpg"):
        st.image(second + ".jpg", width=200)
    else:
        st.image(second + ".png", width=200)
if button:
    st.image("firelogo",width=700)

    a=(model.predict([[firstid,secondid]]))
    result=pokemonid.loc[a[0]][0]
    st.header("Victory")
    st.subheader(result)
    if result.endswith(".jpg"):
        st.image(result+".jpg",width=500)
    else:
        st.image(result+".png",width=500)






