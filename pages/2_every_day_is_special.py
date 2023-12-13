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

from datetime import datetime

import json

import streamlit as st

st.set_page_config(page_title="Every Day is Special :)", page_icon="📹")
st.markdown("# every day is a special day!")
st.sidebar.header("what do you want to see?")

seeFullInformation = st.sidebar.checkbox("see raw data? [debugging]")

st.sidebar.info("By default it fetches information for the current date. Enter your values below for a date of your choice.")
sidebarDate = st.sidebar.text_input("Enter your date (dd-mm) e.g. 19-04 or 19-4 for 19th April")


st.write(
    """This page consists of some brief about everything special about today, starting with everyone who died today!"""
)


beingUsed = True

today_date = datetime.now()

month_day_list = None

if sidebarDate=="":
    # Extract month and day from today's date
    month_day_list = [str(int(today_date.day)), str(int(today_date.month))]
else:
    month_day_list = [str(int(sidebarDate.split('-')[0])), str(int(sidebarDate.split('-')[1]))]

st.sidebar.write("Every day, no matter how inconsequential the day may seem, has had major events and will perpetuate the same notion.")

requestString = 'https://byabbe.se/on-this-day/'+str(month_day_list[1])+'/'+str(month_day_list[0])+'/deaths.json'

# st.write(requestString)
x = requests.get(requestString)

# st.write(x.json())

y = x.json()

dateFetched = y["date"]
st.header('List of people who died on ' + dateFetched)


for item in y["deaths"]:
    description = item["description"]
    year = item["year"]
    wikiLink = item["wikipedia"]
    st.write(f"**{description}** died in the year ***{year}*** on {dateFetched}.")

    if bool(wikiLink):
        st.markdown("Learn More: " + wikiLink[0]['wikipedia'],)
    st.write("\n\n")

st.header("All major events that happened on "  + dateFetched)

requestString = 'https://byabbe.se/on-this-day/'+str(month_day_list[1])+'/'+str(month_day_list[0])+'/events.json'

# st.write(requestString)
x = requests.get(requestString)

# st.write(x.json())

y = x.json()

for item in y["events"]:
    description = item["description"]
    year = item["year"]
    wikiLink = item["wikipedia"]
    st.write(f"**{description}**. This happened in the year ***{year}*** on {dateFetched}.")

    if(bool(wikiLink)):
        st.markdown("Learn More: " + wikiLink[0]['wikipedia'],)
    st.write("\n\n")

st.header("All births that happened on "  + dateFetched)

requestString = 'https://byabbe.se/on-this-day/'+str(month_day_list[1])+'/'+str(month_day_list[0])+'/births.json'

# st.write(requestString)
x = requests.get(requestString)

# st.write(x.json())

y = x.json()

for item in y["births"]:
    description = item["description"]
    year = item["year"]
    wikiLink = item["wikipedia"]
    st.write(f"**{description}** was born in the year ***{year}*** on {dateFetched}.")

    if(bool(wikiLink)):
        st.markdown("Learn More: " + wikiLink[0]['wikipedia'],)
    st.write("\n\n")


if seeFullInformation:
    st.write(y)

if beingUsed:
    st.button("Re-run")

st.sidebar.info("Reload the page if an error appears.")

