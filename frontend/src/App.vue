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
        <button class="btn btn-danger">Submit</button>
      </div>

    </form>




    <table class="table">
      <thead>
      <th>ID</th>
      <th>Title</th>
      <th>Owner</th>
      <th>Create</th>
      </thead>
      <tbody>
      <tr  v-for="snippet in snippets.results" @dblclick="$data.snippet=snippet" :key="snippet.id">
        <td>{{ snippet.id }}</td>
        <td>{{ snippet.title }}</td>
        <td>{{ snippet.owner }}</td>
        <td>{{ snippet.created }}</td>
        <td>
          <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteSnippet(snippet)">X</button>
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

export default {

  name: 'App',
  data(){
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
    }
  },

  async created(){

    await this.getSnippets();

  },


  methods: {

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

        await axios
            .get(`http://127.0.0.1:8000/api/snippet/?page=${this.currentPage}&search=${this.myquery}`)
            .then(response => this.snippets = response.data)
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
      try {
        await axios.post(`http://127.0.0.1:8000/api/snippet/`, this.snippet)
        await this.getSnippets();
      } catch (e) {
        this.errors.push(e)
      }

    },

    async editSnippet(){
      try {
        await axios.put(`http://127.0.0.1:8000/api/snippet/${this.snippet.id}/`, this.snippet);
        await this.getSnippets();
        this.snippet = {};
      } catch (e) {
        this.errors.push(e)
      }
    },

    async deleteSnippet(snippet){
      try {
        await axios.delete(`http://127.0.0.1:8000/api/snippet/${snippet.id}/`, this.snippet);
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

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
