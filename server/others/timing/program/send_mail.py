# -*- coding: utf-8 -*-
# @Time : 2022/6/7 14:26
# @Author : kaede
# @File : send_mail.py
# @Software: PyCharm
# @contact: flowerslanguage@126.com
# -*- Description -*-
# 每日获取服务器接口数据表的内容，将其存为csv文件，发送到邮箱中，达到备份的目的
# -*- Description -*-

import datetime
import os
import logging
import pandas as pd
from sqlalchemy import create_engine
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 全局变量
files = []  # 存储需要发送哪些附件

# 常量
PATH = '/home/server/others/timing' + '/file/'  # 将下载的CSV保存在该文件下面

DATE = datetime.datetime.now().strftime('%Y%m%d')  # 当前备份的日期
MAILTO_LIST = ['2132321138@qq.com', '1798419176@qq.com']  # 收件人(列表)
MAIL_HOST = "smtp.126.com"  # 使用的邮箱的smtp服务器地址，这里是126的smtp地址(连接服务器的主机)
MAIL_USER = "flowerslanguage"  # 邮箱登录用户
MAIL_PASS = "IADGDSSCDFDHREIL"  # 邮箱登录密码 授权smtp后，这里的密码就是授权码
MAIL_POSTFIX = "126.com"  # 邮箱的后缀，126.com

DIALECT = 'mysql'  # 数据库类型
DRIVER = 'pymysql'  # 数据库驱动选择
USERNAME = 'root'  # 数据库用户名
PASSWORD = 'Ping.1235'  # 用户密码
HOST = '49.234.15.210'  # 服务器地址
PORT = '3306'  # 端口
DATABASE = 'kaede'  # 数据库

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s',
                    filemode='a',
                    filename='/home/server/others/timing/log/send_mail.txt')


def get_files():
    """
    1.首先明确哪些数据表需要做备份
    2.连接mysql数据库，通过pandas将数据表的内容写入csv文件中
    3.将备份的数据表的文件名写入files中做全局变量，方便后面作为附件发送
    :return:
    """
    tables = ['app_articles', 'app_books', 'app_documents', 'app_music_v1s', 'app_request_infos',
              'app_summaries']  # 存储需要备份的数据表
    # engine = create_engine('mysql+pymysql://root:Ping.1235@49.234.15.210:3306/kaede')
    engine = create_engine(
        DIALECT + '+' + DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE)  # 连接数据库
    for table in tables:
        sql = "select * from " + table  # 构建取哪张数据表的sql
        df = pd.read_sql_query(sql, engine)  # 通过pandas读取数据表内容同时转换为Dataframe对象
        df.to_csv(PATH + table + '.csv', encoding='utf-8_sig', index=False)  # 将数据表的内容存入csv中

    # 将需要备份的数据表名写入files中
    for file in tables:
        files.append(file + '.csv')


def send_mail():
    sender = "<" + MAIL_USER + "@" + MAIL_POSTFIX + ">"  # 发件人
    receivers = ";".join(MAILTO_LIST)  # 收件人 将收件人列表以‘；’分隔
    sub = DATE + "-服务器数据备份"  # 邮件标题

    # 邮件头部内容 主题 发送人 收件人
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = sender
    msg['To'] = receivers

    # 邮件正文内容
    msg.attach(MIMEText('这是一份备份服务器数据表的邮件', 'plain', 'utf-8'))

    # 附件内容
    for file in files:
        att1 = MIMEText(open(PATH + file, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="' + DATE + '_' + file + '"'
        msg.attach(att1)

    # 邮件连接参数
    server = smtplib.SMTP()
    server.connect(MAIL_HOST)  # 连接服务器
    server.login(MAIL_USER, MAIL_PASS)  # 登录操作
    server.sendmail(sender, MAILTO_LIST, msg.as_string())  # 文件
    server.close()


def main():
    """
    程序入口
    :return:
    """
    logging.debug('------------------------Start------------------------')
    logging.debug('Program start!')

    try:
        logging.debug('Start get_files function!')
        get_files()  # 将数据表的内容写入csv中
        logging.debug('End get_files function!')

        logging.debug('Start send_mail function!')
        send_mail()
        logging.debug('End send_mail function!')
    except Exception as e:
        logging.error(e)

    logging.debug('Program end!')
    logging.debug('------------------------End------------------------')


if __name__ == '__main__':
    main()
