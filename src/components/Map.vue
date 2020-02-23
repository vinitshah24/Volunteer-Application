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
        new google.maps.LatLng(37.782, -122.447),
        new google.maps.LatLng(37.782, -122.445),
        new google.maps.LatLng(37.782, -122.443),
        new google.maps.LatLng(37.782, -122.441),
        new google.maps.LatLng(37.782, -122.439),
        new google.maps.LatLng(37.782, -122.437),
        new google.maps.LatLng(37.782, -122.435),
        new google.maps.LatLng(37.785, -122.447),
        new google.maps.LatLng(37.785, -122.445),
        new google.maps.LatLng(37.785, -122.443),
        new google.maps.LatLng(37.785, -122.441),
        new google.maps.LatLng(37.785, -122.439),
        new google.maps.LatLng(37.785, -122.437),
        new google.maps.LatLng(37.785, -122.435)
      ];
      var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData
      });

      heatmap.setMap(map);

      var location;

      geocoder.geocode(
        { address: "San Francisco, California" },
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