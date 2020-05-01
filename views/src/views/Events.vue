<template>
  <div>
    <h1>Upcoming Events</h1>
    <div>
      <b-tabs content-class="mt-3">
        <b-tab v-if="this.$store.state.loggedIn" title="My Events" active>
          <b-table striped hover :items="userEvents" :fields="fields" v-if="userEvents && userEvents.length > 1"></b-table>
        </b-tab>
        <b-tab title="All Events">
          <b-table striped hover :items="allEvents" :fields="fields" v-if="allEvents.length"></b-table>
        </b-tab>
      </b-tabs>
    </div>
    <div>
      <b-button variant="success" v-on:click="toCreateEvent">Create Event</b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fields: ["name", "category", "details", "address", "date", "time"],
      // allEvents: this.$store.state.events,
      items: [
        { age: 40, first_name: "Dickerson", last_name: "Macdonald" },
        { age: 21, first_name: "Larsen", last_name: "Shaw" },
        { age: 89, first_name: "Geneva", last_name: "Wilson" },
        { age: 38, first_name: "Jami", last_name: "Carney" }
      ],
      userEvents: []
    };
  },
  computed: {
    allEvents: function() {
      return this.$store.state.events;
    }
  },
  methods: {
    async getEvents() {
      const eventsURI = `http://127.0.0.1:5000/api/v1/events`;
      this.$http
        .get(eventsURI)
        .then(result => {
          // console.log(result.data.events);
          this.$store.commit("setEvents", result.data.events);

          this.allEvents.forEach(event => {
            event.address = `${event.address}, ${event.state}`;
          });
          if (this.$store.state.loggedIn) {
            console.log("user logged in");
            this.getRSVPs();
          }
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {});
    },
    createEvent() {
      const createEventURI = `http://127.0.0.1:5000/api/v1/event`;
      console.log(this.$store.state.userAccessToken);
      const eventData = {
        name: "Volunteering",
        category: "Education",
        details: "Read to kids",
        address: "Charlotte",
        county: "Mecklenburg",
        state: "NC",
        date: "2021-02-24",
        time: "02:02:00"
      };
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.userAccessToken}`
        }
      };
      if (this.$store.state.loggedIn) {
        this.$http
          .post(createEventURI, eventData, config)
          .then(result => {
            console.log(result);
            this.getEvents();
          })
          .catch(error => {
            console.log(error.result);
          });
      } else {
        alert("You must log in to create an event!");
      }
    },
    toCreateEvent() {
      if (this.$store.state.loggedIn) {
        this.$router.replace("/create");
      } else {
        alert("You must log in to create an event!");
      }
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
          this.$store.commit("setUserEvents", result.data.events);
          this.userEvents = this.$store.state.user.events;
          console.log(this.$store.state.user);
        })
        .catch(error => {
          console.log(error.config);
        })
        .finally(() => {});
    }
  },
  async created() {
    console.log("Events Created");
    await this.getEvents();
  },
  async mounted() {
    console.log("Events Mounted");
    console.log(this.userEvents);
  }
};
</script>

<style lang="scss" scoped>
</style>