<template>
  <div class="person">
    <div style="position: relative">
      <img src="../../assets/avatar_bg.jpg" alt="头像背景" class="person_avatar_bg">
      <div class="person_avatar"></div>
      <div class="person_name">
        {{ blog_name }}
      </div>
    </div>

    <div class="person_connect">
      <div class="person_connect_wechat" @mouseenter="wechatenter" @mouseleave="wechatleave"></div>
      <img src="../../assets/wechat.jpg" alt="微信二维码" :class="{'person_connect_wechat_code':wechat,person_connect_wechat_code_default:!wechat}">
      <div class="person_connect_qq" @mouseenter="qqenter" @mouseleave="qqleave"></div>
      <img src="../../assets/qq.jpg" alt="QQ二维码" :class="{'person_connect_qq_code':qq,person_connect_qq_code_default:!qq}">
      <a href="https://space.bilibili.com/38836094/bangumi" target="_blank">
        <div class="person_connect_bilibili"></div>
      </a>
    </div>
    <hr style="margin-top: -30px">
    <div style="margin-top: 10px">
      <div class="summary_articles">
        文章  {{articles_sum}}
      </div>
      <div class="summary_life">
        生活  {{life_sum}}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ComponentsHomeSelf",
  data() {
    return {
      blog_name:'kaede',
      wechat:false,  //用来控制微信二维码显示与否
      qq:false,  //用来控制qq二维码显示与否

      articles_sum:1,  //文章数量
      life_sum:0  //生活数量
    }
  },
  methods:{
    wechatenter:function (){
      this.wechat=true
    },
    wechatleave:function (){
      this.wechat=false
    },
    qqenter:function (){
      this.qq=true
    },
    qqleave:function (){
      this.qq=false
    }
  }

}
</script>

<style>
.person {
  width: 25%;
  height: 370px;
  background-color: #f3f3f3;
  float: left;
  margin-left: 8%;
  position: relative;
  border-radius: 5%;
}

.person_avatar_bg {
  width: 100%;
  height: 150px;
  border-radius: 5%;
}

.person_avatar {
  border-radius: 50%; /*控制圆角*/
  width: 90px;
  height: 90px;
  background: url("../../assets/avatar.jpg") no-repeat center;
  background-size: 250px; /*控制图片显示的位置*/
  margin-top: -50px;
  margin-left: 30%;
  z-index: 5;
  position: relative;
  transition-duration: 4s;
}

.person_avatar:hover {
  transform: rotate(360deg);
}

.person_name {
  position: relative;
  margin-top: 10px;
  margin-left: 35%;
  font-size: 20px;
}
.person_connect{
  margin-top: 20px;
  position: relative;
  height: 100px;
}
.person_connect_wechat{
  border-radius: 50%;
  background: url("../../assets/wechat.png") no-repeat center;
  width: 40px;
  height: 40px;
  margin-left: 20px;
  position: absolute;
  background-size: 40px;
  box-shadow: 0px 0px 10px gray;
  float: left;
}
.person_connect_wechat:hover{
  transform: scale(1.1);
}
.person_connect_wechat_code{
  float: left;
  width: 180px;
  margin-left: 60px;
  margin-top: -10px;
  position: absolute;
  z-index: 5;
}
.person_connect_wechat_code_default{
  float: left;
  width: 180px;
  margin-left: 60px;
  margin-top: -10px;
  display: none;
  position: absolute;
}
.person_connect_qq{
  border-radius: 50%;
  background: url("../../assets/qq.png") no-repeat center;
  width: 45px;
  height: 45px;
  margin-left: 100px;
  position: absolute;
  background-size: 45px;
  box-shadow: 0px 0px 10px gray;
  float: left;
}
.person_connect_qq:hover{
  transform: scale(1.1);
}
.person_connect_qq_code{
  float: left;
  width: 180px;
  margin-left: 146px;
  margin-top: -10px;
  position: absolute;
  z-index: 5;
}
.person_connect_qq_code_default{
  float: left;
  width: 180px;
  margin-left: 146px;
  margin-top: -10px;
  margin-top: -10px;
  display: none;
  position: absolute;
}
.person_connect_bilibili{
  border-radius: 50%;
  background: url("../../assets/bilibili.png") no-repeat center;
  width: 45px;
  height: 45px;
  margin-left: 180px;
  position: absolute;
  background-size: 45px;
  box-shadow: 0px 0px 10px gray;
  float: left;
  cursor: pointer;
}
.person_connect_bilibili:hover{
  transform: scale(1.1);
}
.summary_articles{
  float: left;
  margin-left: 30px;
  color: #1A01CC;
}
.summary_life{
  float: left;
  margin-left: 30px;
  color: #1A01CC;
}
</style>