import streamlit as st
import pandas as pd
import plotly.express as px

# Reading the dataframe
df = pd.read_csv('zomato_data_updated.csv')

# Streamlit app
def main():
    st.title("City based data analysis")

    # Dropdown for country selection
    selected_country = st.selectbox("Select Country", df['Country'].unique(), index=0)

    # Dropdown for city selection
    selected_city = st.selectbox("Select City", df[df['Country'] == selected_country]['City'].unique(), index=0)

    # Filter DataFrame based on user input
    filtered_df = df[(df['Country'] == selected_country) & (df['City'] == selected_city)]

    # Famous Cuisine in the City
    st.plotly_chart(px.bar(
        filtered_df['Cuisines'].value_counts().nlargest(10).reset_index(),
        x='Cuisines',
        y='count',
        title='Famous Cuisine in the City',
        labels={'index': 'Cuisine', 'Cuisines': 'Cuisines'}
    ))

    # Costlier Cuisine in the City
    st.plotly_chart(px.box(filtered_df.groupby('Cuisines').agg({'Converted Cost (INR)': 'mean'}).reset_index(),
                           x='Cuisines', y='Converted Cost (INR)', title='Costlier Cuisine in the City'))

    # Rating Count in the City
    st.plotly_chart(px.bar(filtered_df, x='Cuisines', y='Votes', title='Rating Count in the City', color='Aggregate rating'))

    # Pie Chart Online Delivery vs Dine-In
    st.plotly_chart(px.pie(filtered_df, names='Has Online delivery', title='Delivery Mode in the City'))

if __name__ == '__main__':
    main()
