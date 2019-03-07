import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#df1 = pd.read_csv("chicago.csv")
#df2 = pd.read_csv("washington.csv")
#df3 = pd.read_csv("new_york_city.csv")
#df = pd.concat([df1,df2,df3])

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            cities = ['chicago', 'new york city', 'washington']
            city = str(input("\nWould you like to see data for Chicago, New York City, or Washington?\n"))
            city = city.lower()
            if city in cities:
                break
            else:
                print("The city you have entered is incorrect. please check it and try again.")
                continue
        except:
            print("Sorry! I didn't understand that...")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
            month = str(input("\nWhich month - January, February, March, April, May, June or all?\n"))
            month = month.lower()
            if month in months:
                break
            else:
                print("The month you have entered is incorrect. Please enter the correct one.")
                continue
        except:
            print("Sorry! I didn't understand that...")
            continue
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
            day = str(input("\n Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n"))
            day = day.lower()
            if day in days:
                break
            else:
                print("The day you have entered is incorrect. Please try again..")
                continue
        except:
            print("Sorry! I didn't understand that...")
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

    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month

    df["day_of_week"] = df["Start Time"].dt.weekday_name

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        df = df[df['month'] == month]

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]
        print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("\nThe most common month: \n",popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nThe most common day: \n",popular_day)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['start_hour'] = df['Start Time'].dt.hour
    popular_hour = df['start_hour'].mode()[0]
    print("\nThe most common hour: \n",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station: \n",popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("\nThe most popular end station: \n",popular_end_station)

    # display most frequent combination of start station and end station trip
    df['start_end'] = df['Start Station']+' and '+df['End Station']
    popular_start_end = df['start_end'].mode()[0]
    print("\nThe most frequent combination of start and end station: \n",popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("\nThe total travel time(in secs): \n",total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe mean travel time(in secs): \n",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type_counts = df['User Type'].value_counts()
    print("\nCounts of user types: \n",user_type_counts)

    # Display counts of gender
    if city == 'washington':
        print("\nThe data for gender and year of birth are not provided in the csv files of the washington city.")
    else:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of gender: \n',gender_count)


    # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("\nEarlist year of birth: \n",int(earliest_year))

        recent_year = df['Birth Year'].max()
        print("\nMost recent year of birth: \n",int(recent_year))

        popular_birth_year = df['Birth Year'].mode()
        print("\nMost common year of birth: \n",int(popular_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    a = 0
    b = 5
    while True:
        try:
            opinion = input("\nDo you want to look at the first five lines of your data? Type 'yes' or 'no'?\n")
            opinion = opinion.lower()
            if opinion == 'yes':
                print(df.iloc[a:b])
                while True:
                    try:
                        opinion = input("\nWould you like to look at more data? type 'yes' or 'no'?\n")
                        opinion = opinion.lower()
                        if opinion == 'yes':
                            a+=5
                            b+=5
                            print(df.iloc[a:b])
                            break
                        elif opinion == 'no':
                            break
                    except:
                        print("\nSorry!! I didn't understand....")
                        continue
                    else:
                        break
                break
            elif opinion == 'no':
                break
        except:
            print("\nSorry!! I didn't understand....")
            continue
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        # Display five lines of data at a time if user specifies that they would like to
        display(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
