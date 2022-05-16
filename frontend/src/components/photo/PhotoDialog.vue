<template>
  <v-dialog
  v-model="dialogVisible"
  max-width="900"
  >
    <v-card>
      <v-card-title>{{full_title}}</v-card-title>
      <v-card-text>
        <v-img
            :src="photo.photo"
        />
      </v-card-text>
    </v-card>

  </v-dialog>

</template>

<script>
export default {
  // Vue3 use props:[] not props:{}
  // => Error  (in promise) TypeError: Right-hand side of 'instanceof' is not an object
  props: ['photo', 'value'],
  name: "PhotoDialog",
  created() {
    this.dialogVisible = this.value
  },
  data: () => ({
    dialogVisible: false,
  }),
  //function change watcher
  watch: {
    value(newValue){
      this.dialogVisible = newValue
    },
    dialogVisible(newValue){
      this.$emit('input', newValue)
    }
  },

//  Computed Properties
  computed:{
    full_title() {
      return `Название фотографии- ${this.photo.title}`
    }
  }
}
</script>

<style scoped>

</style>