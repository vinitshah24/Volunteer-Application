<template>
  <div>
    <b-container mw-25>
      <b-card header="Create an Account" header-tag="header" border-variant="primary">
        <b-form @submit="onSubmit" @reset="onReset" v-if="40">
          <b-form-group id="input-group-1" label="First Name:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.firstName"
              type="text"
              required
              placeholder="Enter your first name"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="Last Name:" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.lastName"
              type="text"
              required
              placeholder="Enter your last name"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="input-group-3"
            label="Email address:"
            label-for="input-3"
            description="We'll never share your email with anyone else."
          >
            <b-form-input
              id="input-3"
              v-model="form.email"
              type="email"
              required
              placeholder="Enter email"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-4" label="Username:" label-for="input-4">
            <b-form-input
              id="input-4"
              v-model="form.username"
              type="text"
              required
              placeholder="Choose username"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-5" label="Password:" label-for="input-5">
            <b-form-input
              id="input-5"
              v-model="form.password"
              type="password"
              required
              placeholder="Choose password"
            ></b-form-input>
          </b-form-group>

          <b-button class="top-button" type="submit" variant="primary">Submit</b-button>
          <b-button class="top-button" type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-card>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        firstName: "",
        lastName: "",
        email: "",
        username: "",
        password: ""
      },

      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.form));
      console.log(this.$root.$router.app.$children[0]);
      this.$root.$router.app.$children[0].signup(this.form);
      this.$router.push("/");
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.password = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
    }
  }
};
</script>

<style lang="scss" scoped>
.top-button {
  margin: 0.5rem;
}
</style>
