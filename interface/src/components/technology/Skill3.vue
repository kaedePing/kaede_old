<template>
  <div class="skill3">
    <h1 style="margin-left: 40%">命令</h1>
    <ol style="margin-left: 2%">
      <li>
        <h2 id="Conda">Conda</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>创建虚拟环境</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">conda create -n myenv python=3.10.0</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>激活虚拟环境</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">conda activate myenv</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>退出虚拟环境</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">conda deactivate</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>删除虚拟环境</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">conda remove -n myenv --all</span></pre>
          </li>
        </ul>
      </li>
      <br>

      <li>
        <h2 id="Python">Python</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <h3>pip相关</h3>
            <ul style="list-style-type: square;margin-left: 2%">
              <li>
                <p>升级pip</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">pip install pip -U</span></pre>
              </li>
              <li>
                <p>设置数据源</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple</span></pre>
              </li>
            </ul>
          </li>

          <li style="margin-top: 5px">
            <h3>第三方库相关</h3>
            <ul style="list-style-type: square;margin-left: 2%">
              <li>
                <p>安装指定版本库</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">pip install django==3.2.9</span></pre>
              </li>
              <li>
                <p>卸载库</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">pip uninstall django</span></pre>
              </li>
              <li>
                <p>展示库相关信息</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">pip show django</span></pre>
              </li>
            </ul>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="Django">Django</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>创建项目</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">django-admin startproject server</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>创建应用</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">django-admin startapp movie</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>数据迁移</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">python manage.py makemigrations</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">python manage.py migrate</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>创建超级用户</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">python manage.py createsuperuser</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>启动服务器</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">python manage.py runserver</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>云服务器后台运行</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">nohup python manage.py runserver</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>局域网内可访问</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">python manage.py runserver 0.0.0.0:80</span></pre>
          </li>
        </ul>
      </li>
      <br>

      <li>
        <h2 id="server">服务器</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>重启Nginx</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">sudo /etc/init.d/nginx restart</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>关闭supervisord</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">supervisorctl shutdown</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>查看进程</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">ps aux|grep -i manage</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>杀掉进程</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">kill -9 pid</span></pre>
          </li>
        </ul>
      </li>
      <br>

      <li>
        <h2 id="Git">Git</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>创建ssh密匙</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">ssh-keygen -t rsa -C "flowerslanguage@126.com"</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>配置账户和邮箱</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git config --global user.name "kaede"</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git config --global user.email "flowerslanguage@126.com"</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>查看配置的账户和邮箱</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git config user.name</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git config user.email</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>初始化版本仓库</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git init</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>添加远程仓库</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">git remote add origin 地址</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>提交</p>
            <ul style="margin-left: 2%">
              <li style="margin-top: 5px">
                <p>工作区添加到暂存区</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">git add text.txt</span></pre>
              </li>
              <li style="margin-top: 5px">
                <p>暂存区提交到仓库</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">git commit -m "测试"</span></pre>
              </li>
              <li style="margin-top: 5px">
                <p>仓库推送到远程仓库</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">git push origin master</span></pre>
              </li>
            </ul>
          </li>
        </ul>
      </li>

      <li>
        <h2 id="ubuntu">Ubuntu</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>创建用户</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">adduser user</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>切换用户</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">su user</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>查询当前登录用户以及正在使用的进程</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">w</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>查看user用户在哪个组里面</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">groups user</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>查看有哪些组</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">sudo cat /etc/group</span></pre>
          </li>

        </ul>
      </li>

      <li>
        <h2 id="Vue">Vue</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>安装vue指定版本</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">npm install -g @vue/cli@3.10.0</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>默认最新版本</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">npm install -g @vue/cli</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>创建项目</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">vue create project</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>启动项目</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">npm run serve</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>打包项目</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">npm run build</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>‘vue-cli-service‘ 不是内部或外部命令，也不是可运行的程序 或批处理文件</p>
            <p>需要安装依赖</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">npm install --registry=https://registry.npm.taobao.org</span></pre>
          </li>

        </ul>
      </li>

      <li>
        <h2 id="Crontab">Crontab</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>/var/log下没有cron的日志</p>
            <p>在/etc/rsyslog.d/50-default.conf里将 # cron.*前的 # 去掉</p>
            <p>重启rsyslog服务</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">service rsyslog restart</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>重启cron服务</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">service cron restart</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>查看日志文件</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">tail -f /var/log/cron.log</span></pre>
          </li>

        </ul>
      </li>

      <li>
        <h2 id="Mysql">Mysql</h2>
        <p>版本8.0</p>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>root相关</p>
            <ul style="list-style-type: square;margin-left: 2%">
              <li style="margin-top: 5px">
                <p>root登录</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">mysql -uroot -p</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>更改root密码</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">alter user 'root'@'localhost' identified by '新密码';</span></pre>
              </li>
            </ul>
          </li>

          <li style="margin-top: 5px">
            <p>用户相关</p>
            <ul style="list-style-type: square;margin-left: 2%">
              <li style="margin-top: 5px">
                <p>创建用户</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">use mysql</span></pre>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">create user 'ping'@'localhost' identified by '123456';</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>对某用户授权</p>
                <ul style="list-style-type: square;margin-left: 2%">
                  <li style="margin-top: 5px">
                    <p>需要先修改host</p>
                    <pre contenteditable="TRUE" class="pre"><span
                        class="pre_span">update user set host='%' where user='ping';</span></pre>
                  </li>

                  <li style="margin-top: 5px">
                    <p>连着两次授权</p>
                    <pre contenteditable="TRUE" class="pre"><span
                        class="pre_span">grant all privileges on interface.* to 'ping'@'%';</span></pre>
                  </li>
                </ul>
              </li>

              <li style="margin-top: 5px">
                <p>删除用户</p>
                <ul style="list-style-type: square;margin-left: 2%">
                  <li style="margin-top: 5px">
                    <p>删除用户以及权限</p>
                    <pre contenteditable="TRUE" class="pre"><span
                        class="pre_span">drop user ping@'%';</span></pre>
                  </li>

                  <li style="margin-top: 5px">
                    <p>只删除用户，后续创建一个同样用户还会继承权限</p>
                    <pre contenteditable="TRUE" class="pre"><span
                        class="pre_span">delete from user where user='ping' and host='%';</span></pre>
                  </li>
                </ul>
              </li>

              <li style="margin-top: 5px">
                <p>查看所有用户</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">select user,host from mysql.user</span></pre>
              </li>
              <li style="margin-top: 5px">
                <p>查看某用户权限</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">show grants for 用户</span></pre>
              </li>

            </ul>
          </li>

          <li style="margin-top: 5px">
            <p>连接Navicat会报错，加密方式不一样</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">alter user ping identified with mysql_native_password by 'ping';</span></pre>
          </li>
        </ul>

      </li>

    </ol>
  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill3",
  data() {
    return {}
  },
  methods: {}
}
</script>


<style>
.skill3 {
  float: left;
  margin-left: 30%;
  width: 60%;
  /*height: 1000px;*/
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}


</style>