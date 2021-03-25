## Project assignment asks to assume the inputs are valid times, and that the
#  duration minutes will be under 60.

def add_time(start, duration, weekday=None):

    colon_start = start.find(':')
    colon_duration = duration.find(':')

    # Get new minutes in string type
    minutes_start = int(start[colon_start+1:colon_start+3])
    minutes_duration = int(duration[colon_duration+1:])
    minutes_total = minutes_start + minutes_duration
    minutes_final_str = get_final_minutes(minutes_total)

    # Get hours and days to add later
    hours_duration = int(duration[:colon_duration])
    hours_from_mins = minutes_total // 60
    hours_to_add = (hours_duration + hours_from_mins) % 24
    days_to_add = (hours_duration + hours_from_mins) // 24

    # Get hours for new time in 12-hour format
    hours_start_24 = convert_12_to_24_hour(start, colon_start)
    hours_total = hours_start_24 + hours_to_add
    hours_final_24 = hours_total % 24
    hours_final_12 = convert_24_to_12_hour(hours_final_24)

    ## Final time - Main Function
    time_of_day = get_am_pm(hours_final_24)
    days_final = days_to_add + (hours_total // 24)

    if weekday == None:
        time_without_day_count = str(hours_final_12) + ':' + minutes_final_str + ' ' + time_of_day
    else:
        weekday_final = get_new_weekday(weekday, days_final)
        time_without_day_count = str(hours_final_12) + ':' + minutes_final_str + ' ' + time_of_day + ', ' + weekday_final

    if days_final == 0:
        return time_without_day_count
    elif days_final == 1:
        return time_without_day_count + ' (next day)'
    elif days_final > 1:
        return time_without_day_count + f' ({days_final} days later)'



def get_final_minutes(minutes_total):
    minutes_final_int = minutes_total % 60

    if minutes_final_int < 10:
        return '0' + str(minutes_final_int)
    return str(minutes_final_int)


def convert_12_to_24_hour(start, colon_start):
    start_insensitive = start.lower()
    hours_start_12 = start[:colon_start]

    if 'am' in start_insensitive:
        if hours_start_12 == '12':
            return 0
        return int(hours_start_12)
    elif 'pm' in start_insensitive:
        if hours_start_12 == '12':
            return int(hours_start_12)
        return int(hours_start_12) + 12


def convert_24_to_12_hour(hours_final_24):
    if hours_final_24 > 12:
        return hours_final_24 - 12
    else:
        if hours_final_24 == 0:
            return 12
        return hours_final_24

def get_am_pm(hours_final_24):
    if hours_final_24 >= 12 and hours_final_24 < 24:
        return 'PM'
    return 'AM'

def get_new_weekday(weekday, days_final):
    dict_weekdays = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    days_to_shift_within_week = days_final % 7

    for key,value in dict_weekdays.items():
        if value.lower() == weekday.lower():
            weekday_current_key = key
            break

    weekday_final_key = (weekday_current_key + days_to_shift_within_week) % 7
    return dict_weekdays.get(weekday_final_key)
