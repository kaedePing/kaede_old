<script type="text/javascript">
// 定义一些公共的属性和方法
// 本地:http://127.0.0.1:8000
// 服务器:http://49.234.15.210
// const httpUrl = 'http://49.234.15.210'  // 网站IP
// const httpUrl = 'http://127.0.0.1:8000/'  // 网站IP
const httpUrl = process.env.VUE_APP_API_URL
const userName = 'Kaede'  // 博客名

function getTokenFun() {
  let token = this.$store.getters.getToken // 先查看token是否存在
  if (!token) {  // 不存在，弹出错误信息，返回空
    this.$message.error('请重新登录')
    return ''
  } else {  // 存在，返回token
    return token
  }
}

// 暴露出这些属性和方法
export default {
  httpUrl,
  getTokenFun,
  userName
}
</script>