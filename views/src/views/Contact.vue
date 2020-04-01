<template>
  <div>
    <h1>Contact Us!</h1>
    <b-table striped stacked hover :items="items"></b-table>
  </div>
</template>

<script>
export default {
  name: "Contact",
  data() {
    return {
      items: [
        { phone: "704-599-5959", address: "123 Charity Lane", city: "Charlotte", state: "NC" }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
</style>