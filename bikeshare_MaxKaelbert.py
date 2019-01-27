#Welcome to my bikeshare analytics tool!
# First step is to import the modules time, pandas & numpy.

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=["chicago", "new york city", "washington"]
months = ["january", "february", "march", "april", "may", "june"]
days=["sunday", "monday","tuesday","wednesday","thursday","friday","saturday"]
yesno=["yes", "no"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\nWe will start with 3 questions to get the right data for you ...')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Q1 - Which city do you like to explore: Chicago, New York City, or Washington?\n").lower()
    while city not in cities:
        print("You entered: {}. Sorry, but this city is not in our database. Please choose a Chicago, New York City, or Washington.".format(city.title()))
        city=input("One more try: Which city do you like to explore: Chicago, New York City, or Washington?\n").lower()
    else:
        print("Let\'s go and explore the data for: {}.".format(city.title()))


    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Q2 - For which month do you like to explore the data: january, february, march, april, may or june?\n").lower()
    while month not in months:
        print("You entered: {}. Sorry, but this month is not in our database.".format(month.title()))
        month=input("One more try: For which month do you like to explore the data: january, february, march, april, may or june?\n").lower()
    else:
        print("All right. Let\'s go and explore the data for: {}.".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Q3 - For which day do you like to explore the data: sunday, monday, tuesday, wednesday, thursday, friday or saturday?\n").lower()
    while day not in days:
        print("You entered: {}. Sorry, but this day is not real day, bro.".format(day.title()))
        day=input("One more try: For which day do you like to explore the data: sunday, monday, tuesday, wednesday, thursday, friday or saturday?\n").lower()
    else:
        print("All right. Let\'s go and explore the data for: {}.".format(day.title()))


    print("We will now fetch the data for\n city: {}\n month: {}\n day: {}".format(city, month, day))
    return city, month, day

##### WORKING :)


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
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    print('\nCalculating The Most Frequent Times of Travel ...\n')
    start_time = time.time()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("The most people need a bike around {} o'clock".format(popular_hour))

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station'] + " to " + df['End Station']
    combo = df['start_end'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("If you want to be mainstream, pic your bike here: {}".format(start_station))
    print("If you want to be mainstream, drop your bike here: {}".format(end_station))
    print("Most people love to ride from {}".format(combo))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    # TO DO: display mean travel time
    # new column with start and end station
    df['start_end'] = df['Start Station'] + " to " + df['End Station']
    # most frequent trip
    combo = df['start_end'].mode()[0]
    # dataframe just with trip_duration and the most frequent trip
    combo_df = df.loc[df['start_end'] == combo]
        #combo_df = df.loc[lambda df: df['start_end'] == combo]
    # mean of tour time for the most frequent trip
    tour_time = round(((combo_df['Trip Duration'].mean())/60),0)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("If you choose the tour from {}, {} minutes is the average time to beat ...".format(combo,tour_time))

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print("We think you would like to know some facts about your biking community ... \n Here are some details:")

    # TO DO: Display counts of user types
    count_ut = df['User Type'].value_counts()
    print("User types:\n {}".format(count_ut))

    # TO DO: Display counts of gender
    try:
        count_sex = df['Gender'].value_counts()
        print("Gender: {}".format(count_sex))
    # Error Massage
    except KeyError:
        print("Gender:\nThere is no data on the users' gender for Washington.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        early_birth = int(df['Birth Year'].min())
        recent_birth=int(df['Birth Year'].max())
        common_birth=int(df['Birth Year'].mode()[0])
        print('Birth years of Users:\nEarliest Year of Birth:{}'.format(early_birth))
        print('Most Recent Year of Birth: {}'.format(recent_birth))
        print('Most Common Year of Birth: {}'.format(common_birth))

    # Error Massage
    except KeyError:
        print("\nBirth Years:\nThere is no data on the users' years of birth for Washington.")



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
