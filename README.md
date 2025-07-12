### Conversation chatbot 
During this project, I have created a chatbot that has several key features: calculating, translating, telling the time, etc. 
- "Import streamlit as st" and "import re" is required since streamlit and the function rex is used for calculation and UI.
- st.session_state stores user - input values; if the value isn't saved in st.session_state, it refreshes and leaves it as blank.
- Prompt saves the user - input value and converts it to a response shown in UI.
- Eval () is used for converting str values to integers and adding/subtracting/dividing/multiplying them(for instance, '9' + '4') .
- From datetime import datetime is used for telling the time.
