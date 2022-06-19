<template>
  <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="handleLogIn"
      lazy-validation
  >
    <v-container>
      <v-row>
        <v-col
            cols="12"
            md="4"
        >
          <v-text-field
              v-model="username"
              :rules="nameRules"
              :counter="16"
              label="Login"
              required
          ></v-text-field>

          <v-text-field
              v-model="password"
              :rules="pwdRules"
              label="Password"
              required
          ></v-text-field>

          <v-row>
            <div @mouseover="validate">
              <v-btn
                  :disabled="!valid"
                  color="success"
                  class="mr-4"
                  type="submit"
              >
                <p>Log In</p>
              </v-btn>
            </div>

            <v-btn
                color="warning"
                class="mr-4"
                @click="$router.push('/register')"
            >
              <p>Register</p>
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>

import axios from "axios";
import Cookies from 'js-cookie';

export default {
  name: "LoginPage",
  data() {
    return {
      username: '',
      password: '',

      valid: true,
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 16 || 'Name must be less than 16 characters',
      ],
      pwdRules: [v => !!v || "Password required"],
    }
  },
  methods: {
    async handleLogIn() {
      try {
        Cookies.remove('access');
        Cookies.remove('refresh');
        const response = await axios.post(`${this.$store.getters.getServerUrl}/auth/jwt/create/`, {
          username: this.username,
          password: this.password,
        });
        // console.log(response);
        // console.log(response.data);
        for (const [key, value] of Object.entries(response.data)) {
          Cookies.set(key, value,{ expires: 1 })
        }
        console.log(Cookies.get())

      } catch (e) {
        console.log(e)
      }
      // await this.$router.push('/');

    }
  },
};
</script>

<style scoped>

</style>