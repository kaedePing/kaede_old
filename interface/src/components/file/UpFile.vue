<template>
  <div class="container_up" style="margin-top:20px">
    <el-button @click="getFile" style="margin-top: 10px;float: left;margin-left: 5%">
      <i class="el-icon-upload"></i>&nbsp;选择文件
    </el-button>
    <input type="file" ref="file" style="display: none;float: left" v-on:change="handleFileUpload($event)">
    <div style="float: left" class="container_list">
      <Files></Files>
    </div>
  </div>
</template>

<script>

import common from "@/components/common/common";
import Files from "@/components/file/Files";

export default {
  name: "ComponentsOthersUpFile",
  data() {
    return {
      name: "",

    };
  },
  components: {
    Files
  },
  methods: {
    // 打开文件
    getFile() {
      this.$refs.file.click()
    },
// 获取文件
    handleFileUpload(event) {
      // 阻止发生默认行为
      event.preventDefault();
      let formData = new FormData()
      let file = this.$refs.file.files[0]
      formData.append('file', file)
      console.log(formData.get('file'))
      this.onUpload(formData)
    },
// 上传文件
    onUpload(formData) {
      let url = common.httpUrl + '/standard/documents'  // 接收文件的地址  common.httpUrl
      let _this = this
      _this.$http.post(url, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }).then(function (res) {
        _this.$message.success("上传成功!!!");
      }).catch(error => {
        _this.$message.error('上传失败')
      })
    },

  }
}
;
</script>

<style>
.container_up {
  position: relative;
}

.container_list {
  position: relative;
  margin-left: 20%;
  width: 48%;


  box-shadow: #666 0px 0px 10px 0px;
}
</style>