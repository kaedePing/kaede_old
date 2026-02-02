<template>
  <div class="skill1_list">
    <h4 style="margin: 5px;list-style:none;font-family: '等线 Light'">文章目录</h4>
    <ol style="margin-left: 20px;margin-top: 2px">
      <li>
        <a style="text-decoration: none" href="#storeToken">存储token</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#usingAxios">使用Axios</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#passingValuesBetweenComponents">不同组件之间传值</a>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: "ComponentsTechnologySkill1List"
}
</script>

<style>
.skill1_list {
  float: left;
  width: 20%;
  height: 500px;
  box-shadow: #666 0px 0px 10px 0px;
  margin-left: 2%;
  position: fixed;

}
</style>