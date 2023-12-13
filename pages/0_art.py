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

import pandas as pd

st.set_page_config(page_title="Art", page_icon="📹")
st.markdown("# art corner")
st.sidebar.header("what do you want to see?")

seeFullInformation = st.sidebar.checkbox("see raw data? [debugging]")
sideBarSelectBox = st.sidebar.selectbox('select art collection', ['Select One','MET','Art Insitute of Chicago'])

if sideBarSelectBox=='Select One':
    st.write(
        """This page consists of art collections from prominent museums - select one to get a random art piece and all relevant information."""
    )


beingUsed = False

if sideBarSelectBox!='Select One':
    beingUsed = True
    st.write("Random art piece from " + sideBarSelectBox + ": ")

if sideBarSelectBox == 'MET':  
    st.sidebar.write("The met has over 485710 artworks publicly available - hope you have fun viewing one on random!")


    x = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects/'+str(random.randrange(0, 485710)))
    y = x.json()

    st.write('Title: ' + y["title"])
    st.write('Type: ' + y["objectName"])

    st.write('Artist: ' + y["artistDisplayName"])

    if y["culture"]!="":
        st.write('Culture: ' + y["culture"])

    if y["country"]!="":
        st.write('Country Found In: ' + y["country"])

    if y["department"]!="":    
        st.write('Department: ' + y["department"])

    st.write('Artwork Aquired On: ' + y["accessionYear"])

    if y["primaryImage"]!="":
        st.image(y["primaryImage"]) 
    else:
        st.write("This art piece doesn't have any image associated with it.") 

    if seeFullInformation:
        st.write(y)

elif sideBarSelectBox == 'Art Insitute of Chicago':  
    st.sidebar.write("Art Insitute of Chicago has over 123,000 artworks publicly available - hope you have fun viewing one on random!")

    x = requests.get('https://api.artic.edu/api/v1/artworks/'+str(random.randrange(0, 123000)))
    y = x.json()

    st.write('Title: ' + y["data"]["title"])
    st.write('Type: ' + y["data"]["medium_display"])

    st.write('Artist: ' + y["data"]["artist_display"])


    if y["data"]["place_of_origin"]!="":
        st.write('Country Found In: ' + y["data"]["place_of_origin"])

    if y["data"]["description"]!="" and y["data"]["description"]!= None:    
        st.write('Description: ' + y["data"]["description"])

    st.write('Artwork Aquired On: ' + y["data"]["date_display"])   

    if y["config"]["iiif_url"]!="":
        st.image(y["config"]["iiif_url"]+'/'+y["data"]["image_id"]+'/full/843,/0/default.jpg') 
    else:
        st.write("This art piece doesn't have any image associated with it.") 

    if seeFullInformation:
        st.write(y)

elif sideBarSelectBox == "Test":
    x = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
    y = x.json()

    st.write(y)

if beingUsed:
    st.button("Re-run")

st.sidebar.info("Reload the page if an error appears. Note: Sometimes images don't appear simlpy because the art piece doesn't have an image in their museum catalog.")

