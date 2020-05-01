<template>
  <div>
    <b-container mw-25>
      <b-card header="Create an Event" header-tag="header" border-variant="primary">
        <b-form @submit="onSubmit" @reset="onReset" v-if="40">
          <b-form-group id="input-group-1" label="Event Name:" label-for="input-1">
            <b-form-input
              id="input-1"
              v-model="form.name"
              type="text"
              required
              placeholder="The name of your event"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-2" label="Event Category" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="form.category"
              type="text"
              required
              placeholder="Enter the category of your event"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-3" label="Event Details" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.details"
              type="text"
              required
              placeholder="Enter the description of your event"
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="input-group-4"
            label="Event Address"
            label-for="input-4, input-5, input-6"
          >
            <b-form-input
              id="input-3"
              v-model="form.address"
              type="text"
              required
              placeholder="Enter the street address of your event"
            ></b-form-input>
            <b-form-input
              id="input-4"
              v-model="form.county"
              type="text"
              required
              placeholder="Enter the county of your event"
            ></b-form-input>
            <b-form-input
              id="input-5"
              v-model="form.state"
              type="text"
              required
              placeholder="Enter the state of your event"
            ></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-4" label="Date" label-for="input-6">
            <b-form-input id="input-6" v-model="form.date" type="text" required placeholder="Date"></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-5" label="Time" label-for="input-7">
            <b-form-input
              id="input-7"
              v-model="form.time"
              type="text"
              required
              placeholder="Enter Time"
            ></b-form-input>
          </b-form-group>

          <b-button class="top-button" type="submit" variant="primary">Create Event</b-button>
          <b-button class="top-button" type="reset" variant="danger">Reset Form</b-button>
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
        name: "",
        category: "",
        details: "",
        address: "",
        county: "",
        state: "",
        date: "",
        time: ""
      },

      show: true
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.form));
      console.log(this.$root.$router.app.$children[0]);
      this.createEvent(this.form);
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.eventName = "";
      this.form.eventCategory = "";
      this.form.eventAddress = "";
      this.form.eventCounty = "";
      this.form.eventState = "";
      this.form.date = "";
      this.form.time = "";

      // Trick to reset/clear native browser form validation state
      this.show = false;
    },
    createEvent(e) {
      const createEventURI = `http://127.0.0.1:5000/api/v1/event`;
      console.log(e)
      console.log(this.$store.state.userAccessToken);
    //   const eventData = e;
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.userAccessToken}`
        }
      };
      if (this.$store.state.loggedIn) {
        this.$http
          .post(createEventURI, this.form, config)
          .then(result => {
            console.log(result);
            this.$router.push("/events");
            // this.getEvents();
          })
          .catch(error => {
            console.log(error.config);
          });
      } else {
        alert("You must log in to create an event!");
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.top-button {
  margin: 0.5rem;
}
</style>
