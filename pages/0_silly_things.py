# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import requests, random


import numpy as np

import json

import streamlit as st


def animation_demo() -> None:
    beingUsed = False

    if sideBarSelectBox!='Select One':
        beingUsed = True
        st.write("Fresh " + sideBarSelectBox + " for you:")

    if sideBarSelectBox == 'Cat Fact':
        x = requests.get('https://meowfacts.herokuapp.com/')
        y = x.json()

        # st.write(y)
        st.write(y["data"][0])   

        seeTheDoggo = st.checkbox("could i see some cats? please?")

        if seeTheDoggo:
            seeRequest = requests.get('https://api.thecatapi.com/v1/images/search')
            seeJson = seeRequest.json()
            st.image(seeJson[0]["url"])

    elif sideBarSelectBox == 'Dog Fact':
        x = requests.get('http://dog-api.kinduff.com/api/facts?number='+random.choice(['0', '1', '2', '3', '4','5','6','7','8','9']))
        y = x.json()
        
        # st.write(y)
        st.write(y["facts"][random.choice([0, 1, 2, 3, 4])])   

        seeTheDoggo = st.checkbox("i also want to see a dog! please! fast!")

        if seeTheDoggo:
            seeRequest = requests.get('https://random.dog/woof.json')
            seeJson = seeRequest.json()
            # st.write(seeJson)
            st.image(seeJson["url"])

    elif sideBarSelectBox == 'Duck':
            seeRequest = requests.get('https://random-d.uk/api/v2/random')
            seeJson = seeRequest.json()
            # st.write(seeJson)
            st.image(seeJson["url"])
            
    elif sideBarSelectBox == 'Fox':
            seeRequest = requests.get('https://randomfox.ca/floof/')
            seeJson = seeRequest.json()
            # st.write(seeJson)
            st.image(seeJson["image"])
    if beingUsed:
        st.button("Re-run")


st.set_page_config(page_title="Silly things", page_icon="📹")
st.markdown("# whimsical zone")
st.sidebar.header("silliness controller")

sideBarSelectBox = st.sidebar.selectbox('todays whimsy', ['Select One','Cat Fact','Dog Fact','Duck','Fox'])

if sideBarSelectBox=='Select One':
    st.write(
        """This page consists of things to pass your time (or learn cool facts) - from cat facts to other image generators, try it out on your sidebar."""
    )

animation_demo()


