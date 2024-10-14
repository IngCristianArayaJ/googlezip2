import pandas as pd
import googlemaps
import time
import random

# Initialize Google Maps client (replace with your actual API key)
gmaps = googlemaps.Client(key='AIzaSyA6iqSMiZZjpIbm7IrgNN-3NE2KTIOzc3w')

# Function to get ZIP code based on address and city using Google Maps API
def get_zip_code(address, city):
    try:
        # Combine address and city for geocoding
        location = f"{address}, {city}"

        # Get location data from Google Maps Geocoding API
        geocode_result = gmaps.geocode(location)

        # Check if the geocode result contains data
        if geocode_result:
            # Extract ZIP code from the address components
            for component in geocode_result[0]['address_components']:
                if 'postal_code' in component['types']:
                    return component['long_name']
        return None
    except Exception as e:
        print(f"Error retrieving ZIP code for {address}, {city}: {e}")
        return None

# Function to process the uploaded file and add ZIP code
def process_file(file_path, output_file_path):
    # Load the data from the uploaded Excel file
    data = pd.read_excel(file_path)

    # Validate input data
    if not all(col in data.columns for col in ['PROP. ADDR', 'CITY']):
        raise ValueError("Input file must have 'PROP. ADDR' and 'CITY' columns.")

    # Create a new column 'ZIP' to store the fetched ZIP codes
    data['ZIP'] = data.apply(lambda row: get_zip_code(row['PROP. ADDR'], row['CITY']), axis=1)

    # Save the updated data to a new Excel file
    data.to_excel(output_file_path, index=False)

    return output_file_path

# Example usage:
# Assuming you've uploaded the file and it's saved at 'C:/Users/RYZEN 5 GAMER/Mina de Diamantes Dropbox/Cristian Araya/PC/Desktop/PropertySearch_data2/PropertySearch_data2.xlsx'
updated_file_path = process_file('C:/Users/RYZEN 5 GAMER/Mina de Diamantes Dropbox/Cristian Araya/PC/Documents/PropertySearch_data2/PropertySearch_data3.xls', 'output.xlsx')
print(f"New file with ZIP codes has been generated: {updated_file_path}")