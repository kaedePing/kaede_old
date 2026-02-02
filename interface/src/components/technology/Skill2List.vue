<template>
  <div class="skill3_list">
    <h4 style="margin: 5px;list-style:none;font-family: '等线 Light'">文章目录</h4>
    <ol style="margin-top: 2px;list-style-type: none">
      <li>
        <a style="text-decoration: none" href="#foreword">一.前言</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#DjangoBasicDevelopmentProcess">二.Django基本开发流程</a>
      </li>
      <ol style="margin-left: 5%">
        <li>
          <a style="text-decoration: none" href="#createProject">创建project</a>
          <ul style="margin-left: 5%">
            <li>
              <a style="text-decoration: none" href="#DatabaseConfiguration">数据库配置</a>
            </li>
            <li>
              <a style="text-decoration: none" href="#RegisterToLoadTheApp">注册加载应用</a>
            </li>
            <li>
              <a style="text-decoration: none" href="#defineRoutes">定义路由</a>
            </li>
          </ul>
        </li>

        <li>
          <a style="text-decoration: none" href="#createApp">创建app</a>
          <ul style="margin-left: 5%">
            <li>
              <a style="text-decoration: none" href="#modelsFile">models文件</a>
            </li>
            <li>
              <a style="text-decoration: none" href="#serializersFile">serializers文件</a>
            </li>
            <li>
              <a style="text-decoration: none" href="#viewsFile">views文件</a>
            </li>
            <li>
              <a style="text-decoration: none" href="#urlsFile">urls文件</a>
            </li>
          </ul>
        </li>
      </ol>


      <li>
        <a style="text-decoration: none" href="#AdvancedPart">三.高阶部分</a>
      </li>
      <ul style="margin-left: 10%;list-style-type: square">
        <li>
          <a style="text-decoration: none" href="#LoadComponents">加载组件</a>
        </li>
        <li>
          <a style="text-decoration: none" href="#ConfigureTheCorrespondingInformation">配置相应信息</a>
        </li>
      </ul>
      <ol style="margin-left: 5%">
        <li>
          <a style="text-decoration: none" href="#AutomaticInterfaceDocumentation">自动接口文档</a>
        </li>
        <li>
          <a style="text-decoration: none" href="#uploadFiles">上传文件</a>
        </li>
        <li>
          <a style="text-decoration: none" href="#timeZoneSetting">时区设置</a>
        </li>
      </ol>
    </ol>
  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill3List"
}
</script>


<style>
.skill3_list {
  float: left;
  width: 20%;
  height: 500px;
  box-shadow: #666 0px 0px 10px 0px;
  margin-left: 2%;
  position: fixed;
}
</style>