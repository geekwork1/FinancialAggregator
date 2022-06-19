<template>
 <v-btn
      color="error"
      class="mr-4"
      @click="handleLogout"
    >
      <p>Log Out</p>
    </v-btn>
</template>

<script>
import Cookies from "js-cookie";

export default {
  name: "LogOutButton",
  methods:{
    handleLogout () {
      Cookies.remove('access');
      Cookies.remove('refresh');

      this.$router.push('/login');
    }
  },
}
</script>

<style scoped>

</style>