<template>
  <div id="app">
    <div id="nav">
      <top-header></top-header>
    </div>
    <router-view />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue";
export default {
  data() {
    return {
      accessToken: null,
      refreshToken: null,
      loggedIn: false,
      test: true
    };
  },
  methods: {
    async checkLogin() {
      const userURI = `http://127.0.0.1:5000/api/v1/user`;
      const refreshURI = `http://127.0.0.1:5000/api/v1/refresh`;

      this.$http
        .get(userURI, {
          headers: {
            Authorization: `Bearer ${this.$store.state.userAccessToken}`
          }
        })
        .then(result => {
          console.log(result.code);
        })
        .catch(error => {
          console.log(error);
          this.$http
            .get(refreshURI, {
              headers: {
                Authorization: `Bearer ${this.$store.state.userRefreshToken}`
              }
            })
            .then(result => {
              console.log(result.code);
            })
            .catch(error => {
              console.log(error);
            });
          this.$store.commit("setLoggedIn", false);
        })
        .finally(() => {
          // if (!this.loggedIn) {
          //   this.login();
          // }
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
          this.$store.commit("setAccess", result.data["access token"]);
          console.log(this.$store.state.userAccessToken);
          this.$store.commit("setRefresh", result.data["refresh token"]);
          console.log(this.$store.state.userRefreshToken);
          this.$store.commit("setLoggedIn", true);
        });
    },
    logOut: function() {
      this.$http
        .get("http://127.0.0.1:5000/api/v1/logout/access_token", {
          headers: {
            Authorization: `Bearer ${this.$store.state.userAccessToken}`
          }
        })
        .then(result => {
          this.$store.state.userAccessTokenccessToken = null;
          this.$store.state.loggedIn = false;
          console.log(result);
          this.$http
            .get("http://127.0.0.1:5000/api/v1/logout/refresh_token", {
              headers: {
                Authorization: `Bearer ${this.$store.state.userRefreshToken}`
              }
            })
            .then(result => {
              this.$store.state.userAccessTokenccessToken = null;
              this.$store.state.userRefreshToken = null;
              console.log(result);
            });
        });
    },
    signup(e) {
      const signupURI = `http://127.0.0.1:5000/api/v1/user`;
      this.$http
        .post(signupURI, {
          first_name: e.firstName,
          last_name: e.lastName,
          email: e.email,
          username: e.username,
          password: e.password
        })
        .then(result => {
          console.log(result);
          return e;
        })
        .finally(this.login(e));
    }
  },
  components: {
    "top-header": Navbar
  },
  watch: {},
  created() {
    this.checkLogin();
  }
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 0;
  padding-bottom: 3rem;
  margin-bottom: 2rem;
  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
