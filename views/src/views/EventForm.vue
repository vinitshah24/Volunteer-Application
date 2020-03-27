<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Volunteer Event:"
        label-for="input-1"
        description="This event will be public."
      >
        <b-form-input
          id="input-1"
          v-model="form.name"
          type="name"
          required
          placeholder="Enter event name"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Category:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.category"
          required
          placeholder="Enter event category"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Details:" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="form.details"
          required
          placeholder="Enter event details"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="Address:" label-for="input-4">
        <b-form-input
          id="input-4"
          v-model="form.address"
          required
          placeholder="Enter event address"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-5" label="State:" label-for="input-5">
        <b-form-input
          id="input-5"
          v-model="form.state"
          required
          placeholder="Enter state"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-6" label="Time:" label-for="input-6">
        <b-form-input
          id="input-6"
          v-model="form.time"
          required
          placeholder="Enter time"
        ></b-form-input>
      </b-form-group>

       <b-form-group id="input-group-7" label="Date:" label-for="input-7">
        <b-form-input
          id="input-7"
          v-model="form.date"
          required
          placeholder="Enter date"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-8" label="County:" label-for="input-9">
        <b-form-select
          id="input-3"
          v-model="form.county"
          :options="counties"
          required
        ></b-form-select>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          name: '',
          category: '',
          details:'',
          address:'',
          state: '',
          time: '',
          date: '',
          county: null,
          checked: []
        },
        counties: [{ text: 'Select One', value: null }, 'Alamance', 'Alexander', 'Alleghany', 'Anson', 'Ashe', 'Avery', 'Beaufort',
        'Bertie', 'Bladen', 'Brunswick', 'Buncombe', 'Burke', 'Cabarrus', 'Caldwell', 'Camden', 'Carteret', 'Caswell', 'Catawba',
        'Chatham', 'Cherokee', 'Chowan', 'Clay', 'Cleveland', 'Columbus', 'Craven', 'Cumberland', 'Currituck', 'Dare', 'Davidson',
        'Davie', 'Durham', 'Duplin', 'Edgecombe', 'Forsyth', 'Franklin', 'Gaston', 'Gates', 'Graham', 'Granville', 'Green', 
        'Guilford', 'Halifax', 'Harnett', 'Haywood', 'Mecklenberg', 'Henderson', 'Hertferd', 'Hoke', 'Hyde', 'Martin', 'McDowell',
        'Mitchell', 'Montgomery', 'Moore', 'Nash', 'Northampton', 'Onslow', 'Orange', 'Pamlico', 'Pender', 'Person', 'Pitt',
        'Randolph', 'Richmond', 'Rowan', 'Robeson', 'Rutherford', 'Sampson', 'Scotland', 'Stanley', 'Wilkes', 'Yadkin', 'Union',
        'Wake'],
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
        this.form.name = ''
        this.form.category = ''
        this.form.details = ''
        this.form.address = ''
        this.form.state = ''
        this.form.time = ''
        this.form.date = ''
        this.form.county = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
#nav a.router-link-exact-active {
  color: white;
}
</style>