<template>
  <v-form
      ref="form"
  >
    <v-container>

      <v-col>
        <v-file-input
            type="file"
            class=""
            label="Upload photo"
            hint="Add a picture"
            outlined
            dense
            @change="onFileChange"
        />
      </v-col>
      <v-col>
        <h4>Your avatar</h4>
        <v-img :src="avaUrl" style="border: 1px dashed #ccc; min-height: 250px"/>
      </v-col>

      <v-text-field
          v-model="first_name"
          label="first-name"
      />

      <v-text-field
          v-model="middle_name"
          label="middlename"
      />

      <v-text-field
          v-model="last_name"
          label="lastname"
      />

      <v-text-field
          v-model="inn_field"
          label="innfield"
      />

      <v-text-field
          v-model="phone"
          label="phone"
      />

      <v-text-field
          v-model="address"
          label="address"
      />

      <v-text-field
          v-model="username"
          label="username"
      />

      <v-text-field
          v-model="email"
          label="E-mail"
      />

      <v-btn
          color="success"
          class="mr-4"
          @click=""
      >
        <p>
          Update Profile"
        </p>
      </v-btn>

    </v-container>
  </v-form>
</template>

<script>
// import axiosInstance from "@/utils/axiosInstance";



import axios from "axios";

export default {
  name: "ProfileList",
  data: () => ({
    user_id: '',
    first_name: '',
    middle_name: '',
    last_name: '',
    inn_field: '',
    address: '',
    phone: '',
    avatar: undefined,
    avaUrl: '',
    username: '',
    email: ''
  }),
  methods: {
    async getData() {
      try {
        const response = await axios.get('userprofile/');

        console.log(response);
        this.user_id = response.data[0].user.pk;
        console.log('id:', this.user_id);
        this.avatar = response.data[0].avatar;
        console.log(this.avatar);
        this.first_name = response.data[0].first_name;
        console.log('firstname ', this.first_name);
        this.middle_name = response.data[0].middle_name;
        console.log('middle_name ', this.middle_name);
        this.last_name = response.data[0].last_name;
        console.log('last_name ', this.last_name);
        this.inn_field = response.data[0].inn_field;
        console.log('innfield ', this.inn_field);
        this.phone = response.data[0].phone;
        console.log('phone ', this.phone);
        this.address = response.data[0].address;
        console.log('address ', this.address);
        this.username = response.data[0].user.username;
        console.log(this.username);
        this.email = response.data[0].user.email;
        console.log(this.email);
        this.avaUrl = response.data[0].avatar;

        if (response.status === 401 || response.status === 403) {
          this.$router.push('/login');
        }
      } catch (e) {
        console.log(e)
      }
    },

    createImage(file) {
      try {
        const reader = new FileReader();

        reader.onload = (e) => {
          this.avaUrl = e.target.result;
        };
        reader.readAsDataURL(file);
      } catch (e) {
        console.log(e);
      }
    },
    onFileChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;

      this.createImage(files[0]);
    }
  },


  mounted() {
    this.getData();
  },
}
</script>

<style scoped>

</style>