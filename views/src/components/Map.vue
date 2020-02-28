<template>
  <div class="Map" />
</template>

<script>
import gmapsInit from "../utils/gmaps";

export default {
  name: "Map",
  components: {
    // card: Card
  },
  async mounted() {
    try {
      const google = await gmapsInit();
      const geocoder = new google.maps.Geocoder();
    //   var sanFrancisco = new google.maps.LatLng(37.774546, -122.433523);

      const map = new google.maps.Map(this.$el);

      const heatmapData = [
        new google.maps.LatLng(35.302, -80.897),
        new google.maps.LatLng(35.251, -80.857),
        new google.maps.LatLng(35.254, -80.857),
        new google.maps.LatLng(35.244, -80.857),
        new google.maps.LatLng(35.252, -80.857),
        new google.maps.LatLng(35.355, -80.897),
        new google.maps.LatLng(35.299, -80.857),
        new google.maps.LatLng(35.276, -80.857),
        new google.maps.LatLng(35.283, -80.857),
        new google.maps.LatLng(35.258, -80.857),
        new google.maps.LatLng(35.252, -80.857),
        new google.maps.LatLng(35.355, -80.897),
        new google.maps.LatLng(35.299, -80.857),
        new google.maps.LatLng(35.276, -80.857),
        new google.maps.LatLng(35.283, -80.857),
        new google.maps.LatLng(35.258, -80.857),
        new google.maps.LatLng(35.252, -80.857),
        new google.maps.LatLng(35.355, -80.897),
        new google.maps.LatLng(35.299, -80.857),
        new google.maps.LatLng(35.276, -80.857),
        new google.maps.LatLng(35.283, -80.857),
        new google.maps.LatLng(35.258, -80.857),
        new google.maps.LatLng(35.252, -80.857),
        new google.maps.LatLng(35.355, -80.897),
        new google.maps.LatLng(35.299, -80.857),
        new google.maps.LatLng(35.276, -80.857),
        new google.maps.LatLng(35.283, -80.857),
        new google.maps.LatLng(35.258, -80.857),
        new google.maps.LatLng(35.233, -80.857),
        new google.maps.LatLng(35.333, -80.857),
        new google.maps.LatLng(35.258, -80.857),
      ];
      var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData
      });

      var eventsMarkers = 
        new google.maps.Marker({
          position: new google.maps.LatLng(35.255045, -80.853747),
          title: "Test",
        });

      eventsMarkers.setMap(map)
      heatmap.setMap(map);

      var location;

      geocoder.geocode(
        { address: "Charlotte, North Carolina" },
        (results, status) => {
          if (status !== "OK" || !results[0]) {
            throw new Error(status);
          }
          console.log(results[0].geometry.location.lat());
          map.setCenter(results[0].geometry.location);
          map.fitBounds(results[0].geometry.viewport);
        }
      );

      console.log(location);
    } catch (error) {
      console.error(error);
    }
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