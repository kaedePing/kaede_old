<template>
  <div class="skill5">
    <h1 style="margin-left: 40%">Python发送邮件</h1>
    <br>
    <div>
      <p style="text-indent: 2em;margin-top: 5px">
        系统中最重要的是数据。该博客使用sqlalchemy连接数据库，通过pandas直接将数据表中的内容写入CSV文件，
        最后通过邮件将其CSV当作附件发送给指定邮箱，达到备份的目的。
      </p>
      <p style="text-indent: 2em;margin-top: 5px">
        其主要分为两部分内容。get_files连接数据库将表中的内容写入CSV中；send_mail构造邮件内容，发送给指定用户即可。
      </p>
      <p style="text-indent: 2em;margin-top: 5px">
        需要注意的是下面的代码是通过126邮箱发送给其他邮箱，需要登录自己的126邮箱在设置中授权smtp后才可以使用
      </p>
      <br>
      <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{ item }}</span></pre>
    </div>
  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill5",
  data() {
    return {
      data1: ['import datetime',
        'import os',
        'import logging',
        'import pandas as pd',
        'from sqlalchemy import create_engine',
        'import smtplib',
        'from email.mime.multipart import MIMEMultipart',
        'from email.mime.text import MIMEText',
        '',
        '# 全局变量',
        'files = []  # 存储需要发送哪些附件',
        '',
        '# 常量',
        'PATH = os.getcwd() + \'\\file\\\'  # 将下载的CSV保存在该文件下面',
        '',
        'DATE = datetime.datetime.now().strftime(\'%Y%m%d\')  # 当前备份的日期',
        'MAILTO_LIST = [\'1798419176@qq.com\']  # 收件人(列表)',
        'MAIL_HOST = "smtp.126.com"  # 使用的邮箱的smtp服务器地址，这里是126的smtp地址(连接服务器的主机)',
        'MAIL_USER = "xxxxx"  # 邮箱登录用户 前缀即@前的内容',
        'MAIL_PASS = "xxxxx"  # 邮箱登录密码 授权smtp后，这里的密码就是授权码(需网页端登录邮箱进入设置修改)',
        'MAIL_POSTFIX = "126.com"  # 邮箱的后缀，126.com',
        '',
        'DIALECT = \'mysql\'  # 数据库类型',
        'DRIVER = \'pymysql\'  # 数据库驱动选择',
        'USERNAME = \'user\'  # 数据库用户名',
        'PASSWORD = \'password\'  # 用户密码',
        'HOST = \'180.76.144.127\'  # 服务器地址',
        'PORT = \'3306\'  # 端口',
        'DATABASE = \'interface\'  # 数据库',
        '',
        'logging.basicConfig(level=logging.DEBUG,',
        '                    format=\'%(asctime)s - %(filename)s[Line:%(lineno)d] - %(levelname)s %(message)s\',',
        '                    filemode=\'a\',',
        '                    filename=\'send_mail.txt\')  # filename就是logging的具体位置',
        '',
        '',
        'def get_files():',
        '    """',
        '    1.首先明确哪些数据表需要做备份',
        '    2.连接mysql数据库，通过pandas将数据表的内容写入csv文件中',
        '    3.将备份的数据表的文件名写入files中做全局变量，方便后面作为附件发送',
        '    :return:',
        '    """',
        '    logging.info(\'start get_files function!\')',
        '    tables = [\'movies\']  # 存储需要备份的数据表',
        '    # engine = create_engine(\'mysql+pymysql://user:password@180.76.144.127:3306/interface\')',
        '    engine = create_engine(',
        '        DIALECT + \'+\' + DRIVER + \'://\' + USERNAME + \':\' + PASSWORD + \'@\' + HOST + \':\' + PORT + \'/\' + DATABASE)  # 连接数据库',
        '    for table in tables:',
        '        sql = "select * from " + table  # 构建取哪张数据表的sql',
        '        df = pd.read_sql_query(sql, engine)  # 通过pandas读取数据表内容同时转换为Dataframe对象',
        '        df.to_csv(PATH + table + \'.csv\', encoding=\'gbk\', index=False)  # 将数据表的内容存入csv中',
        '',
        '    # 将需要备份的数据表名写入files中',
        '    for file in tables:',
        '        files.append(file + \'.csv\')',
        '',
        '',
        'def send_mail():',
        '    logging.info(\'start send_mail function!\')',
        '    sender = "<" + MAIL_USER + "@" + MAIL_POSTFIX + ">"  # 发件人',
        '    receivers = ";".join(MAILTO_LIST)  # 收件人 将收件人列表以‘；’分隔',
        '    sub = DATE + "-服务器数据备份"  # 邮件标题',
        '',
        '    # 邮件头部内容 主题 发送人 收件人',
        '    msg = MIMEMultipart()',
        '    msg[\'Subject\'] = sub',
        '    msg[\'From\'] = sender',
        '    msg[\'To\'] = receivers',
        '',
        '    # 邮件正文内容',
        '    msg.attach(MIMEText(\'这是一份备份服务器数据表的邮件\', \'plain\', \'utf-8\'))',
        '',
        '    # 附件内容',
        '    for file in files:',
        '        att1 = MIMEText(open(PATH + file, \'rb\').read(), \'base64\', \'utf-8\')',
        '        att1["Content-Type"] = \'application/octet-stream\'',
        '        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字',
        '        att1["Content-Disposition"] = \'attachment; filename="\' + DATE + \'_\' + file + \'"\'',
        '        msg.attach(att1)',
        '',
        '    # 邮件连接参数',
        '    server = smtplib.SMTP()',
        '    server.connect(MAIL_HOST)  # 连接服务器',
        '    server.login(MAIL_USER, MAIL_PASS)  # 登录操作',
        '    server.sendmail(sender, MAILTO_LIST, msg.as_string())  # 文件',
        '    server.close()',
        '    logging.info(\'overcome sending mail!\')',
        '',
        '',
        'if __name__ == \'__main__\':',
        '    get_files()  # 将数据表的内容写入csv中',
        '    send_mail()',
      ]
    }
  },
  methods: {}
}
</script>


<style>
.skill5 {
  float: left;
  margin-left: 5%;
  width: 60%;
  height: 1000px;
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}


</style>