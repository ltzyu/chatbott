var map;
var view;
var ourLoc;
  //initialize Location
ourLoc = ol.proj.fromLonLat([121.010256, 24.752770]);

//let's initialize our variables (give them some value)
function init() {
    //alert(ourLoc)
    //console.log(ourLoc)
  view = new ol.View({
    center: ourLoc, //center the map on our current location, according to ourLoc
    zoom: 6 //how far the map zooms in
  });

  map = new ol.Map({
    target: 'map', //target: the container for the map (refers back to the 'map' on the html); the ID of our <div>
    layers: [
      //objects use colons the = would confuse the map = new[...]
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ], //comma to add another property

    loadTilesWhileAnimating: true,
    view: view
  });

}

function panHome(){
  //alert(ourLoc); for debugging
  view.animate({
    center: ourLoc,
    duration: 2000 //two seconds
  });
}

function panToLocation(){
  var countryName = document.getElementById("country-name").value;
  var query = "https://restcountries.eu/rest/v2/name/"+countryName;

  query = query.replace(/ /g, "%20")

  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);
  countryRequest.send();

  var countryInformation = JSON.parse(countryRequest.responseText);

  console.log(countryInformation);
  //var lon = 0.0;
  //var lat = 0.0;
  var lat = countryInformation[0].latlng[0];
  var lon = countryInformation[0].latlng[1];

  var location = ol.proj.fromLonLat([lon, lat]);
  view.animate({
    center: location,
    duration: 2000
  });
}
window.onload = init;
