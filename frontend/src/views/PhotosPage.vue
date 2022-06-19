<template>
  <v-container>
    <h1>Фотографии</h1>
<!--Скрываем страницу-->
<!--    <PhotoForm v-if="photos.length < 12" @addPhoto="addPhoto" />-->
<!--    <div v-else> Вы не можете больше добавить фотографий</div>-->
<!--    Скрываем, но в DOM остается-->
<!--    <PhotoForm v-show="dialogVisible" @addPhoto="addPhoto" />-->
    <PhotoForm @addPhoto="addPhoto" />

    <v-row>
          <Photo
              v-for="photo in photos"
              v-bind:photo="photo"
              @openPhoto="openPhoto"
          />
    </v-row>
    <PhotoDialog
        :photo="currentPhoto"
        v-model="dialogVisible"
    />
  </v-container>


</template>

<script>


import axios from "axios";
import Photo from "@/components/photo/Photo";
import PhotoForm from "@/components/photo/PhotoForm";
import PhotoDialog from "@/components/photo/PhotoDialog";

export default {
  components:{
    Photo, PhotoForm, PhotoDialog,
  },

  name: "photo",
  data: () => {
    return {
      photos: [],
      // posts:[],
      // currentPage: 1,
      currentPhoto: {},
      dialogVisible: false,
      // showNextButton: false,
      // showPrevButton: false,
      // auth: {},
      // snippet: {},
      // snippets: [],
      // errors: [],
      // myquery: '',
    }
  },
  async created(){
    await this.fetchTodo()
  },
  methods:{
    async fetchTodo() {
      try {
        await axios
            // .get(`https://jsonplaceholder.typicode.com/photos?_limit=10`)
            .get(`${this.$store.getters.getServerUrl}/api/snippet/`)
            .then(response=> this.photos = response.data.results)
        } catch (e) { this.errors.push(e) }
      },
    addPhoto(photo){
      this.photos.push(photo)
    },

    openPhoto(photo){
      this.currentPhoto = photo
      this.dialogVisible = true
    }


  },
}
 </script>

<style scoped>

</style>