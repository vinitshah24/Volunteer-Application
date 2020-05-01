<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col md="1">
          <b-button @click="click" class="mb-4" size="sm" variant="info">Toggle Heatmap</b-button>
          <b-button @click="click" size="sm" variant="info">Toggle Events</b-button>
        </b-col>
        <b-col md="8">
          <div>
            <gmap ref="gmap" />
          </div>
        </b-col>
        <b-col md="3"  style="max-height: 40rem; overflow-y: scroll">
          <b-card title="Upcoming Events" tag="article" class="mb-2">
            <b-container>
              <b-row v-for="event in $store.state.events" :key="event.id">
                <b-card
                  bg-variant="info"
                  class="w-100 mb-2 text-left"
                  :header="event.name"
                  header-tag="header"
                  text-variant="white"
                >
                  <template class="d-flex w-100 justify-content-between" v-slot:header>
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">{{ event.name }}</h5>
                      <small v-if="dateCalc(event.date) >= 0">In {{ dateCalc(event.date) }} Days</small>
                      <small
                        v-if="dateCalc(event.date) < 0"
                      >{{ (-1)*dateCalc(event.date) }} Days Ago</small>
                    </div>
                  </template>
                  
                  <p class="text-left mb-0">{{ event.address.split(',')[1] }}, {{ event.state }}</p>
                  <p class="text-left">{{ dateFormat(new Date(event.date)) }}</p>

                  <p class="mb-1 text-center">{{ event.details }}</p>
                </b-card>
              </b-row>
            </b-container>
            <b-list-group>
              <!-- <b-list-group-item class="mb-4" v-for="event in $store.state.events" :key="event.id">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">{{ event.name }}</h5>
                  <small v-if="dateCalc(event.date) >= 0">In {{ dateCalc(event.date) }} Days</small>
                  <small v-if="dateCalc(event.date) < 0">{{ (-1)*dateCalc(event.date) }} Days Ago</small>
                </div>
                <p class="mb-1">{{ event.details }}</p>
              </b-list-group-item>-->
              <b-list-group-item href="#" active class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small>3 days ago</small>
                </div>

                <p
                  class="mb-1"
                >Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>

                <small>Donec id elit non mi porta.</small>
              </b-list-group-item>

              <b-list-group-item href="#" class="flex-column align-items-start">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small class="text-muted">3 days ago</small>
                </div>

                <p
                  class="mb-1"
                >Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>

                <small class="text-muted">Donec id elit non mi porta.</small>
              </b-list-group-item>
            </b-list-group>

            <b-card-text></b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>




<script>
// Get map a normal size!
// Add cols on either side

// @ is an alias to /src
// import Card from "@/components/Card.vue";
import GMap from "@/components/Map.vue";
// import Card from "@/components/Card.vue";
console.log(process.env.VUE_APP_MAP);
export default {
  name: "Home",
  data() {
    return {
      events: [
        {
          name: "Volunteering",
          category: "Education",
          details: "Read to kids",
          address: "Charlotte",
          county: "Mecklenburg",
          state: "NC",
          date: "2021-02-24",
          time: "02:02:00"
        },
        {
          name: "Noodles",
          category: "Education",
          details: "Read to kids",
          address: "Charlotte",
          county: "Mecklenburg",
          state: "NC",
          date: "2020-02-24",
          time: "02:02:00"
        },
        {
          name: "Bingo",
          category: "Education",
          details: "Read to kids",
          address: "Charlotte",
          county: "Mecklenburg",
          state: "NC",
          date: "2021-02-24",
          time: "02:02:00"
        }
      ],
      tempDate: ""
    };
  },
  components: {
    // card: Card,
    gmap: GMap
  },
  methods: {
    click: function() {
      this.$refs.gmap.toggleHeat();
    },
    dateCalc: function(date1) {
      let today = new Date();
      let target = new Date(date1);
      let millisecondsPerDay = 24 * 60 * 60 * 1000;
      return Math.round((target - today) / millisecondsPerDay);
    },
    dateFormat: function(date1) {
      let days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
      ];
      let months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      ];
      let date = new Date(date1);
      return `${days[date.getDay()]}, ${
        months[date.getMonth()]
      } ${date.getDate()}, ${date.getFullYear()}`;
    }
  },
  async created() {
    const requestOptions = {
      method: "GET",
      redirect: "follow"
    };
    const testResult = await fetch(
      "http://127.0.0.1:5000/api/v1/events",
      requestOptions
    );
    const response = await testResult.text();
    this.$store.commit("setEvents", JSON.parse(response)["events"]);
    // console.log(JSON.parse(response));
    console.log(this.$store.state.events);
  }
};
</script>

<style scoped>
html,
body {
  margin: 0;
  padding: 0;
}
</style>
