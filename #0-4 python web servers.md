def is_R_or_N(user_in_date=2017):
    value_r_n = (user_in_date % 4 == 0 and user_in_date % 100 != 0)\
    or user_in_date % 400 == 0
    return value_r_n

if is_R_or_N(2037):
    print(366)
else:
    print(365)

def get_mEnd_days(mEnd=12, is_R_N=True):
    totaldays =0
    if is_R_N:
        if mEnd == 12:
            totaldays = 30+31+30+31+31+31+30+31+30+31+29+31
        elif mEnd == 11:
            totaldays = 31+30+31+31+31+30+31+30+31+29+31
        elif mEnd == 10:
            totaldays = 30+31+31+31+30+31+30+31+29+31
        elif mEnd == 9:
            totaldays = 31+31+31+30+31+30+31+29+31
        elif mEnd == 8:
            totaldays = 31+31+30+31+30+31+29+31
        elif mEnd == 7:
            totaldays = 31+30+31+30+31+29+31
        elif mEnd == 6:
            totaldays = 30+31+30+31+29+31
        elif mEnd == 5:
            totaldays = 31+30+31+29+31
        elif mEnd == 4:
            totaldays = 30+31+29+31
        elif mEnd == 3:
            totaldays = 31+29+31
        elif mEnd == 2:
            totaldays = 29+31
        elif mEnd == 1:
            totaldays = 31
def get_mEnd_days(mEnd=12, is_R_N=False):
 totaldays = 0
 if mEnd == 12:
        totaldays = 30 + 31 + 30 + 31 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 11:
        totaldays = 31 + 30 + 31 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 10:
        totaldays = 30 + 31 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 9:
        totaldays = 31 + 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 8:
        totaldays = 31 + 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 7:
        totaldays = 31 + 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 6:
        totaldays = 30 + 31 + 30 + 31 + 28 + 31
 elif mEnd == 5:
        totaldays = 31 + 30 + 31 + 28 + 31
 elif mEnd == 4:
        totaldays = 30 + 31 + 28 + 31
 elif mEnd == 3:
        totaldays = 31 + 28 + 31
 elif mEnd == 2:
        totaldays = 28 + 31
 elif mEnd == 1:
        totaldays = 31

def getTotalDaysOneWholeYear(year=2017):
    if is_R_or_N(year):
        total = 366
    else:
        total = 365
    return total

def getBeforeYearsTotalDays(yEnd=2017):
    totaldays = 0
    years = range(1,yEnd)
    for year_every in years:
        if is_R_or_N(year_every):
            totaldays += 366
        else:
            totaldays += 365

def countDaysDiffer(dayStart='20180101',dayEnd="20170101"):
    yStart, mStart, dStart = int(dayStart[:4]),int(dayStart[4:6]),int(dayStart[6:8])
    yEnd, mEnd, dEnd = int(dayEnd[:4]),int(dayEnd[4:6]),int(dayEnd[6:8])
    print('dayStart:',yStart,mStart,dStart)
    print('dayEnd:',yEnd,mEnd,dEnd)
    EndDays =getBeforeYearsTotalDays(yEnd) + get_mEnd_days(mEnd, is_R_or_N(yEnd))+ dEnd
    StartDays = getBeforeYearsTotalDays(yStart ) + get_mEnd_days(mStart, is_R_or_N(yStart))+ dStart

