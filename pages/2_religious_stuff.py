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

st.set_page_config(page_title="Religion", page_icon="📹")
st.markdown("# various religions's scriptures")
st.sidebar.header("what do you want to see?")

seeFullInformation = st.sidebar.checkbox("see raw information alongside the data? [debugging]")
sideBarSelectBox = st.sidebar.selectbox('select text to be fetched', ['Select One','Bible','Bhagavad Gita','Duck','Test'])

if sideBarSelectBox=='Select One':
    st.write(
        """This page consists religious texts of the few major religions of our world."""
    )


beingUsed = False

if sideBarSelectBox!='Select One':
    beingUsed = True
    st.write("Reading through " + sideBarSelectBox + ".")

if sideBarSelectBox == 'Bible':  
    st.sidebar.write("You can search for any bible verse from any chapter/book.")

    st.info("You can search for any chapter/verse to be looked for, press enter after you're done writing. Here are a few examples:\n\n john 3:16 (default) \n\n jn 3:16 (abbreviated) \n\n Leave it blank for a random verse.")
    verse = st.text_input('Enter the bibleverse to look up: ',"")

    x = None

    if verse=="":
        x = requests.get('https://bible-api.com/?random=verse')
    else:
        x = requests.get('https://bible-api.com/'+verse)
    
    y = x.json()

    st.write(y["reference"])
    st.write("Book: " + y["verses"][0]["book_name"] + " Chapter: " + str(y["verses"][0]["chapter"]) + " Verse: " + str(y["verses"][0]["verse"]))
    st.write(y["text"])

    if seeFullInformation:
        st.write(y)


elif sideBarSelectBox == 'Bhagavad Gita':  
    
    st.info("You can search for any chapter/verse to be looked for, press enter after you're done writing. Here are a few examples:\n\n 1.5 \n\n 18.2 \n\n Leave it blank for a random verse.")
    languagePreference = st.sidebar.selectbox("Language to view in ", ['English','Hindi'])
    verse = st.text_input('Enter the Gita shlok to look up: ',"")

    st.sidebar.write("You can search for any Gita shlok.")

    x = None

    if verse=="":
        x = requests.get('https://bhagavadgitaapi.in/slok/'+ str(random.randrange(1,18)) + '/' + str(random.randrange(1, 20)))
    else:
        x = requests.get('https://bhagavadgitaapi.in/slok/'+ (str(verse)).split('.')[0] + '/' + (str(verse)).split('.')[1])
    
    y = x.json()

    st.write(y["_id"])
    st.write("Chapter: " + str(y["chapter"]) + " Verse: " + str(y["verse"]))

    if languagePreference=='Hindi':
        st.write(y["slok"])
        st.write("Transliteration: " + y["transliteration"])
    elif languagePreference=="English":
        st.write("Translation by: "+y["siva"]["author"])
        st.write(y["siva"]["et"])

    if seeFullInformation:
        st.write(y)

       

elif sideBarSelectBox == "Test":
    x = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
    y = x.json()

    st.write(y)

if beingUsed:
    st.button("Re-run")

st.sidebar.info("Reload the page if an error appears. Note: Sometimes images don't appear simlpy because the art piece doesn't have an image in their museum catalog.")

