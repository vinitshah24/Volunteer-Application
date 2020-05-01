<template>
  <div>
    <b-container mw-25>
      <b-card header="Create an Event" header-tag="header" border-variant="primary">
        <b-form @submit="onSubmit" @reset="onReset" v-if="40">
          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="3"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              id="input-group-1"
              label="Event Name:"
              label-for="input-1"
              label-align="left"
            >
              <b-form-input
                id="input-1"
                v-model="form.name"
                type="text"
                required
                placeholder="The name of your event"
              ></b-form-input>
            </b-form-group>
          </b-card>
          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="3"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              id="input-group-2"
              label="Event Category"
              label-for="input-2"
              label-align="left"
            >
              <b-form-select v-model="form.category" :options="categories">
                <template v-slot:first>
                  <b-form-select-option value disabled>-- Please select an option --</b-form-select-option>
                </template>
              </b-form-select>
            </b-form-group>
          </b-card>
          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="3"
              label="Event Details"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              label-align="left"
              id="input-group-3"
              label-for="form-textarea"
            >
              <b-form-textarea
                id="form-textarea"
                v-model="form.details"
                placeholder="Enter a description of your event..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>
          </b-card>

          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="2"
              label="Event Address"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              label-align="left"
            >
              <b-form-group
                label-cols-sm="1"
                label="Street:"
                label-align-sm="right"
                label-for="nested-street"
              >
                <b-form-input v-model="street" id="nested-street"></b-form-input>
              </b-form-group>

              <b-form-group
                label-cols-sm="1"
                label="City:"
                label-align-sm="right"
                label-for="nested-city"
              >
                <b-form-input v-model="city" id="nested-city"></b-form-input>
              </b-form-group>

              <b-form-group
                label-cols-sm="1"
                label="State:"
                label-align-sm="right"
                label-for="nested-state"
              >
                <b-form-input v-model="form.state" id="nested-state"></b-form-input>
              </b-form-group>

              <b-form-group
                label-cols-sm="1"
                label="County:"
                label-align-sm="right"
                label-for="nested-county"
              >
                <b-form-input v-model="form.county" id="nested-county"></b-form-input>
              </b-form-group>
            </b-form-group>
          </b-card>
          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="3"
              label="Date"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              id="input-group-4"
              label-for="datepicker"
              label-align="left"
            >
              <b-form-datepicker id="datepicker" v-model="form.date" class="mb-2"></b-form-datepicker>
            </b-form-group>
          </b-card>

          <b-card bg-variant="light" class="mb-3">
            <b-form-group
              label-cols-lg="3"
              label="Time"
              label-size="lg"
              label-class="font-weight-bold pt-0"
              class="mb-0"
              id="input-group-5"
              label-for="timepicker"
              label-align="left"
            >
              <b-form-timepicker
                id="timepicker"
                v-model="form.time"
                placeholder="Choose a time"
                reset-button
                locale="en"
              ></b-form-timepicker>
            </b-form-group>
          </b-card>
          <div></div>

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
      street: "",
      city: "",
      show: true,
      categories: [
        { value: "Volunteering", text: "Volunteering" },
        { value: "Education", text: "Education" },
        { value: "Youth Outreach", text: "Youth Outreach" },
        { value: "Food donations", text: "Food donations" },
        { value: "Meal prep", text: "Meal prep" },
        { value: "Shelter generation", text: "Shelter generation" },
        { value: "Awareness building", text: "Awareness building" },
        { value: "Political action", text: "Political action" },
        { value: "Performing Arts", text: "Performing Arts" }
      ]
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      // alert(JSON.stringify(this.form));
      console.log(this.$root.$router.app.$children[0]);
      this.form.address = `${this.street}, ${this.city}`;
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
      console.log(e);
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
            this.rsvp(result.data.public_id);
            // this.getEvents();
          })
          .then(() => {
            this.$router.push("/events");
          })
          .catch(error => {
            console.log(error.response);
            alert(`Error: ${error}`);
          });
      } else {
        alert("You must log in to create an event!");
      }
    },
    rsvp(id) {
      const rsvpURI = `http://127.0.0.1:5000/api/v1/rsvp`;
      console.log(this.$store.state.userAccessToken);
      const rsvpData = {
        event_public_id: id
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
    }
  }
};
</script>

<style lang="scss" scoped>
.top-button {
  margin: 0.5rem;
}
</style>
