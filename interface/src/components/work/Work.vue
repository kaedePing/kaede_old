<template>
  <ul class="work">
    <li class="work_item" v-for="(item,index) in works" v-bind:key="index">
      <div>
        <h3>
          待遇相关
        </h3>
        <div>
          薪资：{{ item.salary }}
        </div>
        <div>
          吃住：{{ item.room_board }}
        </div>
      </div>

      <div>
        <h3>
          工作要求
        </h3>
        <div>
          性别：{{ item.sex }}
        </div>
        <div>
          年龄：{{ item.age }}
        </div>
        <div>
          地址：{{ item.address }}
        </div>
      </div>

      <div>
        <a href="" :title="item.title">详细信息</a>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
  name: "ComponentsWorkWork",
  data() {
    return {
      works: [],
      salary: 10,
      room_board: '吃住',
      sex: '男',
      age: '25-45',
      address: '万州区',
      title: '2.27沙坪坝英业达 | 周结临时工          \n' +
          '          【140/天 包三餐】\n' +
          '🆘优势: 不体检、不面试、可选择白夜班、包三餐、至少做5天以上\n' +
          '要求: 16一45岁 男女不限 长期要人 无案底记录\n' +
          '工资: 140元/天（白班11H 夜班10.5H 不满工时的按13元/时计算）可提供住宿10元/天 每周一周五结算一次\n' +
          '地点: 沙坪坝大学城曾家\n' +
          '\n' +
          '️注意: 至少接种疫苗一针以上 行动轨迹在渝14天不用做核酸 行动轨迹只要云贵川渝的 去过外省的不行 云贵川必须持有48小时以内核酸结果 能做五天以上的都可以来'
    }
  },
  methods: {
    init_param() {
      let _this = this
      _this.works.push({
        'salary': _this.salary,
        'room_board': _this.room_board,
        'sex': _this.sex,
        'age': _this.age,
        'address': _this.address,
        'title': _this.title
      })
      _this.works.push({
        'salary': _this.salary,
        'room_board': _this.room_board,
        'sex': _this.sex,
        'age': _this.age,
        'address': _this.address,
        'title': _this.title
      })
      _this.works.push({
        'salary': _this.salary,
        'room_board': _this.room_board,
        'sex': _this.sex,
        'age': _this.age,
        'address': _this.address,
        'title': _this.title
      })
    }
  },
  mounted() {
    this.init_param()  //调用初始化函数
  },
}
</script>

<style>
.work {
  float: left;
  position: relative;
  margin-left: 2%;
  width: 50%;
  height: 500px;
  /*background-color: gray;*/
  box-shadow: #666 0px 0px 10px 0px;
}

.work_item {
  list-style: none;
  margin-left: 1%;
  margin-top: 1%;
  width: 48%;
  height: 200px;
  /*background-color: #1b6d85;*/
  box-shadow: #666 0px 0px 10px 0px;
  float: left;
}

div {
  list-style: none;
}
</style>