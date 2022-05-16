<template>
  <v-col cols="4">
    <v-card class="d-block" heght="600" @click="openPhoto">
      <v-card-title class="d-inline-block">{{photo.title}}
        <v-card-text max-height="200">
          <v-img
              :src="photo.photo"
              width="200"
              height="200"
          />
        </v-card-text>
      </v-card-title>
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