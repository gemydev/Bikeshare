import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("\nSelect city... (chicago , new york city or washington)\n")
        if city not in ('chicago', 'new york city', 'washington'):
            print("Make sure to input and Try again...")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "\nSelect month... (january, february, march, april, may, june or all)\n")
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Make sure to input and Try again...")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(
            "\nSelect day... (sunday, monday, tuesday, wednesday, thursday, friday, saturday or all)\n")
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Make sure to input and Try again...")
            continue
        else:
            break

    print('-' * 40)
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
    df['day_of_week'] = df['Start Time'].dt.day

    # filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

        # filter by day of week
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        day = days.index(day) + 1
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day:', most_common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most common used start station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most common used end station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df.groupby(['Start Station', 'End Station']).count()
    print('The most common used combination of start and end stations trip:', start_station, " & ", end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = sum(df['Trip Duration'])
    print('Total travel time:', total_travel_time / 86400, " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time / 60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # user_types = df['User Type'].value_counts()
    # print(user_types)
    # print('User Types:\n', user_types)
    try:
        user_types = df['User Type'].value_counts()
        print('User types:\n', user_types)
    except KeyError:
        print("\nUser types: There is no data for this month.")

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender types:\n', gender_types)
    except KeyError:
        print("\nGender types: There is no data for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year:', earliest_year)
    except KeyError:
        print("\nEarliest Year:\nThere is no data for this month.")

    try:
        most_recent_year = df['Birth Year'].max()
        print('The most recent year:', most_recent_year)
    except KeyError:
        print("The most recent year:\nThere is no data for this month.")

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('The most common year:', most_common_year)
    except KeyError:
        print("The most common year:\nThere is no data for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
