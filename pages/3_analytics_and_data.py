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

import pandas as pd
import numpy as np

import json

import streamlit as st

st.set_page_config(page_title="data / estimations", page_icon="📹")
st.markdown("# estimation and data analytics")
st.sidebar.header("what do you want to see?")

seeFullInformation = st.sidebar.checkbox("see raw data? [debugging]")
sideBarSelectBox = st.sidebar.selectbox('select data to be analyzed', ['Select One','Name-Based Estimations','Unified Meta Data'])

if sideBarSelectBox=='Select One':
    st.write(
        """This page has analytics data/services that can be utilized for simple estimations and quick agile testing."""
    )


beingUsed = False

if sideBarSelectBox!='Select One':
    beingUsed = True
    st.write("Currently on: " + sideBarSelectBox + "")

if sideBarSelectBox == 'Name-Based Estimations':  
    st.sidebar.write("This will utilize agify to guess your age")

    st.write("Based on a dataset in the backend consisting of scraped data of several websites/census - the agify api will try to guess the age/gender/nationality corresponding to the name")

    ipType = st.radio("What estimate do you want to fetch?",["Age", "Gender", "Nationality"],captions = ["Estimate the age based on the first name.", "Estimate the gender probabilities. [unfortunately - limited to binary estimations].", "Guess the nationality's probablities."])

    currentSwitch = "ip"

    if ipType == "Age":
        currentSwitch = "agify"
    elif ipType == "Gender":
        currentSwitch = "genderize"
    elif ipType == "Nationality":
        currentSwitch = "nationalize"

    name = st.text_input('Enter your first name to look up: ',"satyam")

    if name!="": 
        x = requests.get('https://api.'+ currentSwitch + '.io?name='+str(name))
        y = x.json()

        st.write("Name: " + y["name"])

        if "age" in y:
            st.write("Age: " + str(y["age"]))

        if "gender" in y:
            st.write("Gender: " + str(y["gender"]))

        if "probability" in y:
            st.write("Probablity: " + str(y["probability"]))

        if "country" in y:
            for item in y["country"]:
                st.write("Country ISO: " + item["country_id"] + " Probablity: " + str(item["probability"]))


        if seeFullInformation:
            st.write(y)

elif sideBarSelectBox == 'Unified Meta Data':  
    st.sidebar.write("Get complete meta data of any website through a crawler service.")

    st.write("Allows you to fetch complete metadata / text crawling / embedded images for any website URL without needing to visit the website yourself.")

    domain = st.text_input("Enter the website URL here (e.g. https://www.github.com/sudotman)")

    if domain!="":

        url = 'https://api.microlink.io'
        params = {'url': domain, 'meta': True}

        response = requests.get(url, params)

        st.write(response.json())


if beingUsed:
    st.button("Re-run")

st.sidebar.info("Reload the page if an error appears.")

