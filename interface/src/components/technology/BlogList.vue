<template>
  <div class="blog_list">
    <h4 style="margin: 5px;list-style:none;font-family: '等线 Light'">文章目录</h4>
    <ol style="margin-left: 20px;margin-top: 2px">
      <li>
        <a style="text-decoration: none" href="#foreword">前言</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#technologyList">技术清单</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#systemRelease">系统发布</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#problemSolving">难题解决</a>
        <ul style="list-style-type: disc;margin-left: 5px;margin-top: 2px">
          <li>
            <a style="text-decoration: none" href="#crossDomainProblem">跨域问题</a>
          </li>
          <li>
            <a style="text-decoration: none" href="#staticFileProblem">静态文件问题</a>
            <ul style="margin-left: 15px;">
              <li>
                <a style="text-decoration: none" href="#debugMode">调试模式</a>
              </li>
              <li>
                <a style="text-decoration: none" href="#non-debugMode">非调试模式</a>
              </li>
            </ul>
          </li>
          <li>
            <a style="text-decoration: none" href="#VueAndDjangoJointDebugging">Vue与Django联调</a>
            <ul style="margin-left: 15px;margin-top: 2px">
              <li>
                <a style="text-decoration: none" href="#DjangoDeployVue">Django部署Vue</a>
              </li>
              <li>
                <a style="text-decoration: none" href="#VueAccessDjango">Vue访问Django</a>
              </li>
            </ul>
          </li>

        </ul>
      </li>
      <li>
        <a style="text-decoration: none" href="#other">其它</a>
      </li>

    </ol>
  </div>

</template>

<script>
export default {
  name: "ComponentsTechnologyBlogList"
}
</script>

<style>
.blog_list {
  float: left;
  width: 20%;
  height: 500px;
  box-shadow: #666 0px 0px 10px 0px;
  margin-left: 2%;
  position: fixed;

}


</style>