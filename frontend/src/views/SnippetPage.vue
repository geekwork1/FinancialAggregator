<template>
  <div id="app">
    <div class="form-group row">
      <input type="text" class="form-control col-3 mx-2" placeholder="Input search text" v-model="myquery">
      <button @click="searchText(myquery) " class="btn btn-success">Search</button>
    </div>

    <form @submit.prevent="submitForm" >
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Title" v-model="snippet.title">
        <input type="text" class="form-control col-3 mx-2" placeholder="Owner" v-model="snippet.owner">
        <v-file-input class="form-control col-3 mx-2" placeholder="Photo" v-model="img"></v-file-input>
        <button class="btn btn-danger">Submit</button>
      </div>
    </form>

    <table class="d-inline">
      <thead>
      <th width="200" align="center">ID</th>
      <th width="200">Title</th>
      <th width="200">Owner</th>
      <th width="200">Create</th>
      <th width="200">Photo</th>
      </thead>
      <tbody>
      <tr  v-for="snippet in snippets.results" @dblclick="$data.snippet=snippet" :key="snippet.id">
        <td align="center">{{ snippet.id }}</td>
        <td>{{ snippet.title }}</td>
        <td>{{ snippet.owner }}</td>
        <td>{{ snippet.created }}</td>

        <PhotoTitle
            v-bind:photo="snippet"
            @openPhoto="openPhoto"
        />
        <PhotoDialog
            :photo="currentPhoto"
            v-model="dialogVisible"
        />

        <td>
          <button class="btn btn-outline-danger btn-sm mx-3" @click="deleteSnippet(snippet)">X</button>
        </td>
      </tr>
      </tbody>
    </table>

  </div>
  <div class="form-group row pagination">
    <div v-if="showPrevButton" class="bnt btn-link">
      <button @click="loadPrev()">Prev</button>
    </div>
    <div v-if="showNextButton" class="bnt btn-link">
      <button @click="loadNext() ">Next</button>
    </div>
  </div>
</template>

<script>

import axios from "axios";
import PhotoDialog from "@/components/photo/PhotoDialog";
import Photo from "@/components/photo/Photo";
import PhotoForm from "@/components/photo/PhotoForm";
import PhotoTitle from "@/components/photo/PhotoTitle";
import photo from "@/components/photo/Photo";


export default {
  components: {
    Photo, PhotoDialog, PhotoForm, PhotoTitle
  },

  name: "SnippetPage",

  data:() =>{
    return{
      posts:[],
      currentPage: 1,
      showNextButton: false,
      showPrevButton: false,
      auth: {},
      snippet: {},
      snippets: [],
      errors: [],
      myquery: '',
      currentPhoto: {},
      dialogVisible: false,
      photos: [],
      photo:[],
      img:[],
      file: null,
      imageUrl: null
    }
  },
  async created(){
    await this.getSnippets();
  },
  methods: {

    openPhoto(photo){
      this.currentPhoto = photo
      this.dialogVisible = true
    },


    addPhotoServer(){

      const reader = new FileReader()
      reader.readAsDataURL(this.img[0])
      reader.onload = () => {
        let photo= {
          photo: reader.result
        }
      }
      let fd = new FormData();
      fd.append('file', this.img)
      fd.append('photo', this.img.name)
      fd.append('id', this.snippet.id)
      fd.append('owner', this.snippet.owner)
      fd.append('title', this.snippet.title)
      fd.append('snippet', this.snippet)
      console.log('fd', fd)
    },





    searchText(){
      console.log('this.myquery ', this.myquery);
      this.currentPage = '1'
      this.getSnippets()
      // this.myquery = ''
    },
    loadNext(){
      this.currentPage++
      this.getSnippets()
    },
    loadPrev(){
      this.currentPage--
      this.getSnippets()
    },
    submitForm(){
      if (this.snippet.id === undefined){
        this.createSnippet();
      } else {
        this.editSnippet()
      }
    },
    async getSnippets() {
      try {
        this.showNextButton = false
        this.showPrevButton = false
        // let BASE_URL=BASE_URL;
        await axios

            .get(`${this.$store.getters.getServerUrl}/snippet/?page=${this.currentPage}&search=${this.myquery}`)
            .then(response =>
                this.snippets = response.data
            )
        if (this.snippets.next) {
          this.showNextButton = true
        }
        if (this.snippets.previous) {
          this.showPrevButton = true
        }
      } catch (e) {
        this.errors.push(e)
      }
    },
    async createSnippet(){
      this.addPhotoServer()
      try {
        await axios.post(`${this.$store.getters.getServerUrl}/snippet/`, this.snippet,
            {
              headers: {
                'Content-Type': 'multipart/form-data',
                data: this.fd
              }
            }
        )

        await this.getSnippets();
      } catch (e) {
        this.errors.push(e)
      }
    },
    async editSnippet(){
      try {
        await axios.put(`${this.$store.getters.getServerUrl}/snippet/${this.snippet.id}/`, this.snippet);
        await this.getSnippets();
        this.snippet = {};
      } catch (e) {
        this.errors.push(e)
      }
    },
    async deleteSnippet(snippet){
      try {
        await axios.delete(`${this.$store.getters.getServerUrl}/snippet/${snippet.id}/`, this.snippet);
        this.showNextButton = false
        this.showPrevButton = false
        this.currentPage =1
        await this.getSnippets();
        this.snippet = {};
      } catch (e) {
        this.errors.push(e)
      }
    },
  },
}




</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>