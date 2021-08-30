import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which one of these city would you like to explore: (Chicago, New York ,Washington)?').lower()
        if city not in ['chicago', 'new york', 'washington']:
            print('There is no data for this city, please enter the correct city name!')
         
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input('Which month do you want to explore the ' + city + ' city data: (January,February,March,April,May,June,or all)?').lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print('There is no data for ' + city + ' in this month, please select one of the months listed!')
            
        else:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day of week do you want to explore the ' + city + ' city data: (Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday, or all)?').lower()
        if day not in ['saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']:
            print('Please write the correct day name!')
 
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load cities data into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month, hour, and day of week from the 'Start Time' to create new columns 
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
       
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:", common_month)

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]
    print("The most common day of week is:", common_dow)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour is:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(start_station))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: {}".format(frequent_combination))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print("The total travel time in seconds is:", total_trip, "and in minutes is:", total_trip/60)
    
    # TO DO: display mean travel time
    trip_avg = df['Trip Duration'].mean()
    print("The average travel time in seconds is:" , trip_avg, "and in minutes is:", trip_avg/60)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types is:\n", user_types)
    
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print("The counts of each gender is:\n", gender)
        
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth {} \n The most recent year of birth {} \n The most common year of birth {}".format(earliest_year,recent_year,common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Asks user if they want to displays 5 lines of raw data."""
    raw_data = input('\nDo you want to see 5 lines of raw data?.\n')
    start_loc = 0
    while raw_data.lower() == 'yes':
        print(df.iloc[start_loc: start_loc+5])
        start_loc += 5
        raw_data = input('\nDo you want to see the next 5 rows of data?.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
