<template>
  <div>
    <b-container>
      <b-jumbotron
        header="Meet the GiveWay Team"
        lead="Making Giving Easier"
        bg-variant="primary"
        text-variant="white"
        class="h-50"
      ></b-jumbotron>
    </b-container>
    <b-container>
      <b-row>
        <b-col>
          <b-img src="https://picsum.photos/300/150/?image=41" fluid alt="Fluid image"></b-img>
        </b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
      <b-row>
        <b-col></b-col>
        <b-col></b-col>
        <b-col></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  name: "Contact",
  data() {
    return {
      items: [
        {
          phone: "704-599-5959",
          address: "123 Charity Lane",
          city: "Charlotte",
          state: "NC"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
</style>