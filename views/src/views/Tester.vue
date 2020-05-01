<template>
  <div>
    <b-container>
      <b-row align-h="center" class="mx-2">
        <h1>Testing, testing, 1 - 2 - 3</h1>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="login">Log In</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="logOut">Log Out</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="rsvp">RSVP</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="getRSVPs">Get RSVPs</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="printUser">Print Logged In User</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="getAllUsers">Print All Users to Console</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="makeAdmin">Promote current user to admin</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="changeEmail">Change Email</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <button v-on:click="changeName">Change Name</button>
      </b-row>
      <b-row align-h="center" class="mt-2">
        <b-card :title="displayTitle">
          <b-card-text v-for="el in Object.keys(display)" :key="display[el].public_id">
            <!-- <span v-for="thing in userInfo" :key="thing.public_id"> {{ Object.keys(userInfo) }} </span> -->
            {{ `${el}: ${display[el]}` }}
          </b-card-text>
        </b-card>
      </b-row>
    </b-container>

    <p id="display"></p>
  </div>
</template>

<script>
let token;
export default {
  name: "Tester",
  data() {
    return {
      userInfo: [],
      displayTitle: "",
      display: ""
    };
  },
  methods: {
    updateUserInfo: function() {
      const userURI = `http://127.0.0.1:5000/api/v1/user`;
      this.$http
        .get(userURI, {
          headers: {
            Authorization: `Bearer ${this.$store.state.userAccessToken}`
          }
        })
        .then(result => {
          this.userInfo = result.data.user;

          console.log(this.userInfo);
        });
    },
    login: function() {
      const loginURI = `http://127.0.0.1:5000/api/v1/login`;
      this.$http
        .post(loginURI, {
          username: "h7",
          password: "pass"
        })
        .then(result => {
          token = result.data["access token"];
          console.log(token);
          console.log(result.data["refresh token"]);

          this.updateUserInfo();
        });
    },
    printUser: async function() {
      await this.updateUserInfo();
      this.displayTitle = "User Info";
      this.display = this.userInfo;
    },
    getAllUsers: function() {
      const usersURI = `http://127.0.0.1:5000/api/v1/users`;
      this.$http
        .get(usersURI, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(result => {
          // this.display = result.data.users
          console.log(result.data.users);
        });
    },
    changeEmail: function() {
      //   const emailURI = `http://127.0.0.1:5000/api/v1/user/email`;
      let newEmail;
      if (this.userInfo.email === "boop@gmail.com") {
        newEmail = "thwip@gmail.com";
      } else {
        newEmail = "boop@gmail.com";
      }
      console.log(newEmail);
    },
    makeAdmin: function() {
      const userURI = `http://127.0.0.1:5000/api/v1/user`;
      this.$http
        .put(userURI, {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
            Authorization: `Bearer ${token}`
          }
        })
        .then(result => {
          console.log(result);
        });
    },
    changeName: function() {
      //   var myHeaders = new Headers();
      //   myHeaders.append("Content-Type", "application/json");
      //   myHeaders.append("Authorization", `Bearer ${token}`);

      //   var raw = JSON.stringify({ first_name: "Ashwin", last_name: "Ajmera" });

      //   var requestOptions = {
      //     method: "POST",
      //     headers: myHeaders,
      //     body: raw,
      //     redirect: "follow"
      //   };

      //   fetch("http://127.0.0.1:5000/api/v1/user/name", requestOptions)
      //     .then(response => response.text())
      //     .then(result => console.log(result))
      //     .catch(error => console.log("error", error));

      //   console.log(token);
      //   this.updateUserInfo();
      //   let vm = this;
      //   const options = {
      //     headers: {
      //       Accept: "application/json",
      //       "Content-Type": "application/json",
      //       Authorization: `Bearer ${token}`
      //     },
      //     data: {
      //       first_name: "buddy",
      //       last_name: "boy"
      //     }
      //   };
      //   //   const nameURI = `http://127.0.0.1:5000/api/v1/user/name`;
      //   this.$http
      //     .post(`http://127.0.0.1:5000/api/v1/user/name`, options)
      //     .then(result => {
      //       console.log(result);
      //       //   this.updateUserInfo();
      //     })
      //     .catch(error => console.log(error));

      this.$http({
        method: "post",
        url: "http://127.0.0.1:5000/api/v1/user/name",
        data: {
          first_name: "Jonathan",
          last_name: "Chickie"
        },
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
        .then(response => console.log(response))
        .then(result => console.log(result));
    },
    logOut: function() {
      this.$http
        .get("http://127.0.0.1:5000/api/v1/logout/access_token", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        })
        .then(result => {
          console.log(result);
        });
    },
    rsvp() {
      const rsvpURI = `http://127.0.0.1:5000/api/v1/rsvp`;
      console.log(this.$store.state.userAccessToken);
      const rsvpData = {
        event_public_id: "fa38b511-b4ab-4a77-9fb8-9ece4f788cd5"
      };
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.userAccessToken}`
        }
      };
      this.$http
        .put(rsvpURI, rsvpData, config)
        .then(result => {
          console.log(result);
        })
        .catch(error => {
          console.log(error.response);
        });
    },
    getRSVPs() {
      const rsvpURI = `http://127.0.0.1:5000/api/v1/rsvp`;
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.userAccessToken}`
        }
      };
      this.$http
        .get(rsvpURI, config)
        .then(result => {
          console.log(result);
        })
        .catch(error => {
          console.log(error.config);
        })
        .finally(() => {});
    }
  }
};
</script>

<style lang="scss" scoped>
</style>