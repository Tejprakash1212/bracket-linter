import streamlit as st
from parser import check_brackets

st.set_page_config(
    page_title="Bracket Linter PDA",
    layout="wide"
)

st.title("Bracket Linter using PDA")

st.write("""
This project demonstrates:

- Pushdown Automata
- Context Free Grammar
- Stack-based Parsing
- Real-time Bracket Checking
""")

code = st.text_area(
    "Enter your code",
    height=300
)

if code:

    errors = check_brackets(code)

    if len(errors) == 0:

        st.success("Balanced Brackets")

    else:

        st.error("Bracket Errors Found")

        for err in errors:

            st.write(err)