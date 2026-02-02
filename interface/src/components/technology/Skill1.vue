<template>
  <div class="skill1">
    <h1 style="margin-left: 40%">Vue</h1>
    <ol style="list-style-type: none;margin-top: 2px">
      <li>
        <h2 id="storeToken">一.存储token</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          为了记录当前登录用户。使用LocalStorage管理状态。
          <a href="https://blog.csdn.net/kevinfan2011/article/details/95166073" target="_blank">参考</a>
        </p>
        <p style="text-indent: 2em;margin-top: 5px">
          使用步骤如下：
        </p>
        <p style="text-indent: 2em;margin-top: 5px">
          1.在Vue项目里创建一个store文件夹，与router文件夹同级，然后再在store里面创建index.js文件。state里面的内容就相当于变量，mutations里面函数设置变量的值，getters用于获取变量的值，其内容如下
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          2.在main.js里面导入store
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data2">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          3.使用store设置和获取token
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data3">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          4.关闭浏览器时清除LocalStorage，为了监测到关闭浏览器，写在App.vue的Script里面，与methods同级
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data4">{{ item }}</span></pre>
      </li>
      <br>

      <li>
        <h2 id="usingAxios">二.使用Axios</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          1.首先在main.js里引入Axios
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data5">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          2.发送get请求
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          3.发送post请求
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data7">{{ item }}</span></pre>
      </li>
      <br>

      <li>
        <h2 id="passingValuesBetweenComponents">三.不同组件之间传值</h2>
        <p style="text-indent: 2em;margin-top: 5px">
          1.首先在components文件夹里创建一个msg.js文件，填入以下内容
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data8">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          2.一个组件发送数据
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data9">{{ item }}</span></pre>
        <p style="text-indent: 2em;margin-top: 5px">
          3.一个组件接收数据
        </p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data10">{{ item }}</span></pre>

      </li>

    </ol>
  </div>
</template>

<script>
export default {
  name: "ComponentsTechnologySkill1",
  data() {
    return {
      data1: [
        'import Vue from \'vue\'',
        'import Vuex from \'vuex\'',
        '',
        'Vue.use(Vuex)',
        '',
        'export default new Vuex.Store({  // 用于管理状态',
        '    state: {',
        '        token: \'\',  //初始化token',
        '        userid: \'\'  //初始化用户id',
        '    },',
        '    mutations: {',
        '        //存储token方法',
        '        //设置token等于外部传递进来的值',
        '        setToken(state, token) {',
        '            state.token = token',
        '            localStorage.token = token //同步存储token至localStorage',
        '        },',
        '        setId(state, userid) {',
        '            state.userid = userid',
        '            localStorage.userid = userid //同步存储token至localStorage',
        '        },',
        '    },',
        '    getters: {',
        '        //获取token方法',
        '        //判断是否有token,如果没有重新赋值，返回给state的token',
        '        getToken(state) {',
        '            if (!state.token) {',
        '                state.token = localStorage.getItem(\'token\')',
        '            }',
        '            return state.token',
        '        },',
        '        getId(state) {',
        '            if (!state.userid) {',
        '                state.userid = localStorage.getItem(\'userid\')',
        '            }',
        '            return state.userid',
        '        }',
        '    },',
        '    actions: {}',
        '})',

      ],
      data2: [
        'import store from \'./store\'',
        '',
        'new Vue({',
        '  router,',
        '  store,',
        '  render: h => h(App)',
        '}).$mount(\'#app\')',

      ],
      data3: [
        'this.$store.commit(\'setToken\', _token);  // 将获取的token存入store管路的状态中',
        'this.$store.getters.getToken // 获取token',

      ],
      data4: [
        'mounted() {',
        '    // 关闭浏览器窗口的时候清空浏览器缓存在localStorage的数据',
        '    window.onbeforeunload = function (e) {',
        '      var storage = window.localStorage;',
        '      storage.clear()',
        '    }',
        '  },',

      ],
      data5: [
        'import axios from \'axios\'',
        '',
        'Vue.config.productionTip = false',
        'Vue.prototype.$http=axios',
      ],
      data6: [
        'let headers = {',
        '    \'Authorization\': \'Token \' + _this.$store.getters.getToken,',
        '    \'Content-Type\': \'application/json\'',
        '    }',
        '_this.$http.get(url, {headers: headers}).then(function (res) {',
        '    _this.result = res[\'data\'][\'results\']',
        '}).catch(function (error) {',
        '    console.log(error)',
        '})',
      ],
      data7: [
        'methods: {',
        '    getCookie(name) {  // 验证403错误',
        '      let value = \'; \' + document.cookie',
        '      let parts = value.split(\'; \' + name + \'=\')',
        '      if (parts.length === 2) return parts.pop().split(\';\').shift()',
        '    },',
        '    Login(formName) {  // 登录函数',
        '      let _user = this.ruleForm.user;',
        '      let _pass = this.ruleForm.pass;',
        '      let _this = this;',
        '      let _token;',
        '      let url = common.httpUrl',
        '      let data = {',
        '        \'username\': _user,',
        '        \'password\': _pass,',
        '      }  // 登录账号时需要的参数',
        '      _this.$http.post(url, data, {headers: {\'X-CSRFToken\': this.getCookie(\'csrftoken\')}}).then(function (res) {',
        '        _this.$message.success(\'登录成功\');',
        '        _token = res.data.token;  // 获取登录后取得的token',
        '      }).catch(error => {',
        '        _this.$message.error(\'请输入正确的账号或密码\')',
        '      })',
        '    }',
        '  }',

      ],
      data8: [
        'import Vue from \'vue\'',
        'export default new Vue',
      ],
      data9: [
        'import Msg from \'./msg.js\'',
        '',
        'export default {',
        '    methods: {',
        '        getNovel: function () {',
        '            Msg.$emit(\'type\', \'hot_novel\')  // 发送数据',
        '        }',
        '    }',
        '}',
      ],
      data10: [
        'mounted: function () {',
        '    // 接收数据',
        '    Msg.$on(\'type\', function (res) {',
        '        console.log(res)',
        '    })',
        '    Msg.$on(\'page\', function (url) {',
        '        console.log(url)',
        '    })',
        '}',

      ]
    }
  }
}
</script>

<style>
.skill1 {
  width: 60%;
  float: left;
  margin-left: 30%;
  box-shadow: #666 0px 0px 10px 0px;
  position: relative;
}

.pre {
  background: #303030;
  color: #f1f1f1;
  padding: 10px 16px;
  border-radius: 2px;
  border-top: 4px solid #00aeef;
  -moz-box-shadow: inset 0 0 10px #000;
  box-shadow: inset 0 0 10px #000;
  counter-reset: line;
  width: 96%;
}

.pre .pre_span {
  display: block;
  line-height: 1rem;
  position: relative;
  font-size: 1.2em;
}

.pre .pre_span::before {
  counter-increment: line;
  content: counter(line);
  display: inline-block;
  border-right: 1.5px solid #ddd;
  padding: 0 .5em;
  margin-right: .5em;
  color: #888;
  margin-left: 2px;
}
</style>