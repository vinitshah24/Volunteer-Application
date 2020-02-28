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
        <b-col>
          <b-card
            title="Volunteer Events"
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-list-group flush>
              <b-list-group-item><a href="#">Food Bank</a></b-list-group-item>
              <b-list-group-item>Habitat for Humanity</b-list-group-item>
              <b-list-group-item>Crisis Assitance Ministry</b-list-group-item>
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

export default {
  name: "Home",
  components: {
    // card: Card,
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
