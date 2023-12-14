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

import streamlit as st
from streamlit.logger import get_logger

import numpy as np
from typing import Any

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Introduction",
        page_icon="👋",
    )

    st.write("# This is the everything bagel.")

    st.sidebar.success("Select a function above.")

    st.markdown(
        """
        This a fun little application made to do a bunch of stuff that might be helpful. Inspired by Everything Everywhere All At Once.
        **Start interacting from the sidebar.** Reloading should help if in case any error happens.

        Project created with the help of [[streamlit.io]](https://streamlit.io), public APIs and other open source techonologies.
        #### About me
        Hi, I am Satyam [[website]](https://sudotman.github.io) [[mail]](mailto:satyamsudo@gmail.com)
    """
    )






if __name__ == "__main__":
    run()
