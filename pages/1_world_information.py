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

st.set_page_config(page_title="world information", page_icon="📹")
st.markdown("# world's data")
st.sidebar.header("what do you want to see?")

seeFullInformation = st.sidebar.checkbox("see raw data? [debugging]")
sideBarSelectBox = st.sidebar.selectbox('select data to be fetched', ['Select One','Search any IP/e-mail/DNS','World Registered Domains','World Forex Rates','Indian Postal Codes'])

if sideBarSelectBox=='Select One':
    st.write(
        """This page consists various data fetching capabilities pertaining to the world (and in a few cases, India)."""
    )


beingUsed = False

if sideBarSelectBox!='Select One':
    beingUsed = True
    st.write("Currently on: " + sideBarSelectBox + "")

if sideBarSelectBox == 'Indian Postal Codes':  
    st.sidebar.write("Indian Pin codes and their corresponding information can be fetched for all the states!")

    pincode = st.number_input('Enter the pin code to lookup: ',8000,1000000,400001,1)

    if pincode>9000: 
        x = requests.get('https://api.postalpincode.in/pincode/'+str(pincode))
        y = x.json()

        st.write(y[0]["Message"])

        st.write(pd.DataFrame(y[0]["PostOffice"]))

        # st.write('Title: ' + y["title"])

        if seeFullInformation:
            st.write(y)

elif sideBarSelectBox == 'World Registered Domains':  
    st.sidebar.write("Search up for any registered domain on the world wide web to get their corresponding information.")

    domain = st.text_input("Enter the domain name here (e.g. facebook)")

    if domain!="":
        x = requests.get('https://api.domainsdb.info/v1/domains/search?domain='+domain)
        y = x.json()

        st.write('Total registered domains with this keyword: ' + str(y["total"]))
        st.write('Time taken to fetch these (ms): ' + str(y["time"]))

        st.write(pd.DataFrame(y["domains"]))

        # st.write('Title: ' + y["title"])

        if seeFullInformation:
            st.write(y)

elif sideBarSelectBox == 'World Forex Rates':  
    st.sidebar.write("See the latest forex exchange rates (base - EUR) [updated 16:00 CET every working day].")

    x = requests.get('https://api.frankfurter.app/latest')
    y = x.json()

    st.write('Base Currency: ' + str(y["base"]))
    st.write('Last Updated: ' + str(y["date"]))

    data = y["rates"]
    dataFrame = pd.Series(data).to_frame('Rate')
    st.write(dataFrame)

    # st.write('Title: ' + y["title"])

    if seeFullInformation:
        st.write(y)

elif sideBarSelectBox == "Search any IP/e-mail/DNS":
    st.sidebar.write("Search up for any IP address to get data associated with it - including city, region, and rough lat/longs.")

    ipType = st.radio("What information do you want to fetch?",[":rainbow[IP Address]", "Email ID", "Domain DNS","Who Is Domain"],captions = ["Search for any IP address e.g. 1.1.1.1.", "Search for an email id address e.g. example@gmail.com.", "Get DNS records for a domain. e.g. google.com.","Get who is data of a domain e.g. google.com"])

    domain = st.text_input("Enter the " + ipType +" here.")

    if domain!="":

        currentSwitch = "ip"

        if ipType == ":rainbow[IP Address]":
            currentSwitch = "ip"
        elif ipType == "Email ID":
            currentSwitch = "email"
        elif ipType == "Domain DNS":
            currentSwitch = "dns"
        elif ipType == "Who Is Domain":
            currentSwitch = "whois"
            
        x = requests.get('https://scraper.run/'+ currentSwitch +'?addr='+domain)
        y = x.json()

        st.write('Address: ' + domain)

        if ipType == "Domain DNS":
            data = y

            st.caption("IPs associated with the address: ")

            for item in y["ip"]:
                st.write(item)

            st.caption("txt/certificates: ")
            for item in y["txt"]:
                st.write(item)

            st.caption("mx (mail server): ")
            for item in y["mx"]:
                st.write(item)

            st.caption("domain: ")

            st.write(y["domain"])
            
            # st.write(pd.DataFrame(y))
        elif ipType == "Who Is Domain":
            data = y["domain"]

            data['status'] = ','.join(data['status'])
            
            data['name_servers'] = ','.join(data['name_servers'])

            st.caption("domain Information: ")
            dataFrame = pd.Series(data).to_frame('values')
            st.write(dataFrame)


            st.caption("registrar Information: ")

            data = y["registrar"]
            dataFrame = pd.Series(data).to_frame('values')
            st.write(dataFrame)


            st.caption("registrant Information: ")
            data = y["registrant"]
            dataFrame = pd.Series(data).to_frame('values')
            st.write(dataFrame)
        

            st.caption("administrative Information: ")

            data = y["administrative"]
            dataFrame = pd.Series(data).to_frame('values')
            st.write(dataFrame)
        

            st.caption("technical Information: ")
            data = y["technical"]
            dataFrame = pd.Series(data).to_frame('values')
            st.write(dataFrame)


        else:
            data = y
            dataFrame = pd.Series(data).to_frame('values')

            st.write(dataFrame)


        if seeFullInformation:
            st.write(y)

if beingUsed:
    st.button("Re-run")

st.sidebar.info("Reload the page if an error appears.")

