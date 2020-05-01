import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    userAccessToken: null,
    userRefreshToken: null,
    user: {},
    loggedIn: false,
    error: false,
    status: null,
    username: null,
    events: [],
    google: null,
    gmap: null,
    heatmap: null,
    test: null,
    counties: null
  },
  mutations: {
    setAccess(state, payload) {
      state.userAccessToken = payload;
    },
    setRefresh(state, payload) {
      state.userRefreshToken = payload;
    },
    setLoggedIn(state, payload) {
      state.loggedIn = payload;
    },
    setError(state, payload) {
      state.error = payload;
    },
    setStatus(state, payload) {
      state.status = payload;
    },
    setUsername(state, payload) {
      state.username = payload;
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setUserEvents(state, payload) {
      state.user.events = payload;
    },
    setEvents(state, payload) {
      state.events = payload;
    },
    setGoogle(state, payload) {
      state.google = payload;
    },
    setMap(state, payload) {
      state.gmap = payload;
    },
    setHeatmap(state, payload) {
      state.heatmap = payload;
    },
    setTest(state, payload) {
      state.test = payload;
    },
    setCounties(state, payload) {
      state.counties = payload;
    }
  },
  actions: {},
  modules: {}
});
