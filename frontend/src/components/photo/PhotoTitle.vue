<template>
  <v-col cols="4">
    <v-card class="d-inline-flex" heght="100" width="200" @click="openPhoto">
      <v-card-title class="d-inline-block">Фото: {{photo.title}}

      </v-card-title>
      <v-card-text>
        <v-img
            :src="photo.photo"
            width="30"
            height="30"
        />
      </v-card-text>
    </v-card>
  </v-col>
</template>

<script>
export default {

  // props:{
  //   photo: {
  //     type: Object,
  //     required: true
  //   }
  // },
  props: ['photo'],
  methods:{
    openPhoto(){
      this.$emit('openPhoto', this.photo)
    }
  },
}
</script>

<style scoped>

</style>