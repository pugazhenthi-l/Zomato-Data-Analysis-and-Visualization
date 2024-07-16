import streamlit as st
import pandas as pd
import plotly.express as px

# Reading the dataframe
df = pd.read_csv('zomato_data_updated.csv')

# Streamlit app
def main():
    st.title("Country based data analysis")

    # Dropdown for country selection
    selected_country = st.selectbox("Select Country", df['Country'].unique(), index=0)

    # Filter DataFrame based on user input
    filtered_df = df[df['Country'] == selected_country]

    # Cuisine Analysis
    st.plotly_chart(px.bar(filtered_df, x='Cuisines', title='Cuisine Analysis'))

    # Ratings Analysis - Restaurant-wise
    st.plotly_chart(px.bar(filtered_df, x='Restaurant Name', y='Aggregate rating', title='Ratings Analysis'))

    # Delivery Services
    st.plotly_chart(px.pie(filtered_df.drop_duplicates(subset=['Restaurant Name']), names='Has Online delivery', title='Delivery Services'))

    # Cost Analysis using Converted Cost (INR)
    st.plotly_chart(px.box(filtered_df.groupby('Cuisines').agg({'Converted Cost (INR)': 'mean'}).reset_index(),
                           x='Cuisines', y='Converted Cost (INR)', title='Cost Analysis'))

    # Find the most costly cuisine
    most_costly_cuisine = filtered_df.groupby('Cuisines')['Converted Cost (INR)'].mean().idxmax()

    st.write(f'The most costly cuisine in {selected_country} is "{most_costly_cuisine}"')

if __name__ == '__main__':
    main()
