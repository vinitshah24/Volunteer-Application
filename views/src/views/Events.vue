<template>
  <div>
    <h1>Events</h1>

    <div>
      <!-- collapsable filter-->
      <b-button v-b-toggle.collapse-1 variant="primary">Filters</b-button>
      <b-collapse id="collapse-1" class="mt-2">
        <b-card>
          <p class="card-text">Filters could go here</p>
        </b-card>
      </b-collapse>
    </div>

    <br />

    <div>
      <b-container class="events-row">
        <b-row>
          <!-- row with 3 columns -->
          <b-col>
            <b-card title="Event Name" tag="event" style="max-width: 20rem;" class="mb-2">
              <b-card-text>
                <b-container class="bv-example-row">
                  <b-row>
                    <b-col>Address</b-col>
                  </b-row>
                  <b-row>
                    <b-col>Date</b-col>
                  </b-row>
                  <b-row>
                    <b-col>Host name</b-col>
                  </b-row>
                </b-container>
              </b-card-text>
              <b-container class="bv-example-row">
                <b-row>
                  <b-col>
                    <b-button v-b-toggle.collapse-2>About</b-button>
                  </b-col>
                  <b-col>
                    <b-button>Join</b-button>
                  </b-col>
                </b-row>
              </b-container>
            </b-card>
          </b-col>
        </b-row>
        <b-collapse id="collapse-2" class="mt-2">
          <!-- Collapsed card under the row, event card to small -->
          <b-card>
            <p class="card-text">Description Here</p>
          </b-card>
        </b-collapse>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>