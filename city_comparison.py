import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data from the csv file that contains Indian city data
df = pd.read_csv('zomato_data_updated.csv')
df_india = df[df['Country'] == 'India']  # Filter to only include data from India

def main():
    st.title("City Comparison Report in India")



    if 'Cuisines' in df_india.columns and 'Converted Cost (INR)' in df_india.columns:
    # Grouping data by 'Cuisines' and calculating the average cost
        cuisine_costs = df_india.groupby('Cuisines')['Converted Cost (INR)'].mean().reset_index()

        # Sorting the cuisine costs from highest to lowest
        cuisine_costs_sorted = cuisine_costs.sort_values(by='Converted Cost (INR)', ascending=False)

        # Custom color scale based on #e03546
        color_scale = [
            [0, '#f8d7da'],   # lighter shade of #e03546
            [0.5, '#e03546'], # original color
            [1, '#a02735']    # darker shade of #e03546
        ]

        # Plotting the data
        fig = px.bar(cuisine_costs_sorted, x='Cuisines', y='Converted Cost (INR)',
                        title='Exploring the Expense: The Costliest Cuisines Across India',
                        labels={'Converted Cost (INR)': 'Average Cost (INR)', 'Cuisines': 'Cuisine'},
                        color='Converted Cost (INR)',
                        color_continuous_scale=color_scale)
        st.plotly_chart(fig)
    

    # Analysis for Online Delivery Spend
    if 'Has Online delivery' in df_india.columns and 'Converted Cost (INR)' in df_india.columns:
        online_spend = df_india[df_india['Has Online delivery'] == 'Yes'].groupby('City')['Converted Cost (INR)'].sum().reset_index()
        fig_online = px.bar(online_spend, x='City', y='Converted Cost (INR)', title='Regional Analysis of Online Delivery Spending in India',
                            color_discrete_sequence=["#e03546"])  # Setting the bar color
        st.plotly_chart(fig_online)
    
    # Analysis for Dine-In Spend
    if 'Has Online delivery' in df_india.columns and 'Converted Cost (INR)' in df_india.columns:
        dine_in_spend = df_india[df_india['Has Online delivery'] == 'No'].groupby('City')['Converted Cost (INR)'].sum().reset_index()
        fig_dine_in = px.bar(dine_in_spend, x='City', y='Converted Cost (INR)', title='Comparing Dine-In Spending by Region in India',
                             color_discrete_sequence=["#e03546"])  # Setting the bar color
        st.plotly_chart(fig_dine_in)

    
    # Hypothetical Living Cost Comparison using average dining cost as an indicator
    if 'Converted Cost (INR)' in df_india.columns:
        living_cost = df_india.groupby('City')['Converted Cost (INR)'].mean().reset_index()
        
        # Sorting the DataFrame by 'Converted Cost (INR)' in descending order
        living_cost = living_cost.sort_values(by='Converted Cost (INR)', ascending=False)
        fig_living_cost = px.bar(living_cost, x='City', y='Converted Cost (INR)', title='From High to Low: Mapping Living Costs Across India',
                                 color_discrete_sequence=["#e03546"])  # Setting the bar color
        st.plotly_chart(fig_living_cost)


if __name__ == '__main__':
    main()
