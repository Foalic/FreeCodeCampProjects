## Project assignment asks to assume the inputs are valid times, and that the
#  duration minutes will be under 60.

def add_time(start, duration, weekday=None):

    colon_start = start.find(':')
    colon_duration = duration.find(':')

    ## Parsing and calculating the minutes and hours and days to add from duration
    minutes_start = int(start[colon_start+1:colon_start+3])
    minutes_duration = int(duration[colon_duration+1:])
    hours_duration = int(duration[:colon_duration])

    # if minutes_start >= 60:
    #     return "Time must be entered in '00:00 am/pm' format and minutes cannot be above 59."

    minutes_total = minutes_start + minutes_duration
    minutes_final_int = minutes_total % 60
    if minutes_final_int < 10:
        minutes_final_str = '0' + str(minutes_final_int)
    else:
        minutes_final_str = str(minutes_final_int)

    hours_from_mins = minutes_total // 60
    hours_to_add = (hours_duration + hours_from_mins) % 24

    days_to_add = (hours_duration + hours_from_mins) // 24


    ## Parse hours, change to 24 hour format
    hours_start_12 = start[:colon_start]

    start_insensitive = start.lower()
    if 'am' in start_insensitive:
        if hours_start_12 == '12':
            hours_start_24 = 0
        else:
            hours_start_24 = int(hours_start_12)
    elif 'pm' in start_insensitive:
        if hours_start_12 == '12':
            hours_start_24 = int(hours_start_12)
        else:
            hours_start_24 = int(hours_start_12) + 12
    # else:
    #     return "Time must be given in '00:00 am/pm' format."


    ## Add hours to start time
    hours_total = hours_start_24 + hours_to_add
    hours_final_24 = hours_total % 24
    days_final = days_to_add + (hours_total // 24)

    ## Convert back to 12 hour
    if hours_final_24 > 12:
        hours_final_12 = hours_final_24 - 12
    else:
        if hours_final_24 == 0:
            hours_final_12 = 12
        else:
            hours_final_12 = hours_final_24

    ## Decide on am or pm
    if hours_final_24 >= 12 and hours_final_24 < 24:
        time_of_day = 'PM'
    else:
        time_of_day = 'AM'

    ## Get the weekday that the final time arrives on
    dict_weekdays = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    if weekday != None:
        days_to_shift_within_week = days_final % 7
        for key,value in dict_weekdays.items():
            if value.lower() == weekday.lower():
                weekday_current_key = key
                break
        weekday_final_key = (weekday_current_key + days_to_shift_within_week) % 7
        weekday_final = dict_weekdays.get(weekday_final_key)


    ## Final time
    if weekday == None:
        time_without_day_count = str(hours_final_12) + ':' + minutes_final_str + ' ' + time_of_day
    else:
        time_without_day_count = str(hours_final_12) + ':' + minutes_final_str + ' ' + time_of_day + ', ' + weekday_final

    if days_final == 0:
        new_time = time_without_day_count
    elif days_final == 1:
        new_time = time_without_day_count + ' (next day)'
    elif days_final > 1:
        new_time = time_without_day_count + f' ({days_final} days later)'


    return new_time
