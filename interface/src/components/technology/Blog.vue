<template>
  <div class="blog">
    <h1 style="margin-left: 40%">博客</h1>

    <ol STYLE="margin-left: 0.5%" style="list-style-type: none">
      <li>
        <ol>
          <h2 id="foreword">一.前言：</h2>
          <li style="list-style-type: none;">
            <br>
            <p style="text-indent: 2em;border-left: 10px solid #4cae4c">
              关于博客，作者大学是学习的C#,没有规范学习过前端和后端，只是用自学过的一些知识来融合开发的此博客。自学过Python，最初
              主要是做爬虫开发，现在从事的工作并不会使用到这些知识，由于不想遗忘，遂开发了此博客，主要介绍一些作者遇到的一些问题，
              和分享自己的日常。博客主要使用的技术是Vue和Python，以及后端框架Django，Vue做前端界面布局使用，使用Python来处理数据,
              Django用来当应用服务器做接口使用。整个网站部署使用Uabntu+Nginx+Supervisor+Gunicorn，部署完Django后，再使用其
              路由部署Vue项目，一个系统的流程就此完成。
            </p>
            <p style="text-indent: 2em;border-left: 10px solid #4cae4c">
              最后，欢迎各位大佬添加对我的博客文章进行指导，同时也欢迎加微信交友，说不定以后互相有需要了了。
            </p>
          </li>
        </ol>
      </li>
      <br>

      <li>
        <h2 id="technologyList">二.技术清单</h2>
        <ol style="margin-left: 2%">
          <br>
          <li>
            <p>
              前端：Vue3.11.0
            </p>
          </li>
          <li>
            <p>
              后端：Django3.2.9
            </p>
          </li>
          <li>
            <p>
              其他：Python3.10.0
            </p>
          </li>
        </ol>
      </li>
      <br>

      <li>
        <h2 id="systemRelease">三.系统发布</h2>
        <ol style="margin-left: 2%">
          <br>
          <li style="list-style-type: none">
            <p>
              Uabntu+Nginx+Supervisor+Gunicorn
            </p>
          </li>

        </ol>
      </li>
      <br>

      <li>
        <h2 id="problemSolving">四.难题解决</h2>
        <ol style="margin-left: 2%">
          <br>
          <li>
            <h3 id="crossDomainProblem">
              跨域问题：
            </h3>
            <p style="text-indent: 2em;">
              服务器开发完成后，前端就需要访问接口，遇到的问题，最初一直百度想让前端解决，但是一直行不通，
              最后还是在后端添加了配置解决了跨域问题。解决这个问题只需要在settings.py文件中添加如下三个内容
            </p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data1">{{ item }}</span></pre>
          </li>
          <br>

          <li>
            <h3 id="staticFileProblem">
              静态文件问题：
            </h3>
            <p style="text-indent: 2em;">
              静态文件包含三种类型。第一种就是Django接口自带的静态文件，在本地使用时不需要配置，部署后需要配置；
              第二种就是服务器开放给客户端的静态资源，比如图片等；
              第三种就是html模板的静态文件，比如Vue打包的项目、404页面等
            </p>
            <p style="text-indent: 2em;">
              Django配置静态文件分两种情况。第一种就是调试模式(开发环境)，该情况下通过Django配置进行静态文件的查找，但是就不能配置模板文件，比如404页面；
              第二种就是非调试模式(生产环境)，该情况下静态文件就不能通过Django来配置，此博客使用Nginx来配置非调试模式下的静态文件路径。
            </p>
            <p style="text-indent: 2em;">
              很好理解上面两种类型，当访问错误路由时，Django自带的404页面会抛出详细信息，方便开发者定位问题，这就是调试模式；
              用于实际生产的环境，用户如果访问了不存在的路径，是需要抛出一个自定义的错误信息即自定义404信息给用户，就不能返回调试模式下的详细错误信息，因为用户看不懂。
              下面分两种情况调试模式和非调试模式，对静态文件的配置进行详细说明。
            </p>
            <br>

            <div>
              <b>生成Django接口自带的静态文件</b>
              <p style="text-indent: 2em;">
                1.首先在settings.py文件下定义 STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
              </p>
              <p style="text-indent: 2em;">
                2.使用命令 python manage.py collectstatic
              </p>
              <p style="text-indent: 2em;">
                原理:他会在BASE_DIR目录(默认目录就是进入Django项目里面的第一级)下生成名叫collected_static的文件,
                里面的内容就是自带的Django接口的静态文件,后面建议统一使用 STATICFILES_DIRS 去包含静态文件路径,因为它可以
                定义包含多个静态文件路径,就不要使用 STATIC_ROOT
              </p>
              <p style="text-indent: 2em;">
                注意:Django自带的静态文件在本地不需要使用，但是部署后就需要使用其生成的静态文件
              </p>
            </div>

            <br>
            <ul style="list-style-type: disc; margin-left: 5px; margin-top: 2px">
              <li>
                <h5 style="font-size: 1em" id="debugMode">调试模式</h5>
                <p style="text-indent: 2em;">
                  设置Django项目中，settings.py文件里的DEBUG = True，就是调试模式。
                  下面是将三种静态文件分别放在不同的目录下面，为了方便我区分文件才这么做的，实际开发，静态文件最好放在一个目录下面
                </p>
                <br>
                <ol>
                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em;">只使用Django接口自带的静态文件</h6>
                    <p style="text-indent: 2em;">
                      注意:要使用Django接口自带的静态文件,必须修改 STATIC_URL为其他值,不能是原值(/static/)
                    </p>
                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data2">{{
                        item
                      }}</span></pre>
                  </li>

                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em">使用Django接口自带的静态文件+服务器部署的静态文件供客户端使用的静态文件</h6>
                    <p style="text-indent: 2em;">
                      注意:web/static就是开放给客户端访问的静态资源目录，客户端要访问该目录下的静态文件，直接使用 STATIC_URL(web)即可
                    </p>
                    <p style="text-indent: 2em;">
                      例如: ~/web/img/1.jpg 客户端通过 STATIC_URL(这里就是url里的web) 访问Django项目下的web/static/img/1.jpg文件
                    </p>
                    <p></p>
                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data3">{{
                        item
                      }}</span></pre>
                  </li>

                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em">使用Django接口自带的静态文件+服务器部署的静态文件供客户端使用的静态文件+模板文件(Vue项目、404页面)</h6>
                    <p style="text-indent: 2em;">
                      注意:要使用Vue项目，还需要在 TEMPLATES下,DIRS里填入 os.path.join(BASE_DIR, 'frontend') 内容,
                    </p>
                    <p style="text-indent: 2em;">
                      BASE_DIR表示Django项目目录第一级吗，整个含义表示将Django项目下的frontend文件目录放入模板中，
                      就可以访问里面的html，一般放的是Vue打包后生成的项目文件，即将Vue打包的整个文件放入frontend里面。
                    </p>
                    <p style="text-indent: 2em;">
                      Vue部署后要访问静态资源是通过 vue.config.js的assetsDir去找所有静态资源,而Django是通过STATIC_URL去访问静态资源，
                      因此它们两个里面的内容要相同，然后Django配置Vue的静态资源时，定位到Vue打包生成的静态文件即可
                    </p>
                    <p></p>
                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data4">{{
                        item
                      }}</span></pre>
                  </li>

                </ol>

              </li>
              <br>

              <li>
                <h5 style="font-size: 1em" id="non-debugMode">非调试模式</h5>
                <p style="text-indent: 2em;">
                  设置Django项目中，settings.py文件里的DEBUG = False，就是非调试模式。
                  下面是将三种静态文件都放在一个目录里面了，且只能都放在一个目录下面。
                </p>
                <p style="text-indent: 2em;">
                  注:DEBUG=False,则表示生产环境,Django项目一旦用于生产环境,则静态文件路由就不应该由Django去走了,需要第三方去配置,
                  比如Nginx;另外就是404页面也需要在非调试模式下,因为调试模式404是具体的错误信息,方便开发人员去查找处理错误信息
                  Nginx设置静态文件从 alias下面寻找,所有的静态文件都放在该目录下面
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data5">{{
                    item
                  }}</span></pre>

                <br>
                <ol>
                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em">只使用Django接口自带的静态文件</h6>
                    <p style="text-indent: 2em;">
                      注意:非调试模式 STATIC_URL保持原来的值
                    </p>
                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{
                        item
                      }}</span></pre>
                  </li>

                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em">使用Django接口自带的静态文件+服务器部署的静态文件供客户端使用的静态文件</h6>
                    <p style="text-indent: 2em;">
                      注意:开发的静态资源文件都放在Nginx配置的静态目录下即可

                    </p>
                    <p style="text-indent: 2em;">
                      通过 STATIC_URL(static)访问开放给客户端的静态文件
                      例如:~/static/img/1.jpg 通过static直接访问Nginx配置的静态目录下的img文件下的1.jpg文件
                    </p>
                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{
                        item
                      }}</span></pre>
                  </li>

                  <li style="margin-left: 10px">
                    <h6 style="font-size: 0.9em">使用Django接口自带的静态文件+服务器部署的静态文件供客户端使用的静态文件+模板文件(Vue项目、404页面)</h6>
                    <p style="text-indent: 2em;">
                      注意:将Vue打包生成的项目放在Nginx配置的静态目录下即可,同时需要重新定义TEMPLATES下的DIRS，改为 os.path.join(BASE_DIR,
                      'others/static'),~/others/static下面为Vue项目和404等html.以及所有的静态资源
                    </p>

                    <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data6">{{
                        item
                      }}</span></pre>
                  </li>

                </ol>

              </li>
            </ul>


          </li>
          <br>

          <li>
            <h3 id="VueAndDjangoJointDebugging">
              Vue与Django联调：
            </h3>
            <p style="text-indent: 2em;">
              通过Django设置模板加载Vue项目打包的文件，实现Django部署Vue；同时Vue访问Django接口数据，实现前后端的联调
            </p>
            <ul style="margin-left: 10px;list-style-type: disc;">
              <li>
                <h5 style="font-size: 1em" id="DjangoDeployVue">
                  Django部署Vue
                </h5>
                <p style="text-indent: 2em;">
                  1.首先Django需要设置模板加载Vue的html，在settings.py文件里，修改DIRS内容，定位到Vue的html即可
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data7">{{
                    item
                  }}</span></pre>
                <p style="text-indent: 2em;">
                  2.其次就是配置访问Vue项目静态资源的路径，参考
                  <a style="text-decoration: none" href="#staticFileProblem">静态文件问题</a>中的非调试模式，
                  需要注意的就是打包Vue项目时，vue.config.js文件里的 assetsDir需要与Django的 STATIC_URL对应，同时相应调整文件目录层级关系，按照要访问Django
                  的静态资源需要通过 STATIC_URL去寻找为基准，然后去调整相应静态资源目录即可实现。Vue项目可能不存在 vue.config.js，新建填入以下内容即可：
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data8">{{
                    item
                  }}</span></pre>
                <p style="text-indent: 2em;">
                  3.最后就是定义Django路由去加载Vue打包后的html，在urls.py文件填入以下内容
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data9">{{
                    item
                  }}</span></pre>
              </li>
              <br>

              <li>
                <h5 style="font-size: 1em" id="VueAccessDjango">
                  Vue访问Django
                </h5>
                <p style="text-indent: 2em;">
                  需要先解决
                  <a style="text-decoration: none" href="#crossDomainProblem">跨域问题</a>，请求可参考另一篇专门介绍
                  <a style="text-decoration: none" href="">Vue</a>
                  的博客
                </p>
                <p style="text-indent: 2em;">
                  1.get请求
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data10">{{
                    item
                  }}</span></pre>
                <p style="text-indent: 2em;">
                  2.post请求
                </p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data11">{{
                    item
                  }}</span></pre>
              </li>

            </ul>
          </li>


        </ol>
      </li>
      <br>


      <li>
        <h2 id="other">五.其它</h2>
        <ol style="margin-left: 2%">
          <br>
          <li style="list-style-type: none;color: #A30000">注意：开发过程调试过程中，需要注意一个缓存问题，
            比如修改了配置没有变化等，
            可尝试重启服务，清除浏览器数据等操作
          </li>
          <br>
          <li style="list-style-type: none">
            <a href="https://www.lylinux.net/" target="_blank">参考</a>
          </li>
        </ol>
      </li>


    </ol>
    <br>
    <div>

    </div>


  </div>
</template>

<script>

export default {
  name: "ComponentsTechnologyBlog",
  data() {
    return {
      data1: ['#INSTALLED_APPS下添加如下内容',
        '\'corsheaders\'',
        '\n',
        '#MIDDLEWARE下添加如下内容',
        '\'corsheaders.middleware.CorsMiddleware\'',
        '\n',
        '#最后在settings.py文件中添加如下内容',
        'CORS_ORIGIN_ALLOW_ALL = True '
      ],
      data2: [
        '# STATIC_URL = \'/web/\'  # STATIC_URL 修改为任意其他值',
        '# STATICFILES_DIRS = [',
        '#     os.path.join(BASE_DIR, "collected_static"),  # 当前条件下可以不用写这部分',
        '# ]',
      ],
      data3: [
        '# STATIC_URL = \'/web/\'  # STATIC_URL 修改为任意其他值',
        '# STATICFILES_DIRS = [',
        '#     os.path.join(BASE_DIR, "collected_static"),  # Django接口自带的静态文件路径',
        '#     os.path.join(BASE_DIR, "web/static"),  # 开放给客户端的静态资源目录',
        '# ]',

      ],
      data4: [
        '# STATIC_URL = \'/web/\'  # STATIC_URL 修改为任意其他值',
        '# STATICFILES_DIRS = [',
        '#     os.path.join(BASE_DIR, "collected_static"),  # Django接口自带的静态文件路径',
        '#     os.path.join(BASE_DIR, "web/static"),  # 开放给客户端的静态资源目录',
        '#     os.path.join(BASE_DIR, \'frontend/web\'),  # Vue项目打包生成的静态文件目录',
        '# ]',
      ],
      data5: [
        'location /static/ {',
        '     alias /home/server/file/static/;',
        '     expires max;',
        '     access_log        off;',
        '     log_not_found     off;',
        ' }',
      ],
      data6: [
        '# STATIC_URL = \'/static/\'',
      ],
      data7: [
        'TEMPLATES = [',
        '    {',
        '        \'BACKEND\': \'django.template.backends.django.DjangoTemplates\',',
        '        \'DIRS\': [os.path.join(BASE_DIR, \'file/static\')],  # 配置vue项目  frontend  file/static',
        '        \'APP_DIRS\': True,',
        '        \'OPTIONS\': {',
        '            \'context_processors\': [',
        '                \'django.template.context_processors.debug\',',
        '                \'django.template.context_processors.request\',',
        '                \'django.contrib.auth.context_processors.auth\',',
        '                \'django.contrib.messages.context_processors.messages\',',
        '            ],',
        '        },',
        '    },',
        ']',
      ],
      data8: ['module.exports = {',
        '    transpileDependencies: true,',
        '    publicPath: "./", // 公共路径(必须有的)',
        '    outputDir: "dist", // 输出文件目录',
        '    assetsDir: "static", //静态资源文件名称 ',
        '    lintOnSave: false,',
        '    productionSourceMap: false, //去除打包后js的map文件',
        '    devServer: { //启动项目在8080端口自动打开',
        '        open: true,',
        '        port: 8080,',
        '        proxy: null',
        '    },',
        '    //去掉console',
        '    configureWebpack: (config) => {',
        '        // 判断为生产模式下，因为开发模式我们是想保存console的',
        '        if (process.env.NODE_ENV === "production") {',
        '            config.optimization.minimizer.map((arg) => {',
        '                const option = arg.options.terserOptions.compress;',
        '                option.drop_console = true; // 打开开关',
        '                return arg;',
        '            });',
        '        }',
        '    },',
        '    configureWebpack: {',
        '        // 关闭 webpack 的性能提示',
        '        // performance: {',
        '        //   hints:false',
        '        // }',
        '',
        '        // //或者',
        '',
        '        // 警告 webpack 的性能提示',
        '        performance: {',
        '            hints: \'warning\',',
        '            // 入口起点的最大体积',
        '            maxEntrypointSize: 50000000,',
        '            // 生成文件的最大体积',
        '            maxAssetSize: 30000000,',
        '            // 只给出 js 文件的性能提示',
        '            assetFilter: function (assetFilename) {',
        '                return assetFilename.endsWith(\'.js\')',
        '            }',
        '        }',
        '    }',
        '};',
      ],
      data9: ['from django.urls import path',
        'from django.views.generic.base import TemplateView',
        '',
        'urlpatterns = [',
        '    path(\'\', TemplateView.as_view(template_name=\'index.html\'))  # 访问Vue项目',
        ']',
      ],
      data10: ['_this.$http.get(_this.url).then(function (res) {',
        '    _this.articles = res[\'data\'][\'results\']',
        '    // Msg.$emit(\'data\', _this.result)',
        '  }).catch(function (error) {',
        '    // _this.$message.error(\'请重新登录\')',
        '    console.log(error)',
        '    // _this.$router.push(\'/\')',
        '  })',
      ],
      data11: ['getCookie(name) {  // 验证403错误',
        '  let value = \'; \' + document.cookie',
        '  let parts = value.split(\'; \' + name + \'=\')',
        '  if (parts.length === 2) return parts.pop().split(\';\').shift()',
        '},',
        'Login(formName) {  // 登录函数',
        '    let _user = this.ruleForm.user;',
        '    let _pass = this.ruleForm.pass;',
        '    let _this = this;',
        '    let _token;',
        '    let data = {',
        '      \'username\': _user,',
        '      \'password\': _pass,',
        '    }  // 登录账号时需要的参数',
        '    _this.$http.post(url, data, {headers: {\'X-CSRFToken\': this.getCookie(\'csrftoken\')}}).then(function (res) {',
        '      console.log(res.data)',
        '    }).catch(error => {',
        '      _this.$message.error(\'请输入正确的账号或密码\')',
        '    })',
        '}',
      ]

    }
  }
}
</script>

<style>
.blog {
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