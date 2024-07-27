import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    try:
        data = pd.read_csv('zomato_data_updated.csv')  # Ensure the correct path
        return data
    except FileNotFoundError:
        print("Error: 'zomato_data_updated.csv' file not found.")
        return pd.DataFrame()

def analyze_data(data):
    if 'Cuisines' not in data.columns:
        print("Error: 'Cuisines' column not found in data.")
        return pd.DataFrame(columns=['Cuisines', 'count'])

    cuisine_counts = data['Cuisines'].value_counts().reset_index()
    cuisine_counts.columns = ['Cuisines', 'count']
    return cuisine_counts

def visualize_data(cuisine_counts):
    if cuisine_counts.empty:
        print("Error: No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(cuisine_counts['Cuisines'], cuisine_counts['count'])
    plt.xlabel('Cuisines')
    plt.ylabel('Count')
    plt.title('Cuisine Counts in Zomato Data')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('cuisine_counts.png')  # Save the plot as an image file

def main():
    data = load_data()
    cuisine_counts = analyze_data(data)
    visualize_data(cuisine_counts)

if __name__ == '__main__':
    main()

