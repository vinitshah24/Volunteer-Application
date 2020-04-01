const API_KEY = process.env.VUE_APP_MAP;
const CALLBACK_NAME = "gmapsCallback";

let initialized = !!window.google;
let resolveInitPromise;
let rejectInitPromise;
// This promise handles the initialization
// status of the google maps script.
const initPromise = new Promise((resolve, reject) => {
  resolveInitPromise = resolve;
  rejectInitPromise = reject;
});

export default function init() {
  // var requestOptions = {
  //   method: "GET",
  //   redirect: "follow"
  // };
  // var data;

  // fetch("http://127.0.0.1:5000/api/v1/poverty/NC", requestOptions)
  //   .then(response => response.text())
  //   .then(result => {
  //     data = JSON.parse(result);
  //     var filt = data.NC.map(county => county.region)
  //     console.log(filt);
  //   })
  //   .catch(error => console.log("error", error));
  // If Google Maps already is initialized
  // the `initPromise` should get resolved
  // eventually.
  if (initialized) return initPromise;

  initialized = true;
  // The callback function is called by
  // the Google Maps script if it is
  // successfully loaded.
  window[CALLBACK_NAME] = () => resolveInitPromise(window.google);

  // We inject a new script tag into
  // the `<head>` of our HTML to load
  // the Google Maps script.
  const script = document.createElement("script");
  script.async = true;
  script.defer = true;
  script.src = `https://maps.googleapis.com/maps/api/js?key=${API_KEY}&callback=${CALLBACK_NAME}&libraries=visualization`;
  script.onerror = rejectInitPromise;
  document.querySelector("head").appendChild(script);

  return initPromise;
}
