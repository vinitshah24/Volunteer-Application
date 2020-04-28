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
      counties: [],
      latlangs: [],
      geocoder: null,
      gmap: null,
      google: null,
      heatPoints: [],
      heatmap: null,
      jsonDataTest: {}
    };
  },
  components: {
    // card: Card
  },
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
      console.log(response);
      return response;
    },

    initializeMap() {
      console.log("Initializing map");
      this.gmap = new this.google.maps.Map(this.$el);
      console.log("map initialized");
    },

    async populateHeat(geocoder, google) {
      console.log("in populate");
      let counties = this.counties;
      console.log(`in populate counties: ${counties}`);
      counties.forEach(async county => {
        console.log(county.region);
        // this.jsonDataTest[county.code] = {};
        // this.jsonDataTest[county.code]["region"] = county.region;
        // console.log(this.jsonDataTest);
        await this.heatPoints.push({
          location: new google.maps.LatLng(county.lat, county.lng),
          weight: county.value
        });
        this.generateHeatmap();
        // await geocoder.geocode(
        //   { address: county.region },
        //   (results, status) => {
        //     console.log("calling geocoder");
        //     if (status !== "OK" || !results[0]) {
        //       new Error(status);
        //     }
        //     console.log(results[0]);
        //     this.jsonDataTest[county.code][
        //       "lat"
        //     ] = results[0].geometry.location.lat();
        //     this.jsonDataTest[county.code][
        //       "lng"
        //     ] = results[0].geometry.location.lng();
        //     // console.log(tempy);
        //     console.log(this.jsonDataTest);
        //     console.log(`status OK: ${status}`);
        //     this.heatPoints.push({
        //       location: new google.maps.LatLng(
        //         results[0].geometry.location.lat(),
        //         results[0].geometry.location.lng()
        //       ),
        //       weight: county.value
        //     });
        //     console.log(JSON.stringify(this.jsonDataTest));

        //     console.log(`heatpoints at end of pop: ${this.heatPoints}`);

        //     this.generateHeatmap();
        //   }
        // );
      });
      // await geocoder.geocode({ address: counties[0] }, (results, status) => {
      //   console.log("calling geocoder");
      //   if (status !== "OK" || !results[0]) {
      //     new Error(status);
      //   }
      //   console.log(`status OK: ${status}`);
      //   this.heatPoints.push({
      //     location: new google.maps.LatLng(
      //       results[0].geometry.location.lat(),
      //       results[0].geometry.location.lng()
      //     ),
      //     weight: 2
      //   });
      //   console.log(`heatpoints at end of pop: ${this.heatPoints}`);
      //   this.generateHeatmap();
      // });

      // console.log(`Try this:`);
      // this.generateHeatmap();

      // return new Promise((resolve, reject) => {
      //   let heats = [];
      //   this.counties.forEach(county =>
      //     geocoder.geocode({ address: county }, (results, status) => {
      //       if (status !== "OK" || !results[0]) {
      //         reject(status);
      //       }
      //       heats.push(
      //         new google.maps.LatLng(
      //           results[0].geometry.location.lat(),
      //           results[0].geometry.location.lng()
      //         )
      //       );
      //       console.log(heats);
      //     })
      //   );
      //   resolve(heats);
      // }
      // );

      // this.counties.map(county =>
      // geocoder.geocode({ address: county }, (results, status) => {
      //   if (status !== "OK" || !results[0]) {
      //     throw new Error(status);
      //   } else {
      //     console.log(results[0].geometry.location.lng());
      //     this.heatmaps.push(
      //       new google.maps.LatLng(
      //         results[0].geometry.location.lat(),
      //         results[0].geometry.location.lng()
      //       )
      //     );
      //     console.log(this.heatmaps);
      //     // new google.maps.LatLng(35.302, -80.897)
      //     // console.log(`results from geocoder: ${JSON.stringify(results[0].geometry.location)}`);
      //   }
      //   })
      // );
      // this.heatmaps.push(
      //   new google.maps.LatLng(36.0117388, -81.20781640000001)
      // );

      // this.heatmaps.push(
      //   new google.maps.LatLng(35.8974199, -81.20781640000001)
      // );
    },
    generateHeatmap() {
      console.log("Generating Heatmap");
      console.log(`Heatmaps points: ${this.heatPoints}`);
      console.log(this.heatPoints);
      this.heatmap = new this.google.maps.visualization.HeatmapLayer({
        data: this.heatPoints,
        radius: 15
      });
      this.heatmap.setMap(this.gmap);
    }
  },

  async created() {
    console.log("Created");
    // var temp = await this.getCounties();
    this.counties = JSON.parse(await this.getCounties());
    console.log(`Counties collected: ${this.counties}`);

    // console.log(JSON.parse(temp))
  },

  beforeMount() {},

  async mounted() {
    this.google = await gmapsInit();
    this.geocoder = await new this.google.maps.Geocoder();
    this.initializeMap();
    this.heatmaps = await this.populateHeat(this.geocoder, this.google);
    // console.log(this.heatmaps);

    // let heatmap2 = [];
    console.log(`mounted: ${this.counties}`);
    // try {
    //   const google = await gmapsInit();

    //   this.counties.map(county =>
    //     geocoder.geocode({ address: county }, (results, status) => {
    //       if (status !== "OK" || !results[0]) {
    //         throw new Error(status);
    //       } else {
    //         console.log(results[0].geometry.location.lat());
    //         this.latlangs.push(
    //           new google.maps.LatLng(
    //             results[0].geometry.location.lat(),
    //             results[0].geometry.location.lng()
    //           )
    //         );
    //         console.log(this.latlangs);
    //         // new google.maps.LatLng(35.302, -80.897)
    //         // console.log(`results from geocoder: ${JSON.stringify(results[0].geometry.location)}`);
    //       }
    //     })
    //   );
    // console.log(heatmap2)
    console.log(`this is latlngs: ${this.latlangs}`);
    // var requestOptions = {
    //   method: "GET",
    //   redirect: "follow"
    // };
    // const testResult = await fetch(
    //   "http://127.0.0.1:5000/api/v1/poverty/NC",
    //   requestOptions
    // );
    // const texty = await testResult.text();
    // let data = JSON.parse(texty).NC.slice(0, 2);
    // console.log("this is data:" + data);
    // heatmap2 = data.map(county =>
    //   geocoder.geocode({ address: county.region }, (results, status) => {
    //     if (status !== "OK" || !results[0]) {
    //       throw new Error(status);
    //     }

    //   })
    // );
    // console.log("heatmaps:" + heatmap2)

    //   console.log(data);
    // heatmap2 = data.map(county =>
    //   geocoder.geocode({ address: county.region }, (results, status) => {
    //     if (status !== "OK" || !results[0]) {
    //       throw new Error(status);
    //     }
    //     google.maps.LatLng(results[0].geometry.location.lat(), results[0].geometry.location.lng())
    //       // console.log(results[0].geometry)
    //       console.log(
    //         `${
    //           county.region
    //         } lat: ${results[0].geometry.location.lat()}\n ${
    //           county.region
    //         } long: ${results[0].geometry.location.lng()}`
    //       );
    //       // map.setCenter(results[0].geometry.location);
    //       // map.fitBounds(results[0].geometry.viewport);
    //     })
    //   );

    //   // console.log(data);
    //   // console.log(
    //   //   geocoder.geocode(
    //   //     { address: "Mecklenburg County, North Carolina" },
    //   //     (results, status) => {
    //   //       if (status !== "OK" || !results[0]) {
    //   //         throw new Error(status);
    //   //       }
    //   //       console.log(results[0].geometry.location.lat())
    //   //     }
    //   //   )
    //   // );
    // })
    // .catch(error => console.log("error", error));

    //   var sanFrancisco = new google.maps.LatLng(37.774546, -122.433523);
    // const heatmapData = [
    //   new google.maps.LatLng(35.302, -80.897),
    //   new google.maps.LatLng(35.251, -80.857),
    //   new google.maps.LatLng(35.254, -80.857),
    //   new google.maps.LatLng(35.244, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.233, -80.857),
    //   new google.maps.LatLng(35.333, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),

    //   new google.maps.LatLng(35.311, -80.897),
    //   new google.maps.LatLng(35.486, -80.857),
    //   new google.maps.LatLng(35.487, -80.857),
    //   new google.maps.LatLng(35.2654, -80.857),
    //   new google.maps.LatLng(35.3565, -80.857),
    //   new google.maps.LatLng(35.298, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.299, -80.856),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.252, -80.857),
    //   new google.maps.LatLng(35.355, -80.897),
    //   new google.maps.LatLng(35.299, -80.857),
    //   new google.maps.LatLng(35.276, -80.857),
    //   new google.maps.LatLng(35.283, -80.857),
    //   new google.maps.LatLng(35.258, -80.857),
    //   new google.maps.LatLng(35.233, -80.857),
    //   new google.maps.LatLng(35.333, -80.857),
    //   new google.maps.LatLng(35.258, -80.857)
    // ];
    // var heatmap = new this.google.maps.visualization.HeatmapLayer({
    //   data: this.heatmaps
    // });

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
    // this.heatmap.setMap(this.gmap);

    var location;

    this.geocoder.geocode(
      { address: "Mecklenburg County, North Carolina" },
      (results, status) => {
        if (status !== "OK" || !results[0]) {
          throw new Error(status);
        }
        console.log(
          `results from Clt geocoder: ${results[0].geometry.location.lat()}`
        );
        this.gmap.setCenter(results[0].geometry.location);
        this.gmap.fitBounds(results[0].geometry.viewport);
      }
    );

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