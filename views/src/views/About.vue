<template>
  <div>
    <div id="carousel-div">
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        background="#ababab"
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Text slides with image -->
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=52"></b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54"></b-carousel-slide>

        <!-- Slides with image only -->
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

        <!-- Slides with img slot -->
        <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <b-carousel-slide>
          <template v-slot:img>
            <img
              class="d-block img-fluid w-100"
              height="100%"
              src="https://picsum.photos/1024/480/?image=55"
              alt="image slot"
            />
          </template>
        </b-carousel-slide>
      </b-carousel>
    </div>
    <b-container fluid>
      <b-card class="content-card">
        <b-card-text>
          <b-row>
            <b-col cols="3">
              <b-img left src="https://i.picsum.photos/id/455/300/300.jpg" alt="problem image"></b-img>
            </b-col>
            <b-col class="text-left">
              <h2>Our Mission</h2>
              <p>At Helpdesk Hero Co. we're on a mission to serve underrepresented communities through charitably giving our time and resources!</p>
              <p>
                Homelessness and poverty are prominent issues in the Charlotte metro area
                and in surrounding North Carolina communities.
              </p>
              <p>Our platform aims to connect those who want to better their communities to those who need their time and resources</p>
              <p>
                <em>Leverage our service to:</em>
                <br />Volunteer for different community-related events
                <br />Donate money to various causes
                <br />Become better educated to understand the impact your actions have on your community
              </p>
            </b-col>
            <b-col cols="2"></b-col>
          </b-row>
        </b-card-text>
      </b-card>
    </b-container>
    <b-container fluid class="mt-2">
      <b-card class="content-card">
        <b-card-text>
          <b-row>
            <b-col cols="3"></b-col>
            <b-col class="text-left">
              <h2>Our Service</h2>
              <p>
                <em>To combat this, we have designed a self service portal for our volunteers to:</em>
              </p>
              <p>Scout out where where poverty is most prominent in North Carolina</p>
              <p>Plan and organize volunteer events</p>
              <p>Make an impact in the community through personal initiatives</p>
              <p>Donate to a list of different charities and causes</p>
            </b-col>
            <b-col cols="2">
              <b-img right src="https://i.picsum.photos/id/48/300/300.jpg" alt="Website image"></b-img>
            </b-col>
          </b-row>
        </b-card-text>
      </b-card>
    </b-container>

    <b-container fluid>
      <b-card class="mt-2" title="Meet the Team">
        <b-row>
          <b-card-group deck class="mx-5">
            <b-card
              img-src="@/assets/images/vinit.jpg"
              img-alt="Card image"
              bottom
              class="class-pic"
              header="Vinit Shah - Back-end Developer"
            ></b-card>
            <b-card
              img-src="@/assets/images/matt.jpg"
              img-alt="Card image"
              img-top
              class="class-pic"
              header="Matthew Frazier - Scrum Master, Back-end Developer"
            >
              <b-card-text></b-card-text>
            </b-card>
            <b-card
              img-src="@/assets/images/jonathan.png"
              img-alt="Card image"
              img-top
              class="class-pic"
              header="Jonathan Chickie - Front-end Developer"
            ></b-card>
          </b-card-group>
        </b-row>
        <b-row>
          <b-card-group deck class="mx-5 mt-4">
            <b-card
              img-src="@/assets/images/donald.jpg"
              img-alt="Card image"
              img-top
              class="class-pic"
              header="Donald Bennett - Tester/Documentation"
            ></b-card>
            <b-card
              img-src="@/assets/images/keri.png"
              img-alt="Card image"
              img-top
              class="class-pic"
              header="Keri Misenheimer - Front-end Developer"
            ></b-card>
            <b-card
              img-src="@/assets/images/arvind.png"
              img-alt="Card image"
              bottom
              class="class-pic"
              header="Arvind Suriakanth - Note Taker/Database Developer"
            ></b-card>
          </b-card-group>
        </b-row>
      </b-card>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slide: 0,
      sliding: null
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    }
  }
};
</script>

<style lang="scss" scoped>
#carousel-div {
  max-height: 0.25rem;
}
.content-card {
  opacity: 0.8;
}
#nav {
  margin-bottom: 0px;
}
.card-title {
  font-size: 3rem;
}
// .class-pic {
//   max-height: 29.5rem;
//   overflow: hidden;
// }
</style>