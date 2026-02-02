<template>
  <div class="skill8_list">
    <h4 style="margin: 5px;list-style:none;font-family: '等线 Light'">文章目录</h4>
    <ol style="margin-left: 20px;margin-top: 2px">
      <li>
        <a style="text-decoration: none" href="#cssFontProperties">css字体属性</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#cssTextProperty">css文本属性</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#cssSelectors">CSS的复合选择器</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#cssElementDisplayMode">css的元素显示模式</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#cssBackground">css的背景</a>
      </li>
      <li>
        <a style="text-decoration: none" href="#cssBoxModel">css的盒子模型</a>
      </li>
    </ol>
  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill8List"
}
</script>


<style>
.skill8_list {
  float: left;
  width: 20%;
  height: 500px;
  box-shadow: #666 0px 0px 10px 0px;
  margin-left: 2%;
  position: fixed;
}

a:link {
  color: black;
}

a:visited {
  color: black;
}

a:hover {
  color: red;
}

a:active {
  color: green;
}
</style>