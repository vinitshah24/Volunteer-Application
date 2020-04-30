<template>
  <div class="charities">
    <h1 class="display-4" style="text-align: left">Donate to these worthy charities in your area</h1>

    <b-container v-for="rows in rowCount" :key="rows.id">
      <b-card-group deck>
        <b-col group deck v-for="column in numberOfColumns" :key="column.id">
          <b-card
            v-if="charities.length >= cardCount(rows, column)"
            :rating="cardCount(rows, column)"
            :title="charities[cardCount(rows, column) - 1].charityName"
            :sub-title="subTitle + charities[cardCount(rows, column) - 1].rating"
            :img-src="getImgUrl(charities, cardCount(rows, column) - 1)"
            img-alt="Image"
            img-top
            tag="article"
            style="height: 450px; margin: 25px 0px"
            class="mb-2"
          >
            <b-card-text>{{ charities[cardCount(rows, column) - 1].cause }}</b-card-text>

            <template v-slot:footer>
              <b-button :href="charities[column].charityNavigatorURL" variant="primary">Donate!</b-button>
            </template>
          </b-card>
        </b-col>
      </b-card-group>
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
      rating: 4,
      numberOfColumns: 3
    };
  },
  computed: {
    rowCount: function() {
      return Math.floor((this.charities.length - 1) / this.numberOfColumns) + 1;
    }
  },
  methods: {
    getImgUrl: function(charity, index) {
      return require(`@/assets/images/${charity[index].cause
        .split(/[ ,]+/)[0]
        .toLowerCase()}.png`);
    },
    cardCount: function(rows, columns) {
      return (rows - 1) * this.numberOfColumns + columns;
    },
    fetchCharities: function() {
      const baseURI = `http://127.0.0.1:5000/api/v1/charities/NC`;
      this.$http
        .get(baseURI, {
          method: "GET",

          headers: {
            Authorization:
              "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODgxMzM2NDksIm5iZiI6MTU4ODEzMzY0OSwianRpIjoiNDNmODVkOWYtOGUzOC00OGEyLTgwNDMtNjdiY2YyZGI2Y2IzIiwiZXhwIjoxNTg4MTM0NTQ5LCJpZGVudGl0eSI6ImJlY2RiYmFmLTE0MGUtNDUyNC04NjM5LWExMjZlYjI0ZTk5ZSIsImZyZXNoIjp0cnVlLCJ0eXBlIjoiYWNjZXNzIn0.7FJi_ljS9S-CqSK2nDu-WLqY62zoUV8z9yVM07z6Vcw"
          }
        })
        .then(result => {
          console.log("request made");
          console.log(result);
          this.charities = result.data.charities;
          console.log(this.charities);
        });
    }
  },
  async beforeMount() {
    try {
      await this.fetchCharities();
    } catch (error) {
      console.log(error);
    }
  },
  async mounted() {
    // try {
    //   await this.fetchCharities();
    // } catch (error) {
    //   console.log(error);
    // }
  }
};
</script>

<style scoped>
img.card-img-top {
  height: 250px;
}
</style>