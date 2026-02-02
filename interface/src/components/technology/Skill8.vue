<template>
  <div class="Skill8">
    <h1 style="margin-left: 40%">CSS</h1>
    <ol style="margin-left: 2%">
      <li>
        <h2 id="cssFontProperties">css字体属性</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>字体系列</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">font-family: "Microsoft YaHei";</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>字体大小</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">font-size: 23px;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>字体粗细</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">font-weight: bold;</span></pre>
            <p style="text-indent: 2em">normal 默认值</p>
            <p style="text-indent: 2em">
              400正常 700 加粗</p>
          </li>
          <li style="margin-top: 5px">
            <p>字体倾斜</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*font-style: italic;  倾斜*/</span></pre>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*font-style: normal;  正常*/</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>字体复合属性</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">/*font: font-style font-weight font-size/line-height font-family;*/</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">/*font: italic 700 30px 'Microsoft YaHei';*/</span></pre>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="cssTextProperty">css文本属性</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>颜色</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*color: rgba(200,100,0,0.2);*/</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>对齐</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*text-align: center;*/</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>装饰(设置下划线)</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">/*text-decoration: line-through;*/</span></pre>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*text-decoration: overline;*/</span></pre>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*text-decoration: underline;*/</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>缩进</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*text-indent: 2em;*/</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>行间距</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">/*line-height: 20px;*/</span></pre>
          </li>
        </ul>
      </li>
      <br>

      <li>
        <h2 id="cssSelectors">CSS的复合选择器</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>后代选择器</p>
            <p style="text-indent: 2em">直接选择标签层层向下面找</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">div div a{
        color: red;
              }</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>子代选择器</p>
            <p style="text-indent: 2em">选择该标签下面的子元素不会跨过孙子</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">div > a {
        color: red;}</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>并集选择器</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">span, p {
        color: grey;}</span></pre>
          </li>

          <li style="margin-top: 5px">
            <p>伪类选择器</p>
            <p style="text-indent: 2em">向某些选择器添加特殊的效果，用:表示</p>
            <p style="text-indent: 2em">注意：按下面顺序写对应的伪类选择器 link>visited>hover>activate</p>
            <ul style="text-indent: 2em">
              <li>
                <p>/*未访问过的*/</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">.a:link {
    color: red;}</span></pre>
              </li>

              <li>
                <p>/*访问过的*/</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">.a:visited {
    color: pink;}</span></pre>
              </li>

              <li>
                <p>/*鼠标经过*/</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">.a:hover {
    color: gray;}</span></pre>
              </li>

              <li>
                <p>/*鼠标按下但还没松开*/</p>
                <pre contenteditable="TRUE" class="pre"><span class="pre_span">.a:active {
    color: green;}</span></pre>
              </li>

            </ul>
          </li>

          <li style="margin-top: 5px">
            <p>focus伪类选择器</p>
            <p style="text-indent: 2em">把获得光标的input表单元素选取出来</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">input:focus{
    background-color: grey;}</span></pre>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="cssElementDisplayMode">css的元素显示模式</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>行内元素 转换为块级元素</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">display:block;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>块级元素转换为行内元素</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">display:inline;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>转换为行内块元素</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">display:inline-block;</span></pre>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="cssBackground">css的背景</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>背景颜色</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">background-color:transparent;</span></pre>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">background-color: rgba(125,125,125,0.5)</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>背景图片</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">background-image: none | url;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>背景平铺</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">background-repeat: repeat no-repeat repeat-x;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>背景图片位置（x y 无顺序关系，因为top只能在y上面 right和left只能在x上面）</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">background-position: center top;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>背景图像固定还是随屏幕滚动</p>
            <pre contenteditable="TRUE" class="pre"><span class="pre_span">background-attachment:scroll;</span></pre>
          </li>
          <li style="margin-top: 5px">
            <p>复合属性</p>
            <pre contenteditable="TRUE" class="pre"><span
                class="pre_span">background: 背景颜色 背景图片地址 背景平铺 背景图像滚动 背景图片位置;</span></pre>
          </li>

        </ul>
      </li>
      <br>

      <li>
        <h2 id="cssBoxModel">css的盒子模型</h2>
        <ul style="list-style-type: square;margin-left: 2%">
          <li style="margin-top: 5px">
            <p>边框 border</p>
            <ul style="list-style-type: square;margin-left: 2%">
              <li style="margin-top: 5px">
                <p>宽度</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">border-width: 5px;</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>样式</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">/*border-style: solid;  实线*/</span></pre>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">/*border-style: dashed;  虚线*/</span></pre>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">/*border-style: dotted;  点线*/</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>颜色</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">border-color: pink;</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>复合写法</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">border: 5px dotted pink;</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>合并相邻单元格边框</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">border-collapse: collapse;</span></pre>
              </li>
            </ul>
          </li>
          <br>

          <li style="margin-top: 5px">
            <p>内边距 padding</p>
            <ul style="list-style-type: square;margin-left: 2%">
              <li style="margin-top: 5px">
                <p>距左边内容</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">padding-left: 10px;</span></pre>
              </li>

              <li style="margin-top: 5px">
                <p>复合写法</p>
                <pre contenteditable="TRUE" class="pre"><span
                    class="pre_span">/*padding: 5px 10px 15px 20px; 顺时针。上 右 下 左*/</span></pre>

              </li>
            </ul>
          </li>
          <br>

        </ul>

      </li>


      <br>
    </ol>

  </div>
</template>


<script>
export default {
  name: "ComponentsTechnologySkill8",
  data() {
    return {}
  },
  methods: {}
}
</script>


<style>
.Skill8 {
  float: left;
  margin-left: 30%;
  width: 60%;
  height: 1000px;
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}


</style>