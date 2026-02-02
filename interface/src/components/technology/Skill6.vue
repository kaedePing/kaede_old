<template>
  <div class="Skill6">
    <h1 style="margin-left: 40%">python操作mysql</h1>
    <br>
    <div>
      <p style="text-indent: 2em;margin-top: 5px">
        使用pandas读取csv内容，以及pymysql连接mysql，然后构造插入数据表的sql即可，详情见代码
      </p>
      <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{ item }}</span></pre>
    </div>

  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill6",
  data() {
    return {
      data1: ['import pymysql',
        'import pandas as pd',
        '',
        '',
        'def getcon(db_name):',
        '    """',
        '    连接数据库，获取与mysql的连接以及游标',
        '    :param db_name: 数据库名字',
        '    :return: 连接对象 游标',
        '    """',
        '    # host是选择连接哪的数据库localhost是本地数据库，port是端口号默认3306',
        '    # user是使用的人的身份，root是管理员身份，passwd是密码。db是数据库的名称，charset是编码格式',
        '    conn = pymysql.connect(host="localhost", port=3306, user=\'root\', passwd=\'Kaede\', db=db_name, charset=\'utf8\')',
        '    # 创建游标对象',
        '    cursor1 = conn.cursor()',
        '    return conn, cursor1',
        '',
        '',
        'def insertData(db_name, table_name):',
        '    """',
        '    1.首先获取csv文件的内容',
        '    2.获取需要插入的列名，注意需要排查id字段，因为mysql自增',
        '    3.在for循环里，读取每行的值，拼接成sql语句，最后执行提交即可',
        '    :param db_name: 数据库名',
        '    :param table_name: 表名',
        '    :return: 连接对象 游标',
        '    """',
        '    # 调用链接到mysql的函数，返回我们的conn和cursor1',
        '    conn, cursor1 = getcon(db_name)',
        '    # 使用pandas 读取csv文件',
        '    df = pd.read_csv(\'documents.csv\')',
        '    # 使用for循环遍历df，是利用df.values，但是每条数据都是一个列表',
        '    # 使用counts计数一下，方便查看一共添加了多少条数据',
        '    columns = df.columns',
        '    columns = list(columns)  # 获取列名',
        '    columns.remove(\'id\')  # 不需要插入id字段 自增',
        '    field = \',\'.join(columns)  # 拼接需要插入的字段名',
        '    counts = 0  # 记录条数',
        '    for i in df.values:',
        '        value = i',
        '        value = list(value)  # 转换为list对象，方便处理',
        '        value.remove(value[0])  # 移出id那列的值',
        '        value = [\'"\' + str(k) + \'"\' for k in value]  # 将值转换为字符串并在前后添加"',
        '        value = \',\'.join(value)',
        '        sql = \'insert into \' + table_name + \'(\' + field + \')\' + \' values(\' + value + \');\'',
        '        print(sql)',
        '        cursor1.execute(sql)',
        '        # data = cursor1.fetchall()  # 读取sql执行查询的内容',
        '        # 提交sql语句执行操作',
        '        conn.commit()',
        '        # 没提交一次就计数一次',
        '        counts += 1',
        '    print(\'成功添加了\' + str(counts) + \'条数据 \')',
        '    return conn, cursor1',
        '',
        '',
        'def main(db_name, table_name):',
        '    """',
        '    主函数，执行完毕后需要关闭游标以及与mysql的连接',
        '    :param db_name: 数据库',
        '    :param table_name: 表名',
        '    :return:',
        '    """',
        '    conn, cursor1 = insertData(db_name, table_name)',
        '    # 当添加完成之后需要关闭我们的游标，以及与mysql的连接',
        '    cursor1.close()',
        '    conn.close()',
        '',
        '',
        '# 判断一下，防止再次在其他文件调用当前函数的时候会使用错误，多次调用',
        'if __name__ == \'__main__\':',
        '    main(\'kaede\', \'documents_copy1\')',
      ]
    }
  },
  methods: {}
}
</script>


<style>
.Skill6 {
  float: left;
  margin-left: 10%;
  width: 60%;
  height: 1000px;
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}


</style>