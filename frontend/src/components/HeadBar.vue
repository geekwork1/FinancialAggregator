<template>
  <div>
    <v-container fluid >
      <v-btn outlined class="ml-3">
        <router-link :to="{ name:'main' }">Главная</router-link>
      </v-btn>
      <v-btn outlined class="ml-3">
        <router-link to="/snippet">Snippet</router-link>
      </v-btn>

      <v-btn outlined class="ml-3">
        <router-link to="/photos">Фотографии</router-link>
      </v-btn>


  <v-btn outlined color="success" class="ml-3">
    <router-link to="/login">Login</router-link>
  </v-btn>

  </v-container>
  </div>


</template>

<script>
export default {
  name: "HeadBar"
}
</script>

<style scoped>

</style >
