<template>
  <div id="container_list">
    <table style="position: relative;margin-left: 1%;margin-bottom: 20px;border-spacing: 20px;border: 1px solid black;">
      <caption><b>文件列表</b></caption>
      <tr class="container_list_header">
        <th style="font-size: 20px;width: 30%;">
          文件名
        </th>
        <th style="width: 10%">
          文件类型
        </th>
        <th style="width: 30%">
          上传日期
        </th>
        <th style="width: 15%">
          下载
        </th>
        <th style="width: 15%">
          删除
        </th>
      </tr>

      <tr v-for="item in files">
        <td style="font-size: 20px;width: 30%">
          {{ item.originalName }}
        </td>
        <td style="width: 10%">
          {{ item.originalType }}
        </td>
        <td style="width: 30%;padding-left: 5%">
          {{ item.dateCreatedStr }}
        </td>
        <td style="width: 15%">
          <button type="button" style="width: 100%;height: 30px">
            <a style="width: 100%;height: 30px" :href="''+item.downloadLink+''">下载</a>
          </button>
        </td>
        <td style="width: 15%">
          <button type="button" style="width: 100%;height: 30px" @click="delete_file(item.id)">删除</button>
        </td>
      </tr>

    </table>
  </div>
</template>

<script>

import common from "@/components/common/common";

export default {
  name: "ComponentsOthersFiles",
  data() {
    return {
      url: common.httpUrl + '/original/documents',
      files: []
    }
  },
  methods: {
    init_param: function () {
      // 文件组件初始化函数
      let _this = this

      _this.$http.get(_this.url).then(function (res) {
        _this.files = res['data']  // 此次请求的结果
      }).catch(function (error) {
        // _this.$message.error('请重新登录')
        console.log(error)
        // _this.$router.push('/')
      })
    },
    delete_file: function (id) {
      let _this = this
      let headers = {
        'Authorization': 'Token ' + _this.$store.getters.getToken,
        'Content-Type': 'application/json'
      }

      let url_delete = _this.url + '/' + id
      let userId = _this.$store.getters.getId // 先获取当前用户ID
      if (userId != null && userId == common.userName) {
        // 已经登录过，且当前用户满足要求
        _this.$http.delete(url_delete, {headers: headers}).then(function (res) {
          console.log('删除成功')
        }).catch(function (error) {
          // _this.$message.error('请重新登录')
          console.log(error)
          // _this.$router.push('/')
        })
      } else if (userId == null) {
        // 需要到登录页面重新登录
        _this.$router.push({path: '/Login'})  // 跳转到登录页面进行登录
      } else {
        // 无权查看
        _this.$message.error('禁止删除！')
      }


    }
  },
  mounted() {
    this.init_param()
  }
}
</script>

<style>
.container_list_header {
  margin-top: 2px;

}
</style>