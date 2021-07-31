import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
      city = input("Please enter a city?/n New York City, Chicago or Washington?")
      city = city.lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("SORRY, I could not get your input.")
        continue
      else:
        break
        


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Please enter a month?/n (all, january, february, ... , june)/n")
      month = month.lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("SORRY, I could not get your input.")
        continue
      else:
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Please enter a day in the week?/n 'Sunday', 'Monday', 'Tuesday',....., 'Saturday', 'all'/n")
      day = day.lower()
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("SORRY, I could not get your input.")
        continue
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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt


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
        df = df = df[df['day_of_week'] == day.title()]
    
    return df
    
        #df = load_data('chicago', 'march', 'friday')
  
        #return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)
   

    # TO DO: display the most common day of week
    popular_day = df['month'].mode()[0]
    print('Most Frequent week:', popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour 
    popular_hour = df["hour"].mode()[0]
    print('Most Common Hour:', popular_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
          #done......


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('Most Frequent start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_station = df['End Station'].mode()[0]
    print('Most Frequent end station:', End_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    combination = df['combination'].mode()[0]
    print('Most frequently used stations:{}'.format(combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    #done....
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_t_time = df['Trip Duration'].sum()
    print("total travel time is:{} days".format(total_t_time))

    # TO DO: display mean travel time
    

    average_time = df['total_t_time'].mean()
    print("the mean of the travel time is:{} minutes".format(average_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

          #done......

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:{}'.format(user_types))

    # TO DO: Display counts of gender
    
    

    try:
      gender_counts  = df['Gender'].value_counts()
      print('gender_counts:{}'.format(gender_counts))
    except KeyError:
      print("\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth
          
          #earliest year
    try:
      earliest_Year =max(df['Birth Year'].value_counts())
      print('Earliest Year:{}'.format(earliest_Year))  
    except KeyError:
      print("\nNo data available for this month.")
    
    
          #most recent year
    try:
      recent_Year = min(df['Birth Year'])
      print('most recent Year is :{}'.format(recent_Year))
    except KeyError:
      print("\nNo data available for this month.")
          
          
          #common year
    try:
      common_year = max(df['Birth Year'])
      print('most common year is:{}'.format(common_year))
    except KeyError:
      print("\nNo data available for this month.")
          
                    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  
  	main()
