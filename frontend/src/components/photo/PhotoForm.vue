<template>
  <v-container>
    <v-row class="d-flex">
      <v-text-field v-model="title"/>
      <v-file-input v-model="img"/>
      <v-btn @click="addPhoto">Добавить</v-btn>
    </v-row>
  </v-container>

</template>

<script>
export default {
  name: "PhotoForm",
  data:() => {
    return{
      title: '',
      img: [],
    }
  },
  methods:{
    addPhoto() {
      const reader = new FileReader()
      reader.readAsDataURL(this.img[0])
      reader.onload = () => {
        let photo = {
          id: Date.now(),
          title: this.title,
          // url: reader.result
          photo: reader.result
        }
        this.$emit('addPhoto', photo)
      }

    },
  }
}
</script>

<style scoped>

</style>