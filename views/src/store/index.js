import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    gmap: null,
    heatmap: null,
    test: null
  },
  mutations: {
    setMap(state, payload) {
      state.gmap = payload;
    },
    setHeatmap(state, payload) {
      state.heatmap = payload;
    },
    setTest(state, payload) {
      state.test = payload;
    }
  },
  actions: {},
  modules: {}
});
