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
        labels={'index': 'Cuisine', 'Cuisines': 'Cuisines'},
        color_discrete_sequence=['#e03546']  # Setting bar color to red
    ))

    
    # Costlier Cuisine in the City
    st.plotly_chart(px.line(filtered_df.groupby('Cuisines').agg({'Converted Cost (INR)': 'mean'}).reset_index(),
                           x='Cuisines', y='Converted Cost (INR)', title='Costlier Cuisine in the City',
                           color_discrete_sequence=['#e03546']))

    
    # Rating Count in the City
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add bar for Votes
    fig.add_trace(
        go.Bar(x=cuisine_data['Cuisines'], y=cuisine_data['Votes'], name='Total Votes', marker_color='#e03546'),
        secondary_y=False,
    )

    # Add line for Aggregate Rating
    fig.add_trace(
        go.Scatter(x=cuisine_data['Cuisines'], y=cuisine_data['Aggregate rating'], name='Aggregate Rating', marker_color='#eeeeee'),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=f"Rating Count and Aggregate Rating for Each Cuisine in {selected_city}"
    )

    # Set x-axis title
    fig.update_xaxes(title_text="Cuisines")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Primary</b> Total Votes", secondary_y=False)
    fig.update_yaxes(title_text="<b>Secondary</b> Aggregate Rating", secondary_y=True)

    # Display the figure/chart
    st.plotly_chart(fig)

    
    # Prepare data for pie chart 
    delivery_counts = filtered_df['Has Online delivery'].value_counts().reset_index()
    delivery_counts.columns = ['Delivery Mode', 'Count']
    pie_fig = px.pie(delivery_counts, values='Count', names='Delivery Mode', title='Online Delivery vs Dine-In in ' + selected_city,
                         color='Delivery Mode', color_discrete_map={'Yes': '#e03546', 'No': '#21394f'})
    
    st.plotly_chart(pie_fig)

if __name__ == '__main__':
    main()
