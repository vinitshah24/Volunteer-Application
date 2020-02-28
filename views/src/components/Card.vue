<template>
  <b-card
    :title="title"
    img-src="https://picsum.photos/600/300/?image=25"
    img-alt="Hey"
    img-top
    tag="article"
    style="max-width:20rem"
    class="mb-2"
    footer="Card Footer"
  >
    <b-card-text>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, doloribus? Eligendi voluptates repellat, earum libero inventore reprehenderit. Nobis ullam cum doloremque accusamus, itaque aliquam, iste omnis sit odit assumenda mollitia?</b-card-text>
    <b-button variant="primary">Apply</b-button>
  </b-card>
</template>

<script>
export default {
  props: ["title", "body"]
};
</script>

<style lang="scss" scoped>
</style>