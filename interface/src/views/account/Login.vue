<template>
  <div class="body">
    <AccountLogin></AccountLogin>
  </div>
</template>

<script>
import AccountLogin from "@/components/account/AccountLogin";

export default {
  name: "ViewsAccountLogin",
  components: {
    AccountLogin
  }
}
</script>

<style>
* {
  padding: 0;
  margin: 0;
}

.body {
  margin-top: 10px;
}
</style>