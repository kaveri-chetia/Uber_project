import pandas as pd
import numpy as np

def clean_data(df):
    """
    Cleans the DataFrame by handling missing values, extracting time-related features,
    and calculating the trip distance between pickup and dropoff locations.

    Parameters:
    df (pd.DataFrame): The input DataFrame to clean.

    Returns:
    pd.DataFrame: The cleaned DataFrame with additional features.
    """

    # 1. Handle missing values
    df = df.dropna()
    
    # 2. Convert pickup_datetime to datetime format
    df.loc[:, 'pickup_datetime'] = pd.to_datetime(df.loc[:, 'pickup_datetime'])
    
    # 3. Extract time-related features
    df.loc[:, 'Year'] = df['pickup_datetime'].apply(lambda time: time.year)
    df.loc[:, 'Month'] = df['pickup_datetime'].apply(lambda time: time.month)
    df.loc[:, 'Day of Week'] = df['pickup_datetime'].apply(lambda time: time.dayofweek)
    df.loc[:, 'Day of Week_num'] = df['pickup_datetime'].apply(lambda time: time.dayofweek)
    df.loc[:, 'Hour'] = df['pickup_datetime'].apply(lambda time: time.hour)
    
    # 4. Map day of the week to its name
    day_map = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}
    df['Day of Week'] = df['Day of Week'].map(day_map)
    
    # 5. Add a counter column
    df['counter'] = 1
    
    # 6. Define the Haversine function to calculate distance
    def haversine(lon1, lat1, lon2, lat2):
        R = 6371  # Radius of the Earth in kilometers
        dlon = np.radians(lon2 - lon1)
        dlat = np.radians(lat2 - lat1)
        a = np.sin(dlat / 2) ** 2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon / 2) ** 2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
        distance = R * c
        return distance
    
    # 7. Apply the Haversine function to calculate trip distance
    try:
        df['trip_distance_km'] = haversine(df['pickup_longitude'], df['pickup_latitude'], 
                                           df['dropoff_longitude'], df['dropoff_latitude'])
    except IndexError as e:
        print(f"IndexError: {e}")
    
    return df

# Example usage:
# cleaned_df = clean_data(raw_df)
