<template>
  <div class="charities">
    <b-container class="mh-50">
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
      <b-row></b-row>
    </b-container>
  </div>
</template>

<script>
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
      const baseURI = `https://api.data.charitynavigator.org/v2/Organizations?app_id=0de7ab2c&app_key=${process.env.VUE_APP_CHARITY}&pageSize=4&rated=true&state=NC`;
      this.$http.get(baseURI).then(result => {
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