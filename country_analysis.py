import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset
df = pd.read_csv('zomato_data_updated.csv')

# Streamlit application definition
def main():
    st.title("Cuisine and Restaurant Analysis by Country")

    # Selection of country via dropdown
    selected_country = st.selectbox("Select Country", df['Country'].unique(), index=0)

    # Data filtering based on country selection
    filtered_data = df[df['Country'] == selected_country]


    # Chart 1: Cuisine Sales and Ratings Analysis 

    # Preparing data for the combined chart
    sales_data = filtered_data.groupby('Cuisines')['Converted Cost (INR)'].sum().reset_index()
    rating_data = filtered_data.groupby('Cuisines')['Aggregate rating'].mean().reset_index()

    # Creating a figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Adding bar chart for sales
    fig.add_trace(
        go.Bar(x=sales_data['Cuisines'], y=sales_data['Converted Cost (INR)'],
               name='Total Sales', marker_color='#e03546'),
        secondary_y=False,
    )

    # Adding line chart for ratings
    fig.add_trace(
        go.Scatter(x=rating_data['Cuisines'], y=rating_data['Aggregate rating'],
                   name='Average Rating', marker_color='#eeeeee', mode='lines+markers'),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=f"Total Sales and Average Ratings by Cuisine in {selected_country}"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Cuisines")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Primary</b> - Total Sales (INR)", secondary_y=False)
    fig.update_yaxes(title_text="<b>Secondary</b> - Average Rating", secondary_y=True)

    # Plot the figure
    st.plotly_chart(fig)

    # Chart 2: Cuisine Ratings Overview
    rating_data = filtered_data.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
    rating_chart = px.scatter(rating_data, x='Cuisines', y='Aggregate rating', size='Aggregate rating',
                              color='Aggregate rating', color_continuous_scale=px.colors.sequential.Reds,
                              title=f'Cuisine Ratings Overview in {selected_country}', hover_data=['Cuisines'])
    st.plotly_chart(rating_chart)

    # Chart 3: Total Restaurant Sales in Selected Country
    sales_data = filtered_data.groupby('Restaurant Name')['Converted Cost (INR)'].sum().reset_index()
    sales_chart = px.bar(sales_data, x='Restaurant Name', y='Converted Cost (INR)', title=f'Total Restaurant Sales in {selected_country}',
                         color_discrete_sequence=["#e03546"])
    st.plotly_chart(sales_chart)


    # Chart 4: Comparative Analysis of Rating vs. Cost
    cost_rating_chart = px.scatter(filtered_data, x='Converted Cost (INR)', y='Aggregate rating',
                                   hover_data=['Restaurant Name', 'Cuisines'],
                                   color='Aggregate rating', size='Aggregate rating',
                                   title='Comparative Analysis of Rating vs. Cost in Restaurants',
                                   labels={'Converted Cost (INR)': 'Converted Cost (INR)', 'Aggregate rating': 'Aggregate Rating'},
                                   color_continuous_scale=px.colors.sequential.Reds)
    st.plotly_chart(cost_rating_chart)

    # Chart 5: Highlighting the Best Restaurant
    # Sorting by highest rating and most reasonable cost
    best_restaurant = filtered_data.sort_values(by=['Aggregate rating', 'Average Cost for two'], ascending=[False, True]).head(1)
    if not best_restaurant.empty:
        st.subheader("Highlight of the Best Restaurant Based on Rating and Cost Efficiency:")
        st.write(best_restaurant[['Restaurant Name', 'Cuisines', 'Aggregate rating', 'Average Cost for two']])
    else:
        st.write("No data available for the selected country in the criteria specified.")

if __name__ == '__main__':
    main()
