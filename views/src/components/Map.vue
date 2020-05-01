<template>
  <div class="Map" />
</template>

<script>
import gmapsInit from "../utils/gmaps";

export default {
  name: "Map",
  data() {
    return {
      loading: false,
      error: null,
      counties: this.$store.state.counties,
      geocoder: null,
      gmap: null,
      google: null,
      heatPoints: [],
      heatmap: null
    };
  },
  components: {},
  methods: {
    async getCounties() {
      console.log("Getting counties");
      this.loading = true;
      const requestOptions = {
        method: "GET",
        redirect: "follow"
      };
      const testResult = await fetch(
        "http://127.0.0.1:5000/api/v1/poverty/NC",
        requestOptions
      );
      const response = await testResult.text();
      console.log("Finished getting counties");
      // console.log(response);
      return response;
    },

    initializeMap() {
      console.log("Initializing map");
      this.gmap = new this.google.maps.Map(this.$el);
      console.log("map initialized");
    },

    async populateHeat(google) {
      console.log("in populate");
      let counties = this.counties;
      console.log(`in populate counties`);
      await counties.forEach(async county => {
        // console.log(county.region);
        this.heatPoints.push({
          location: new google.maps.LatLng(county.lat, county.lng),
          weight: county.value
        });
      });
      this.generateHeatmap();
    },
    generateHeatmap() {
      console.log("Generating Heatmap");
      // console.log(`Heatmaps points: ${this.heatPoints}`);
      // console.log(this.heatPoints);
      this.heatmap = new this.google.maps.visualization.HeatmapLayer({
        data: this.heatPoints,
        radius: 15
      });
      this.heatmap.setMap(this.gmap);
    },
    toggleHeat() {
      this.heatmap.setMap(this.heatmap.getMap() ? null : this.gmap);
    },

    toggleEvents() {
      if (!this.$store.state.eventsMarkers) {
        this.$store.commit("setEventsMarkers", []);
        this.$store.state.events.forEach((event, index) => {
          this.geocoder.geocode(
            { address: event.address },
            (results, status) => {
              if (status !== "OK" || !results[0]) {
                throw new Error(status);
              }
              this.$store.state.eventsMarkers.push(
                new this.google.maps.Marker({
                  position: new this.google.maps.LatLng(
                    results[0].geometry.location.lat(),
                    results[0].geometry.location.lng()
                  ),
                  title: event.name
                })
              );
              this.$store.state.eventsMarkers[index].setMap(this.gmap);
            }
          );
        });
      } else {
        this.$store.state.eventsMarkers.forEach(marker => {
          marker.setMap(marker.getMap() ? null : this.gmap);
        });
      }

      // console.log(
      //   `results from toggleEvents geocoder: ${results[0].geometry.location.lat()}`
      // );
    }
  },
  // var eventString =
  //   "<div><h4>Habitat For Humanity Event</h4>" +
  //   "<p>Come help hang drywall in our new homebuild</p></div>";

  // var eventsMarkers = new this.google.maps.Marker({
  //   position: new this.google.maps.LatLng(35.255146, -80.822402),
  //   title: "Test"
  // });
  //   // var infoWindow = new this.google.maps.InfoWindow({
  //   //   content: eventString
  //   // });
  //   // eventsMarkers.setMap(this.gmap);
  //   // eventsMarkers.addListener("click", function() {
  //   //   infoWindow.open(this.gmap, eventsMarkers);
  //   // });
  // }

  async created() {
    console.log("Created");
    if (!this.$store.state.counties) {
      console.log("Counties not stored, calling getCounties");
      let counties = JSON.parse(await this.getCounties());
      this.$store.commit("setCounties", counties);
      this.counties = this.$store.state.counties;
    }
    console.log("store has counties");
    console.log(this.$store);
    // console.log(`Counties collected: ${this.counties}`);
  },

  beforeMount() {},

  async mounted() {
    this.google = await gmapsInit();
    this.geocoder = await new this.google.maps.Geocoder();
    this.initializeMap();
    this.heatmaps = await this.populateHeat(this.google);

    console.log(`mounted`);

    // var eventString =
    //   "<div><h4>Habitat For Humanity Event</h4>" +
    //   "<p>Come help hang drywall in our new homebuild</p></div>";

    // var eventsMarkers = new this.google.maps.Marker({
    //   position: new this.google.maps.LatLng(35.255146, -80.822402),
    //   title: "Test"
    // });
    // var infoWindow = new this.google.maps.InfoWindow({
    //   content: eventString
    // });
    // eventsMarkers.setMap(this.gmap);
    // eventsMarkers.addListener("click", function() {
    //   infoWindow.open(this.gmap, eventsMarkers);
    // });

    var location;

    this.geocoder.geocode({ address: "North Carolina" }, (results, status) => {
      if (status !== "OK" || !results[0]) {
        throw new Error(status);
      }
      console.log(
        `results from NC geocoder: ${results[0].geometry.location.lat()}`
      );
      this.gmap.setCenter(results[0].geometry.location);
      this.gmap.fitBounds(results[0].geometry.viewport);
    });

    console.log(`location: ${location}`);
    let tester = "hello";
    this.$store.commit("setMap", tester);
    console.log(this.$store);
  }
};
</script>

<style lang="scss" scoped>
.Map {
  width: 100%;
  height: 90vh;
  margin: auto;
}
</style>