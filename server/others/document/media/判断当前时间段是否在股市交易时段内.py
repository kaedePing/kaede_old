import datetime


def get_week(date):
    """
    传入日期参数判断当前是星期几
    :param date:
    :return:
    """
    week1 = datetime.date.weekday(date)
    week1 += 1
    week1 %= 7
    if week1 == 0:
        week1 = 7
    return week1


def get_trad_time():
    """
    获取所有的交易时间段
    :return:
    """
    result = []
    starts = ['00.00', '09.00', '10.30', '13.30', '21.00']
    ends = ['02.30', '10.15', '11.30', '15.00', '24.00']
    length = len(starts)
    for i in range(length):
        temp = starts[i].split('.')
        start = int(temp[0]) * 60 + int(temp[1])

        temp = ends[i].split('.')
        end = int(temp[0]) * 60 + int(temp[1])
        # temp = []
        # for j in range(start, end + 1):
        #     temp.append(j)
        result.append([start, end])
    return result


def distance(now_time, trad_time):
    """
    计算当前距离下一个交易时间段差多少分钟
    :param now_time:
    :param trad_time:
    :return:
    """
    for i in trad_time:
        if i[0] > now_time:
            temp = i[0] - now_time
            return temp
    return 0


def calc():
    now = datetime.datetime.now()
    week = get_week(now)  # 获取星期
    hour = datetime.datetime.now().hour  # 获取小时
    minute = datetime.datetime.now().minute  # 获取分钟

    # 获取所有的交易时间段
    trad_time = get_trad_time()

    # 获取当前时间是一天的第多少个分钟
    now_time = hour * 60 + minute

    # 首先处理特殊情况
    # 如果当前是星期6 凌晨那个时间段是交易时间 其它时间不是
    if week == 6:
        if trad_time[0][0] <= now_time <= trad_time[0][1]:
            print('在交易时间')
        else:
            print('不在交易时间')
            # 不在交易时间，则计算还需要多少到达交易时间
            temp = trad_time[-1][1] - now_time + 12 * 60 + trad_time[1][0]
            print('距离交易时间还剩{}分钟'.format(str(temp)))
    if week == 7:
        temp = trad_time[-1][1] - now_time + trad_time[1][0]
        print('距离交易时间还剩{}分钟'.format(str(temp)))
    if week == 1:
        if trad_time[0][0] <= now_time <= trad_time[0][1]:
            print('不在交易时间')
            # 不在交易时间，则计算还需多少到达
            temp = trad_time[1][0] - now_time
            print('距离交易时间还剩{}分钟'.format(str(temp)))
        else:
            flag = True
            for i in range(1, len(trad_time)):
                if trad_time[i][0] <= now_time <= trad_time[i][1]:
                    print('在交易时间')
                    flag = False
                    break
            if flag:
                temp = distance(now_time, trad_time.copy()[1:])
                print('距离交易时间还剩{}分钟'.format(str(temp)))
    if week in [2, 3, 4, 5]:
        flag = True
        for i in range(0, len(trad_time)):
            if trad_time[i][0] <= now_time <= trad_time[i][1]:
                print('在交易时间')
                flag = False
                break
        if flag:
            temp = distance(now_time, trad_time.copy())
            print('距离交易时间还剩{}分钟'.format(str(temp)))


if __name__ == '__main__':
    calc()
