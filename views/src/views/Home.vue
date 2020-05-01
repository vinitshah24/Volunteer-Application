<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col>
          <b-button @click="click" size="sm" variant="info">Toggle Heatmap</b-button>
        </b-col>
        <b-col md="8">
          <div>
            <gmap ref="gmap" />
          </div>
        </b-col>
        <b-col>
          <b-card title="Volunteer Events" tag="article" style="max-width: 20rem;" class="mb-2">
            <b-list-group flush>
              <b-list-group-item>
                <b-dropdown
                  id="dropdown-dropup"
                  dropup
                  text="Food Bank"
                  variant="outline-secondary"
                  class="m-2"
                >
                  <b-dropdown-item href="#">Join Event</b-dropdown-item>
                  <b-dropdown-item href="#">Invite Friends</b-dropdown-item>
                </b-dropdown>
              </b-list-group-item>
              <b-list-group-item>
                <b-dropdown
                  id="dropdown-dropup"
                  dropup
                  text="Habitat for Humanity"
                  variant="outline-secondary"
                  class="m-2"
                >
                  <b-dropdown-item href="#">Join Event</b-dropdown-item>
                  <b-dropdown-item href="#">Invite Friends</b-dropdown-item>
                </b-dropdown>
              </b-list-group-item>
              <b-list-group-item>
                <b-dropdown
                  id="dropdown-dropup"
                  dropup
                  text="Crisis Assitance Ministry"
                  variant="outline-secondary"
                  class="m-2"
                >
                  <b-dropdown-item href="#">Join Event</b-dropdown-item>
                  <b-dropdown-item href="#">Invite Friends</b-dropdown-item>
                </b-dropdown>
              </b-list-group-item>
              <b-list-group-item>
                <b-button variant="success">Create Event</b-button>
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
    return {};
  },
  components: {
    // card: Card,
    gmap: GMap
  },
  methods: {
    click: function() {
      this.$refs.gmap.toggleHeat();
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
