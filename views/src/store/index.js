import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    gmap: null
  },
  mutations: {
    setMap(state, payload) {
      state.gmap = payload;
    }
  },
  actions: {},
  modules: {}
});
