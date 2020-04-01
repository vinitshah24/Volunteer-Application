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

      var requestOptions = {
        method: "GET",
        redirect: "follow"
      };

      var data;

      fetch("http://127.0.0.1:5000/api/v1/poverty/NC", requestOptions)
        .then(response => response.text())
        .then(result => {
          data = JSON.parse(result).NC.slice(0, 2);
          var filt = data.map(county =>
            geocoder.geocode({ address: county.region }, (results, status) => {
              if (status !== "OK" || !results[0]) {
                throw new Error(status);
              }
              // console.log(results[0].geometry)
              console.log(`${county.region} lat: ${results[0].geometry.location.lat()}\n ${county.region} long: ${results[0].geometry.location.lng()}`);
              // map.setCenter(results[0].geometry.location);
              // map.fitBounds(results[0].geometry.viewport);
            })
          );
          console.log(filt);
          // console.log(data);
          // console.log(
          //   geocoder.geocode(
          //     { address: "Mecklenburg County, North Carolina" },
          //     (results, status) => {
          //       if (status !== "OK" || !results[0]) {
          //         throw new Error(status);
          //       }
          //       console.log(results[0].geometry.location.lat())
          //     }
          //   )
          // );
        })
        .catch(error => console.log("error", error));

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

        new google.maps.LatLng(35.311, -80.897),
        new google.maps.LatLng(35.486, -80.857),
        new google.maps.LatLng(35.487, -80.857),
        new google.maps.LatLng(35.2654, -80.857),
        new google.maps.LatLng(35.3565, -80.857),
        new google.maps.LatLng(35.298, -80.897),
        new google.maps.LatLng(35.299, -80.857),
        new google.maps.LatLng(35.299, -80.856),
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
        new google.maps.LatLng(35.258, -80.857)
      ];
      var heatmap = new google.maps.visualization.HeatmapLayer({
        data: heatmapData
      });

      var eventString =
        "<div><h4>Habitat For Humanity Event</h4>" +
        "<p>Come help hang drywall in our new homebuild</p></div>";

      var eventsMarkers = new google.maps.Marker({
        position: new google.maps.LatLng(35.255146, -80.822402),
        title: "Test"
      });
      var infoWindow = new google.maps.InfoWindow({
        content: eventString
      });
      eventsMarkers.setMap(map);
      eventsMarkers.addListener("click", function() {
        infoWindow.open(map, eventsMarkers);
      });
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