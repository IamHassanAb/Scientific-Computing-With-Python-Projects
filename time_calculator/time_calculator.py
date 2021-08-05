def add_time(start, duration, day=False):

    days_of_week_dict = {"Monday":0, "Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    days_of_week_tup = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    meridiem_lst = ["AM", "PM"]

    no_of_days = 0
    index = 0

    [start, meridiem] = start.split()
    [SH, SM] = start.split(":")
    [DH, DM] = duration.split(":")
    TM = int(SM) + int(DM)
    TH = int(SH) + int(DH)

    if TM >= 60:
        TH+=1
        TM = TM%60

    no_of_12s = int(TH) // 12

    if meridiem == "PM" and no_of_12s >= 1:
        no_of_days = 1
    no_of_days = int(DH) // 24 + no_of_days

    ind = 0 if meridiem == "AM" else 1
    for i in range(no_of_12s):
        ind +=1
        if ind > 1:
            ind = 0

    if TH > 12:
        TH = TH%12
        if TH ==0:
            TH = 12

    #Setting Up index for the day_of_the week_tuple
    if day:
        args = day.lower()
        for j in days_of_week_dict:
            if j.lower() == args:
                index = int(days_of_week_dict[j]+no_of_days)%7

    #Formatting
    TM = str(TM).zfill(2) if TM < 10 else str(TM)
    new_time_01_arg = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]}, {days_of_week_tup[index]} ({no_of_days} days later)'''
    new_time_02_arg = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]}, {days_of_week_tup[index]} (next day)'''
    new_time_03_arg = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]}, {days_of_week_tup[index]}'''
    new_time_01 = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]} ({no_of_days} days later)'''
    new_time_02 = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]} (next day)'''
    new_time_03 = f'''{str(TH)}:{str(TM)} {meridiem_lst[ind]}'''

    if day:
        if no_of_days > 1:
            return new_time_01_arg
        elif no_of_days == 1:
            return new_time_02_arg
        else:
            return new_time_03_arg
    if no_of_days > 1:
        return new_time_01
    elif no_of_days == 1:
        return new_time_02
    else:
        return new_time_03