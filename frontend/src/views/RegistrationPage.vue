<template>
  <v-form
      ref="form"
      v-model="valid"
      @submit.prevent="handleSubmit"
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
              v-model="email"
              :rules="emailRules"
              label="E-mail"
              required
          ></v-text-field>

          <v-text-field
              v-model="password"
              :rules="pwdRules"
              label="Password"
              required
          ></v-text-field>

          <v-text-field
              v-model="password2"
              :rules="pwdConfirm"
              label="Repeat Password"
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
                <p>Submit</p>
              </v-btn>
            </div>

            <v-btn
                color="warning"
                class="mr-4"
                @click="$router.push('/login')"
            >
              <p>Log In</p>
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
import axios from 'axios'


export default {
  name: "RegistrationPage",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',


      //Base vuetify form data
      valid: true,
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 16 || 'Name must be less than 10 characters',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      pwdRules: [v => !!v || "Password required"],
      pwdConfirm: [
        v => !!v || "Confirm password",
        v => v === this.password || "Passwords do not match"
      ]
    }
  },
  computed: {},
  methods: {
    validate() {
      this.$refs.form.validate()
    },

    async handleSubmit() {
      try {
        const response = await axios.post(`${this.$store.getters.getServerUrl}/auth/users/`, {
          username: this.username,
          email: this.email,
          password: this.password,
          password2: this.password2
        });
        console.log(response);
      } catch (e) {
        console.log(e)
      }
      await this.$router.push('/login');
    }
  }
}
</script>

<style scoped>

</style>