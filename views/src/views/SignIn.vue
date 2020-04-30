<template>
  <div>
    <b-container>
      <b-row>
        <b-col></b-col>
        <b-col>
          <b-card>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
              <b-form-group id="input-group-1" label="Username:" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="form.username"
                  type="text"
                  required
                  placeholder="Enter username"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2" label="Password:" label-for="input-2">
                <b-form-input
                  id="input-2"
                  v-model="form.password"
                  required
                  type="password"
                  placeholder="Enter password"
                ></b-form-input>
              </b-form-group>
              <div v-if="loginError" class="error-message">
                <span>Incorrect Credentials, please try again</span>
              </div>
              <div>
                <b-button class="top-button" type="submit" variant="primary">Submit</b-button>
                <b-button class="top-button" type="reset" variant="danger">Reset</b-button>
              </div>
              <div>
                <b-button variant="success" to="/signup">Sign up</b-button>
              </div>
            </b-form>
          </b-card>
        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: ""
      },
      regexName: /^[a-zA-Z\d]{8,16}$/,
      regexPassword: / /,
      loginError: false,
      show: true
    };
  },
  methods: {
    async onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.form));
      // console.log(this.$root.$router.app.$children[0]);
      // this.$emit("login-test", this.form);
      // if (this.$root.$router.app.$children[0].login(this.form) == 401) {
      //   alert("Invalid Credentials!");
      // } else if (this.$root.$router.app.$children[0].login(this.form) == 200) {
      //   this.$router.replace("/");
      // }
      // let status = await this.$root.$router.app.$children[0].login(this.form);
      // console.log(status);
      this.login(this.form);
      // console.log(this.$store.state.error);

      // this.$router.push("/");
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.username = "";
      this.form.password = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    login(e) {
      const loginURI = `http://127.0.0.1:5000/api/v1/login`;
      console.log(e.email);
      this.$http
        .post(loginURI, {
          username: e.username,
          password: e.password
        })
        .then(result => {
          // console.log(result.status)
          this.$store.commit("setAccess", result.data["access token"]);
          console.log(this.$store.state.userAccessToken);
          this.$store.commit("setRefresh", result.data["refresh token"]);
          console.log(this.$store.state.userRefreshToken);
          this.$store.commit("setLoggedIn", true);
          this.$store.commit("setError", false);
          this.$store.commit("setStatus", result.status);
          this.$store.commit("setUsername", e.username);
          console.log(this.$store.state.username)
          this.$router.replace({
            path: "/",
            params: { status: "result.status" }
          });
        })
        .catch(error => {
          this.$store.commit("setError", true);
          this.$store.commit("setStatus", error.response.status);
          this.loginError = this.$store.state.status;
        });
    }
  }
};
</script>

<style scoped>
.error-message {
  color: red;
  text-align: left;
  font-size: 0.85rem;
  margin-bottom: 1rem;
}
.top-button {
  margin: 0.5rem;
}
</style>