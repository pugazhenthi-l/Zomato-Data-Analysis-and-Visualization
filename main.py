import streamlit as st
from city_analysis import main as city_based_analysis
from city_comparison import main as city_comparison
from country_analysis import main as country_based_analysis

st.set_page_config(page_title="Zomato Data Analysis", layout="wide")

def main():
    st.title("Zomato Data Analysis Dashboard")

    # Setup button-based tab navigation
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("City-Based Analysis"):
            st.session_state['current_page'] = 'city_based_analysis'
    with col2:
        if st.button("City Comparison"):
            st.session_state['current_page'] = 'city_comparison'
    with col3:
        if st.button("Country-Based Analysis"):
            st.session_state['current_page'] = 'country_based_analysis'

    # Display the appropriate page based on the current state
    if st.session_state.get('current_page', 'city_based_analysis') == 'city_based_analysis':
        city_based_analysis()
    elif st.session_state['current_page'] == 'city_comparison':
        city_comparison()
    elif st.session_state['current_page'] == 'country_based_analysis':
        country_based_analysis()

if __name__ == "__main__":
    main()
