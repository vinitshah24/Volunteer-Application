<template>
  <div>
    <h1>Upcoming Events</h1>
    <b-table striped hover :items="events" :fields="fields" v-if="events.length"></b-table>
    <div>
      <b-button variant="success" v-on:click="createEvent">Create Event</b-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      fields: ["name", "category", "details", "address", "date", "time"],
      events: [
        {
          name: "Event 3",
          category: "twt",
          details: "segbc",
          address: "Chwgearlotte",
          county: "Unwggion",
          state: "NCwegw",
          date: "2021-02-24",
          time: "02:02:00"
        }
      ],
      items: [
        { age: 40, first_name: "Dickerson", last_name: "Macdonald" },
        { age: 21, first_name: "Larsen", last_name: "Shaw" },
        { age: 89, first_name: "Geneva", last_name: "Wilson" },
        { age: 38, first_name: "Jami", last_name: "Carney" }
      ]
    };
  },
  methods: {
    async getEvents() {
      const eventsURI = `http://127.0.0.1:5000/api/v1/events`;
      this.$http
        .get(eventsURI)
        .then(result => {
          console.log(result);
          this.events = result.data.events;

          this.events.forEach(event => {
            event.address = `${event.address}, ${event.state}`;
          });
        })
        .catch(error => {
          console.log(error);
        })
        .finally(() => {});
    },
    createEvent() {
      const createEventURI = `http://127.0.0.1:5000/api/v1/event`;
      console.log(this.$root.$router.app.$children[0].accessToken);
      this.$http
        .post(createEventURI, {
          data: {
            name: "Volunteering",
            category: "Education",
            details: "Read to kids",
            address: "Charlotte",
            county: "Mecklenburg",
            state: "NC",
            date: "2021-02-24",
            time: "02:02:00"
          },
          headers: {
            Authorization: `Bearer ${this.$root.$router.app.$children[0].accessToken}`
          }
        })
        .then(result => {
          console.log(result);
        })
        .catch(error => {
          console.log(error);
          alert("You must log in to create an event!");
        })
        .finally(this.getEvents());
    }
  },
  async mounted() {
    this.getEvents();
  }
};
</script>

<style lang="scss" scoped>
</style>