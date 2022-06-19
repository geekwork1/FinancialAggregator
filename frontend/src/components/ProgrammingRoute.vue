<template>
<div class="d-flex inline">
  <v-btn
      class="ma-2"
      color="primary"
      dark
      @click="back"
  >
    <v-icon
        dark
        left
    >
      mdi-arrow-left
    </v-icon>Назад
  </v-btn>

  <v-btn
      class="ma-2"
      color="primary"
      dark
      @click="forward"
  >
    <v-icon
        dark
        right
    >
      mdi-arrow-right
    </v-icon>Вперед
  </v-btn>


</div>
</template>

<script>
export default {
  name: "ProgrammingRoute",

  methods:{
    // redirect(){
    //   this.$router.push( {name: 'main'},)
    // },
    back(){
      this.$router.go(-1)
    },
    forward(){
      this.$router.go(1)
    },
  },
}
</script>

<style scoped>



</style>