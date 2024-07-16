import streamlit as st
from city_analysis import main as city_based_analysis
from city_comparison import main as city_comparison
from country_analysis import main as country_based_analysis

st.set_page_config(page_title="Zomato Data Analysis", layout="wide")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a page:", ['City-Based Analysis', 'City Comparison', 'Country-Based Analysis'])

    if page == 'City-Based Analysis':
        city_based_analysis()
    elif page == 'City Comparison':
        city_comparison()
    elif page == 'Country-Based Analysis':
        country_based_analysis()

if __name__ == "__main__":
    main()
