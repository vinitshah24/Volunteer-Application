<template>
  <div class="charities">
    <b-container>
      <b-row>
        <b-col v-for="charity in charities" :key="charity.ein">
          <b-card
            :rating="charity.currentRating.rating"
            :title="charity.charityName"
            :sub-title="subTitle + charity.currentRating.rating"
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            style="max-width: 20rem;"
            class="mb-2"
          >
            <b-card-text>{{charity.mission.toString()}}</b-card-text>

            <b-button :href="charity.charityNavigatorURL" variant="primary">Donate!</b-button>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// var request = require("request");
// var reqy = {
//   method: "GET",
//   url: "http://127.0.0.1:5000/api/v1/user\n",
//   headers: {
//     Authorization:
//       "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODQ3NDY0MDIsIm5iZiI6MTU4NDc0NjQwMiwianRpIjoiYmU2Yjk0ZWEtNWIxYS00OWM0LTliYjgtNGVkOGQ4MzM2NDBjIiwiZXhwIjoxNTg0NzQ3MzAyLCJpZGVudGl0eSI6IjBjZjBjNmE3LTBmYWMtNGE4ZS1hMGJhLWY1YzFiM2M1YjU0ZCIsImZyZXNoIjp0cnVlLCJ0eXBlIjoiYWNjZXNzIn0.oGBCfh8RFNbdS4Q_CSHtQ6Rk1hO5uLqB-YD9LKY2944"
//   }
// };
// request(options, function(error, response) {
//   if (error) throw new Error(error);
//   console.log(response.body);
// });

export default {
  name: "Charities",
  data() {
    return {
      charities: [],
      title: "",
      subTitle: "Current rating: ",
      rating: 4
    };
  },
  methods: {
    fetchCharities: function() {
      const baseURI = `http://127.0.0.1:5000/api/v1/user`;
      this.$http.get(baseURI, {
  method: "GET",
  
  headers: {
    Authorization:
      "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODQ3NjIxNTksIm5iZiI6MTU4NDc2MjE1OSwianRpIjoiNGUyMDE1MmUtOWJkNC00ZjJlLWJjM2EtY2M5MTY4MDAyMjlhIiwiZXhwIjoxNTg0NzYzMDU5LCJpZGVudGl0eSI6IjBjZjBjNmE3LTBmYWMtNGE4ZS1hMGJhLWY1YzFiM2M1YjU0ZCIsImZyZXNoIjp0cnVlLCJ0eXBlIjoiYWNjZXNzIn0.NvPizSZB_SZD2glGGO4Zg3QUHLVLDj8u_Plgz7NPC4A"
  }
}).then(result => {
        console.log("request made");
        console.log(result);
        this.charities = result.data;
        console.log(this.charities);
      });
    }
  },
  async mounted() {
    try {
      await this.fetchCharities();
    } catch (error) {
      console.log(error);
    }
  }
};
</script>
