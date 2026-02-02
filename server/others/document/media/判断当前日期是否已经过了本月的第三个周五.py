import datetime


def get_week(date):
    week = datetime.date.weekday(date)
    week += 1
    week %= 7
    if week == 0:
        week = 7
    return week


def CheckDate(date):
    """
    求出当月所有星期五 然后比较当前日期是否大于第三个
    :param date:
    :return:
    """
    now_month = []  # 记录当前月份所有的周五
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])

    # 获取当前月所有的周五
    for i in range(1, 32):
        try:
            day1 = datetime.date(year=year, month=month, day=i)
            week1 = get_week(date=day1)
            if week1 == 5:
                now_month.append(str(year) + str(month).rjust(2, '0') + str(i).rjust(2, '0'))
        except:
            break
    array = [int(i) for i in now_month]
    temp = str(year) + str(month).rjust(2, '0') + str(day).rjust(2, '0')
    week = int(temp)
    for i in range(2, len(temp)):
        if week > array[i]:
            return True
        else:
            return False


date = '20180720'
print(CheckDate(date=date))
