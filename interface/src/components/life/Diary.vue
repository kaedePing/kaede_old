<template>
  <div class="diary">
    <h1 class="diary_title">{{ diary_title }}</h1>
    <div class="diary_item" v-for="item in diary_detail" v-bind:key="item">
      <div class="diary_time">{{ item.diary_time }}</div>
      <p class="diary_content">
        {{ item.diary_content }}
      </p>
    </div>
    <div id="skPlayer">
    </div>
  </div>
</template>

<script>
export default {
  name: "ComponentsLifeLifeDiary",
  data() {
    return {
      diary_title: 'Kaedeのにっき',
      diary_detail: []
    }
  },
  methods: {
    init_param() {
      this.diary_detail.push({
        'diary_time': '2021年12月18日',
        'diary_content': '今天开始写日记'
      })
      this.diary_detail.push({
        'diary_time': '****年**月**日',
        'diary_content': '有人用童年治愈一生，有人用一生治愈童年'
      })
      this.diary_detail.push({
        'diary_time': '****年**月**日',
        'diary_content': '最美的不是风景，而是你刚好在这里。愿终能找到一个陪伴一生的人，去游遍三河，看繁华盛世。'
      })
      this.diary_detail.push({
        'diary_time': '****年**月**日',
        'diary_content': '愿你既有手握方向盘的自由，也有坐副驾驶的快乐，前者是生活，后者是被爱，有能力生活，也有资格被爱。'
      })

    }
  },
  mounted() {
    this.init_param();
  }
}
</script>

<style>
.diary {
  float: left;
  margin-left: 5%;
  width: 60%;
  /*height: 1000px;*/
  box-shadow: 0px 0px 1px gray;
  position: relative;
  margin-top: 5px;
}

.diary_title {
  text-align: center;
}

.diary_time {
  margin-left: 10px;
  margin-top: 15px;
}

.diary_time {
  font-family: 华文彩云;
}

.diary_content {
  font-family: 方正舒体;
  padding-left: 2em;
  margin-top: 5px;
  font-size: 1.2em;
}

</style>