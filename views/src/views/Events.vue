<template>
  <div>
    <h1>Upcoming Events</h1>
    <div>
      <b-tabs content-class="mt-3">
        <b-tab v-if="this.$store.state.loggedIn" title="My Events" active>
          <b-table
            striped
            hover
            :items="userEvents"
            :fields="fields"
            v-if="userEvents && userEvents.length >= 1"
          ></b-table>
        </b-tab>
        <b-tab title="All Events">
          <b-table striped hover :items="allEvents" :fields="fields" v-if="allEvents.length">
            <template v-slot:cell(actions)="row">
              <b-button
                size="sm"
                @click="info(row.item, row.index, $event.target, 'allEvents')"
                class="mr-1"
              >Details</b-button>
              <!-- <b-button
                size="sm"
                class="mr-1"
                @click="row.toggleDetails"
              >{{ row.detailsShowing ? 'Hide' : 'Show' }} Details</b-button> -->
              <b-button
                v-if="$store.state.loggedIn && $store.state.user.eventsHash"
                size="sm"
                :variant="$store.state.user.eventsHash.hasOwnProperty(row.item.public_id) ? 'danger' : 'success'"
                @click="clickEvent(row.item.public_id)"
                class="mr-1"
                style="width:65px"
              >{{$store.state.user.eventsHash.hasOwnProperty(row.item.public_id) ? 'Leave' : 'Join'}}</b-button>
            </template>

            <template v-slot:row-details="row">
              <b-card>
                <ul>
                  <li v-for="(value, key) in row.item" :key="key">{{ key }}: {{ value }}</li>
                </ul>
              </b-card>
            </template>
          </b-table>
          <b-modal :id="infoModal.id" :title="infoModal.title" ok-only @hide="resetInfoModal">
            <b-container>
              <b-row>
                <b-col cols="3">
                  <h6>When:</h6>
                </b-col>
                <b-col cols>
                  <p>{{infoModal.content.date}} at {{infoModal.content.time}}</p>
                </b-col>
              </b-row>
              <b-row>
                <b-col cols="3">
                  <h6>Where:</h6>
                </b-col>
                <b-col cols>
                  <p>{{infoModal.content.address}}</p>
                </b-col>
              </b-row>
              <b-row>
                <b-col cols="3">
                  <h6>What:</h6>
                </b-col>
                <b-col cols>
                  <p>{{infoModal.content.details}}</p>
                </b-col>
              </b-row>
              <b-row>
                <b-col cols="3">
                  <h6>Organizer:</h6>
                </b-col>
                <b-col cols>
                  <p>{{infoModal.content.first_name}} {{infoModal.content.last_name}} ({{infoModal.content.username}})</p>
                </b-col>
              </b-row>
            </b-container>
          </b-modal>
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
      fields: [
        { key: "name", label: "Event Name" },
        { key: "category", sortable: true },
        "address",
        {
          key: "county",
          sortable: true,
          sortFormatted: true,
          formatter: (value, key, item) => {
            return item.county + ", " + item.state;
          }
        },
        {
          key: "date",
          label: "Date",
          sortable: true,
          formatter: (value, key, item) => {
            let date = new Date(item.date);
            let days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
            let months = [
              "Jan",
              "Feb",
              "March",
              "April",
              "May",
              "June",
              "July",
              "Aug",
              "Sept",
              "Oct",
              "Nov",
              "Dec"
            ];
            return (
              days[date.getDay()] +
              ", " +
              months[date.getMonth()] +
              " " +
              date.getDate() +
              ", " +
              date.getFullYear()
            );
          }
        },

        {
          key: "username",
          label: "Organizer",
          sortable: true
        },

        { key: "actions", label: "" }
      ],
      // allEvents: this.$store.state.events,
      items: [
        { age: 40, first_name: "Dickerson", last_name: "Macdonald" },
        { age: 21, first_name: "Larsen", last_name: "Shaw" },
        { age: 89, first_name: "Geneva", last_name: "Wilson" },
        { age: 38, first_name: "Jami", last_name: "Carney" }
      ],
      userEvents: [],
      infoModal: {
        id: "info-modal",
        title: "",
        content: ""
      }
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
          this.formatFields(this.allEvents);
          // this.allEvents.forEach(event => {
          //   event.address = `${event.address}, ${event.state}`;
          // });
          // if (this.$store.state.loggedIn) {
          //   console.log("user logged in");
          //   this.getRSVPs();
          // }
        })
        .then(() => {
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
      console.log("calling RSVPs");
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
          // console.log(result.data.events.reduce((map, obj) => (map[obj.public_id] = obj, map), {}));
          this.$store.commit(
            "setUserEventsHash",
            result.data.events.reduce(
              (map, obj) => ((map[obj.public_id] = obj), map),
              {}
            )
          );
          this.$store.commit("setUserEvents", result.data.events);

          this.userEvents = this.$store.state.user.events;
          console.log(this.$store.state.user);
        })
        .then(() => {
          this.userEvents = this.$store.state.user.events;
          console.log(this.userEvents);
          this.formatFields(this.userEvents);
        })
        .catch(error => {
          console.log(error.config);
        })
        .finally(() => {});
    },
    addRSVP(id) {
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
          this.getEvents();
        })
        .catch(error => {
          console.log(error.response);
        });
    },
    deleteRSVP(id) {
      console.log(id);
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      myHeaders.append(
        "Authorization",
        `Bearer ${this.$store.state.userAccessToken}`
      );
      myHeaders.append("Content-Type", "application/json");

      var raw = JSON.stringify({
        event_public_id: id
      });

      var requestOptions = {
        method: "DELETE",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
      };

      fetch("http://127.0.0.1:5000/api/v1/rsvp", requestOptions)
        .then(this.getEvents())
        .then(result => console.log(result))
        .catch(error => console.log("error", error));
    },
    clickEvent(id) {
      console.log(id);
      if (
        Object.prototype.hasOwnProperty.call(
          this.$store.state.user.eventsHash,
          id
        )
      ) {
        console.log("it's true");
        this.deleteRSVP(id);
      } else {
        console.log("it is not true");
        this.addRSVP(id);
      }
    },
    formatFields(arrs) {
      arrs.forEach(event => {
        event.address = `${event.address}, ${event.state}`;
      });
    },
    info(item, index, button, context) {
      this.infoModal.title = this[context][index].name;
      this.infoModal.content = item;
      console.log(item);
      this.infoModal.content.time = this.timeFormatter(item.time);
      this.infoModal.content.date = this.dateFormatter(item.date);
      this.$root.$emit("bv::show::modal", this.infoModal.id, button);
    },
    resetInfoModal() {
      this.infoModal.title = "";
      this.infoModal.content = "";
    },
    timeFormatter(item) {
      let arr = item.split(":");
      console.log(arr);
      if (arr.length >= 3) {
        let m = arr[0] < 12 ? "AM" : "PM";
        let time;
        console.log(m);
        console.log(time);
        if (+arr[0] === 0 || +arr[0] === 12) {
          time = `12:${arr[1]} ${m}`;
        } else if (m === "PM") {
          time = `${+arr[0] - 12}:${arr[1]} ${m}`;
        } else {
          time = `${arr[0]}:${arr[1]} ${m}`;
        }
        return time;
      } else {
        return item;
      }
    },
    dateFormatter(item) {
      let date = new Date(item);
      let days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"];
      let months = [
        "Jan",
        "Feb",
        "March",
        "April",
        "May",
        "June",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec"
      ];
      return (
        days[date.getDay()] +
        ", " +
        months[date.getMonth()] +
        " " +
        date.getDate() +
        ", " +
        date.getFullYear()
      );
    }
  },
  async created() {
    console.log("Events Created");
    await this.getEvents();
  },
  async mounted() {
    this.totalRows = this.items.length;
    console.log("Events Mounted");
    console.log(this.userEvents);
  }
};
</script>

<style lang="scss" scoped>
</style>