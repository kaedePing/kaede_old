<template>
  <div class="skill4">
    <h1 style="margin-left: 40%">Django部署流程</h1>
    <br>
    <ol style="margin-left: 2%">
      <li style="margin-top: 5px">
        <p>列出所有可更新的软件清单命令</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt update</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>一键升级</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt upgrade -y</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>安装进程管理器supervisor</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt install supervisor -y</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>安装nginx</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt install nginx -y</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>安装miniconda3</p>
        <ul style="list-style-type: square;margin-left: 2%">
          <li>
            <p>与Anaconda类似，但只包含了Conda软件包管理器和Python以及相关依赖性，因此miniconda3适合服务器的安装。
              创建一个文件夹用来单独放下载的安装包</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">mkdir ubuntu</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">cd ubuntu</span></pre>
          </li>

          <li>
            <p>下载最新的miniconda3</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh</span></pre>
          </li>

          <li>
            <p>安装miniconda3</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">bash ./Miniconda3-latest-Linux-x86_64.sh</span></pre>
          </li>

          <li>
            <p>激活conda</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">source ~/.bashrc</span></pre>
          </li>

          <li>
            <p>配置conda数据源</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">cd /root</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">touch .condarc</span></pre>
            <p>填入以下内容</p>
            <pre contenteditable="TRUE" class="pre"><span v-for="item in data1"
                                                          class="pre_span">{{ item }}</span></pre>
          </li>

          <li>
            <p>刷新配置</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">source ~/.bashrc</span></pre>
          </li>

          <li>
            <p>清除下源记录</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">conda clean -i</span></pre>
          </li>

        </ul>
      </li>

      <li style="margin-top: 5px">
        <p>创建python虚拟环境</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">conda create -n myenv python=3.10.0</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>激活虚拟环境</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">conda activate myenv</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>升级pip</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip install pip -U</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>设置pip数据源</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>自行安装相关库即可</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip install django==3.2.9</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>通过requirements安装</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip install -r requirements.txt</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>安装Mysql</p>
        <p>查看最新的APT源(https://dev.mysql.com/downloads/repo/apt/)</p>
        <ul style="list-style-type: square;margin-left: 2%">
          <li>
            <p>下载</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">cd ubuntu</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb</span></pre>
          </li>

          <li>
            <p>安装</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb</span></pre>
          </li>

          <li>
            <p>更新</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">sudo apt update</span></pre>
          </li>

          <li>
            <p>安装mysql-server</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">sudo apt install mysql-server</span></pre>
          </li>

          <li>
            <p>登录mysql</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">mysql -uroot -p</span></pre>
          </li>

          <li>
            <p>授权</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">use mysql;</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">update user set host='%' where user='root';</span></pre>
          </li>

          <li>
            <p>刷新</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">flush privileges;</span></pre>
          </li>

          <li>
            <p>创建数据库</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">create database server</span></pre>
          </li>

          <li>
            <p>退出</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">exit;</span></pre>
          </li>

        </ul>
      </li>

      <li style="margin-top: 5px">
        <p>安装mysqlclient</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip install mysqlclient</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>解决安装mysqlclient失败问题</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt-get install python-dev default-libmysqlclient-dev</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt-get install python3 python-dev python3-dev</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt-get install build-essential libssl-dev libffi-dev</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo apt-get install libxml2-dev libxslt1-dev zlib1g-dev</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>设置Django项目 settings文件对于连接数据库的配置</p>
        <pre contenteditable="TRUE" class="pre"><span class="pre_span" v-for="item in data2">{{ item }}</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>简单的启动Django</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">python manage.py makemigrations</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">python manage.py migrate</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">python manage.py runserver</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>启动如果没有错误前面就算顺利进行，接下来停掉项目，配置GUNICORN</p>
        <p>安装GUNICORN</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">pip install gunicorn</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>创建gunicorn_start.sh放入以下内容(建议放到项目目录下)</p>
        <p>i:输入 esc:停止输入,:wq:退出</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">vim gunicorn_start.sh</span></pre>
        <pre contenteditable="TRUE" class="pre"><span v-for="item in data3"
                                                      class="pre_span">{{ item }}</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>更改Django为非调试模式(通过NGINX加载配置文件)</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">DEBUG=False</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>增加可执行权限</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">chmod +x gunicorn_start.sh</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>查看是否安装成功</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">./gunicorn_start.sh</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>删除NGINX默认配置</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo rm /etc/nginx/sites-enabled/default</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>添加配置</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo vim /etc/nginx/sites-enabled/interface.com.conf</span></pre>
        <pre contenteditable="TRUE" class="pre"><span v-for="item in data4"
                                                      class="pre_span">{{ item }}</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>重启NGINX</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo /etc/init.d/nginx restart</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>配置Supervisor</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">sudo vim /etc/supervisor/conf.d/interface.conf</span></pre>
        <pre contenteditable="TRUE" class="pre"><span v-for="item in data5"
                                                      class="pre_span">{{ item }}</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>修改settings</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">ALLOWED_HOSTS=[‘*’]  # 允许所有IP访问</span></pre>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">DEBUG=True  # 调试模式</span></pre>
      </li>

      <li style="margin-top: 5px">
        <p>启动服务</p>
        <pre contenteditable="TRUE" class="pre"><span
            class="pre_span">python manage.py runserver</span></pre>
      </li>

    </ol>


  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill4",
  data() {
    return {
      data1: ['channels:',
        '  - defaults',
        'show_channel_urls: true',
        'default_channels:',
        '  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main',
        '  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r',
        '  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2',
        'custom_channels:',
        '  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
        '  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud',
      ],
      data2: ['DATABASES = {',
        '    \'default\': {',
        '        \'ENGINE\': \'django.db.backends.mysql\',',
        '        \'NAME\': \'server\',',
        '        \'USER\': \'user\',',
        '        \'PASSWORD\': \'password\',',
        '        \'HOST\': \'localhost\',',
        '        \'PORT\': 3306,',
        '        \'OPTIONS\': {\'charset\': \'utf8mb4\'},',
        '    }',
        '}',
      ],
      data3: ['#!/bin/bash',
        '',
        'NAME="interface"  # serve name',
        'DJANGODIR=/home/interface #Django project directory',
        'USER=user # the user to run as',
        'GROUP=user # the group to run as',
        'NUM_WORKERS=1 # how many worker processes should Gunicorn spawn',
        'DJANGO_SETTINGS_MODULE=interface.settings # which settings file should Django use',
        'DJANGO_WSGI_MODULE=interface.wsgi # WSGI module name',
        '',
        'echo "Starting $NAME as `whoami`"',
        '',
        '# Activate the virtual environment',
        'cd $DJANGODIR',
        'source /root/miniconda3/envs/myenv/bin/activate  # python environment',
        'export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE',
        'export PYTHONPATH=$DJANGODIR:$PYTHONPATH',
        '',
        '# Create the run directory if it doesn\'t exist',
        'RUNDIR=$(dirname $SOCKFILE)',
        'test -d $RUNDIR || mkdir -p $RUNDIR',
        '',
        '# Start your Django Unicorn',
        '# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)',
        'exec /root/miniconda3/envs/myenv/bin/gunicorn  ${DJANGO_WSGI_MODULE}:application \  # gunicorn location same as what python environment',
        '--name $NAME \\',
        '--workers $NUM_WORKERS \\',
        '--user=$USER --group=$GROUP \\',
        '--log-level=debug \\',
        '--log-file=-',
      ],
      data4: ['server {',
        '',
        '    listen 80;',
        '    server_name 180.76.144.127;  # host',
        '    root /home/interface/;  # Django project location',
        '',
        '    access_log /var/log/nginx/django_access.log;',
        '    error_log /var/log/nginx/django_error.log;',
        '',
        '    location /static/ {',
        '        alias /home/interface/collectedstatic/;  # static resource',
        '        expires max;',
        '        access_log        off;',
        '        log_not_found     off;',
        '    }',
        '    location /media {',
        '        # 静态文件配置',
        '        alias /home/interface/uploads/;  # upload dir resource',
        '        expires max;',
        '    }',
        '    location ~ \.py$ {',
        '        return 403;',
        '    }',
        '',
        '    location / {',
        '        proxy_set_header X-Real-IP $remote_addr;',
        '        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;',
        '        proxy_set_header Host $http_host;',
        '        proxy_set_header X-NginX-Proxy true;',
        '        proxy_redirect off;',
        '        if (!-f $request_filename) {',
        '            proxy_pass http://127.0.0.1:8000;',
        '            break;',
        '        }',
        '    }',
        '',
        '}',
      ],
      data5: ['[program:interface]  # gunicorn serve name',
        'command = /home/interface/gunicorn_start.sh  # gunicorn_start location',
        'user = user # user',
        'autostart=true',
        'autorestart=true',
        '',
        'redirect_stderr = true',
        'stdout_logfile = /var/log/interface.log  # log',
        'stderr_logfile=/var/log/interface.err  # log',
      ]
    }
  },
  methods: {}
}
</script>


<style>
.skill4 {
  float: left;
  margin-left: 5%;
  width: 60%;
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
  padding-left: 0.5%;
}


</style>