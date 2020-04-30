<template>
  <b-navbar fixed="top" toggleable="lg" type="dark" variant="info">
    <b-navbar-brand to="/">GiveWay</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/events">Events</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav>
        <b-nav-item to="/charities">Charities</b-nav-item>
      </b-navbar-nav>
      <!-- <b-navbar-nav>
        <b-nav-item to="/tester">Tester</b-nav-item>
      </b-navbar-nav> -->
      <b-navbar-nav>
        <b-nav-item to="/contact">About Us</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>

        <b-nav-item-dropdown right v-if="this.$store.state.loggedIn">
          <!-- Using 'button-content' slot -->

          <template v-slot:button-content>
            <strong>User Profile</strong>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item v-on:click="this.$parent.logOut">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item v-else to="/signin">Log In</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
#nav a.router-link-exact-active {
  color: white;
}
</style>