<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col></b-col>
        <b-col md="8">
          <div>
            <gmap />
          </div>
        </b-col>
        <b-col></b-col>
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

export default {
  name: "Home",
  components: {
    // card: Card
    gmap: GMap
  }
  // async mounted() {
  //   try {
  //     const google = await gmapsInit();
  //     const geocoder = new google.maps.Geocoder();
  //     const map = new google.maps.Map(this.$el);

  //     geocoder.geocode(
  //       { address: "Mecklenberg County, North Carolina" },
  //       (results, status) => {
  //         if (status !== "OK" || !results[0]) {
  //           throw new Error(status);
  //         }

  //         map.setCenter(results[0].geometry.location);
  //         map.fitBounds(results[0].geometry.viewport);
  //       }
  //     );
  //   } catch (error) {
  //     console.error(error);
  //   }
  // }
};
</script>

<style scoped>
html,
body {
  margin: 0;
  padding: 0;
}
</style>
