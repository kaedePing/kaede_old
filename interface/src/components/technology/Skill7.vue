<template>
  <div class="Skill7">
    <h1 style="margin-left: 40%">html</h1>
    <ol style="margin-left: 2%">
      <li>
        <h2 id="table">表格</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>实例</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{
                item
              }}</span></pre>

            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data2">{{
                item
              }}</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>table属性</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data3">{{
                item
              }}</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>td属性</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data4">{{
                item
              }}</span></pre>
          </li>


        </ul>
      </li>
      <br>

      <li>
        <h2 id="unorderedList">无序列表</h2>
        <p>实例</p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data5">{{
            item
          }}</span></pre>
      </li>
      <br>

      <li>
        <h2 id="orderedList">有序列表</h2>
        <p>实例</p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{
            item
          }}</span></pre>
      </li>
      <br>

      <li>
        <h2 id="customList">自定义列表</h2>
        <p>实例</p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data7">{{
            item
          }}</span></pre>
      </li>
      <br>

      <li>
        <h2 id="form">表单</h2>
        <ul style="list-style-type: disc;margin-left: 2%">
          <li>
            <p>form属性</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data8">{{
                item
              }}</span></pre>
          </li>

          <li>
            <p>input标签</p>
            <ul style="list-style-type: disc;margin-left: 2%">
              <li>
                <p>text(文本框) password(密码框)</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data9">{{
                    item
                  }}</span></pre>
              </li>

              <li>
                <p>radio(单选框) checkbox(复选框)</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data10">{{
                    item
                  }}</span></pre>
              </li>
              <li>
                <p>placeholder="请输入查询条件" 提示文本</p>
              </li>
            </ul>
          </li>

          <li>
            <p>label标签</p>
            <p>
              用于绑定一个表单元素，当点击标签内的文本时，浏览器会自动聚焦转到对应的表单元素上，增加用户体验
              label的for属性要等于目标表单元素的id
            </p>
          </li>

          <li>
            <p>select标签</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data11">{{
                item
              }}</span></pre>
          </li>

          <li>
            <p>textarea标签(文本框)</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data12">{{
                item
              }}</span></pre>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="emmet">emmet语法</h2>
        <p style="margin-left: 2%">一些生成html的快捷语法</p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data13">{{
            item
          }}</span></pre>
      </li>
      <br>

      <!--      下面是html的实例代码之类的-->
      <li>
        <h2 id="someHtmlExamples">一些html实例</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <span id="someHtmlExamplesForm">表单
              <a :href="url_form" target="_blank" style="text-decoration: none">点我查看效果</a>
            </span>
            <p>以下是示例完整代码</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data14">{{
                item
              }}</span></pre>
          </li>
          <br>

          <li style="margin-top: 5px">
            <span id="someHtmlExamplesTable">表格
              <a :href="url_table" target="_blank" style="text-decoration: none">点我查看效果</a>
            </span>
            <p>以下是示例完整代码</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data15">{{
                item
              }}</span></pre>
          </li>
          <br>

          <li style="margin-top: 5px">
            <span id="someHtmlExamplesWhole">完整示例
              <a :href="url_whole" target="_blank" style="text-decoration: none">点我查看效果</a>
            </span>
            <p>以下是示例完整代码</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data16">{{
                item
              }}</span></pre>
          </li>

        </ul>
      </li>
      <br>

    </ol>
  </div>
</template>


<script>
import common from "@/components/common/common";

export default {
  name: "ComponentsTechnologySkill7",
  data() {
    return {
      url_form: common.httpUrl + '/static/example/html/form.html',
      url_table: common.httpUrl + '/static/example/html/table.html',
      url_whole: common.httpUrl + '/static/example/html/whole.html',
      data1: ['<table border="1">',
        '    <tr>',
        '        <th>表头</th>',
        '        <th>表头</th>',
        '    </tr>',
        '    <tr>',
        '        <td>单元格</td>',
        '        <td>单元格</td>',
        '    </tr>',
        '</table>',
      ],
      data2: ['tr: 一行',
        'th: 表头',
        'td: 单元格内容',
      ],
      data3: ['align: 居中',
        'border: 边框',
        'cellpadding: 单元格内文字与边框的距离',
        'cellspacing: 单元格之间的距离',
      ],
      data4: ['colspan: 列合并',
        'rowspan: 行合并',
      ],
      data5: ['<ul>',
        '  <li>苹果</li>',
        '  <li>香蕉</li>',
        '  <li>葡萄</li>',
        '</ul>',
      ],
      data6: ['<ol>',
        '  <li>苹果</li>',
        '  <li>香蕉</li>',
        '  <li>葡萄</li>',
        '</ol>',
      ],
      data7: ['<dl>',
        '  <dt>水果</dt>',
        '  <dd>香蕉</dd>',
        '  <dd>苹果</dd>',
        '  <dd>葡萄</dd>',
        '</dl>',
      ],
      data8: ['action:表单提交的地址',
        'method:提交方法 get post',
        'name:',
      ],
      data9: ['name:方便后端取值',
        'value:实际取值(可以设置默认值)',
        'maxlength:最大输长度入',
      ],
      data10: ['name:方便后端取值(都需要这个值且同一组取一样的名称)',
        'value:实际取值(可以设置默认值)',
        'checked:默认值(checked)',
      ],
      data11: ['selected="selected"设置默认值',
        '<select name="select" id="">',
        '    <option value="四川">四川</option>',
        '    <option value="" >河南</option>',
        '    <option value="">河北</option>',
        '    <option value="">上海</option>',
        '    <option value="" selected="selected">浙江</option>',
        '</select>',
      ],
      data12: ['<textarea name="" id="textarea" cols="30" rows="10">',
        '    时间的追逐者',
        '</textarea>',
      ],
      data13: ['div*3     生成3个div',
        'ul>li     生成父子级标签',
        'div+p     生成兄弟级标签',
        '.demo$*5  生成五个div,且class依次递增的demo+数字',
        'p.s$*4    生成4个p,且class依次递增的s+数字',
      ],
      data14: ['<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <title>Title</title>',
        '</head>',
        '<body>',
        '<form action="https://translate.google.cn/" method="get" name="name1">',
        '    用户名: <input type="text" name="username" value="222" maxlength="5">',
        '    <br>',
        '    密 码: <input type="password" name="password">',
        '',
        '    <br>',
        '    单选框: 男 <input type="radio" name="sex" value="男" checked="checked"> 女 <input type="radio"  name="sex" value="女">',
        '    <br>',
        '    复选框: 吃饭 <input type="checkbox" name="checkbox" value="吃饭" checked="True"> 睡觉 <input checked="True" type="checkbox" name="checkbox" value="睡觉">',
        '    <br>',
        '',
        '    <input type="reset">',
        '    <br>',
        '    <input type="submit" value="免费提交">',
        '    <br>',
        '    <input type="button" value="获取验证码">',
        '    <br>',
        '    <input type="file" name="file">',
        '    <br>',
        '',
        '    <label for="sex1">男</label>',
        '    <input type="radio" name="sex1" id="sex1">',
        '    <br>',
        '',
        '    <select name="select" id="">',
        '        <option value="四川">四川</option>',
        '        <option value="" >河南</option>',
        '        <option value="">河北</option>',
        '        <option value="">上海</option>',
        '        <option value="" selected="selected">浙江</option>',
        '    </select>',
        '    <br>',
        '',
        '    <textarea name="" id="textarea" cols="30" rows="10">',
        '        时间的追逐者',
        '    </textarea>',
        '',
        '',
        '</form>',
        '</body>',
        '</html>',
      ],
      data15: ['<html>',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <meta name="viewport"',
        '          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">',
        '    <meta http-equiv="X-UA-Compatible" content="ie=edge">',
        '    <title>测试</title>',
        '</head>',
        '<body>',
        '<table align="center" border="1" cellpadding="20" cellspacing="0">',
        '    <thead>',
        '        <tr>',
        '            <th>排名</th>',
        '            <th>关键词</th>',
        '            <th>趋势</th>',
        '            <th>今日搜索</th>',
        '            <th>最近七日</th>',
        '            <th>相关链接</th>',
        '        </tr>',
        '    </thead>',
        '    <tbody>',
        '        <tr>',
        '            <td>1</td>',
        '            <td>鬼吹灯</td>',
        '            <td>1</td>',
        '            <td>345</td>',
        '            <td>123</td>',
        '            <td>',
        '                <a href="">贴吧</a>',
        '                <a href="">图片</a>',
        '                <a href="">百科</a>',
        '            </td>',
        '        </tr>',
        '        <tr>',
        '            <td>2</td>',
        '            <td>盗墓笔记</td>',
        '            <td>1</td>',
        '            <td>124</td>',
        '            <td>675432</td>',
        '            <td>',
        '                <a href="#">贴吧</a>',
        '                <a href="#">图片</a>',
        '                <a href="#">百科</a>',
        '            </td>',
        '        </tr>',
        '    </tbody>',
        '</table>',
        '<table border="1">',
        '    <tr>',
        '        <th>表头</th>',
        '        <th>表头</th>',
        '    </tr>',
        '    <tr>',
        '        <td>单元格</td>',
        '        <td>单元格</td>',
        '    </tr>',
        '</table>',
        '',
        '</body>',
        '</html>',
      ],
      data16: ['<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '    <meta charset="UTF-8">',
        '    <title>Title</title>',
        '</head>',
        '<body>',
        '<div>',
        '    <h2>愿不负韶华</h2>',
        '</div>',
        '<div>',
        '    <form action="https://translate.google.cn/" method="get">',
        '        <table width="500" border="0" align="center" cellpadding="2" cellspacing="0">',
        '            <tr>',
        '                <td>性别</td>',
        '                <td>',
        '                    <input type="radio" name="sex" value="male" id="male" checked="checked"> <label for="male">男</label>',
        '                    <input type="radio" name="sex" value="female" id="female"><label for="female">女</label>',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>生日</td>',
        '                <td>',
        '                    <select name="year" id="year">',
        '                        <option value="0">--请选择年--</option>',
        '                        <option value="1997">1997</option>',
        '                        <option value="1998">1998</option>',
        '                        <option value="1999">1999</option>',
        '                        <option value="2000">2000</option>',
        '                    </select>',
        '                    <select name="month" id="month">',
        '                        <option value="0">--请选择月--</option>',
        '                        <option value="1">1</option>',
        '                        <option value="2">2</option>',
        '                        <option value="3">3</option>',
        '                        <option value="4">4</option>',
        '                    </select>',
        '                    <select name="day" id="day">',
        '                        <option value="1">1</option>',
        '                        <option value="2">2</option>',
        '                        <option value="3">3</option>',
        '                        <option value="4">4</option>',
        '                        <option value="0" selected>--请选择日--</option>',
        '                    </select>',
        '',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>所在地区</td>',
        '                <td>',
        '                    <input type="text" value="四川成都" maxlength="20">',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>婚姻状况</td>',
        '                <td>',
        '                    <input type="radio" name="status1" value="未婚"> 未婚',
        '                    <input type="radio" name="status1" value="已婚" checked> 已婚',
        '                    <input type="radio" name="status1"> 离婚',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>学历</td>',
        '                <td>',
        '                    <input type="text" value="学士">',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>喜欢的类型</td>',
        '                <td>',
        '                    <input type="checkbox" name="status2"> 狐媚的',
        '                    <input type="checkbox" name="status2"> 可爱的',
        '                    <input type="checkbox" name="status2"> 小鲜肉',
        '                    <input type="checkbox" name="status2"> 老腊肉',
        '                    <input type="checkbox" name="status2"> 都喜欢',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td>自我介绍</td>',
        '                <td>',
        '                    <textarea name="textarea" id="textarea" cols="30" rows="10">这是自我介绍',
        '                    </textarea>',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td></td>',
        '                <td>',
        '                    <input type="submit" value="免费注册">',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td></td>',
        '                <td>',
        '                    <input type="radio" name="status3" checked>我同意注册条款和会员加入标准',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td></td>',
        '                <td>',
        '                    <a href="http://49.234.15.210/">我是会员，立即登录</a>',
        '                </td>',
        '            </tr>',
        '            <tr>',
        '                <td></td>',
        '                <td>',
        '                    <dl>',
        '                        <dt><strong>我承诺</strong></dt>',
        '                        <dd>年满18岁、单身</dd>',
        '                        <dd>抱着严肃的态度</dd>',
        '                        <dd>真诚寻找另一半</dd>',
        '                    </dl>',
        '                </td>',
        '            </tr>',
        '        </table>',
        '    </form>',
        '</div>',
        '',
        '</body>',
        '</html>',
      ]
    }
  },
  methods: {},
  components: {
    common
  }
}
</script>


<style>
.Skill7 {
  float: left;
  margin-left: 30%;
  width: 60%;
  /*height: 1000px;*/
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}


</style>