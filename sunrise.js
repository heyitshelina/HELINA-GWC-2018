function sunriseTime () {
  var lat = document.getElementById ("lat").value;
  var lng = document.getElementById ("lng").value;
  var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
  //gets us to doc that has infor about user lat/long value
  var request = new XMLHttpRequest();
  request.open('GET', query, false);
  request.send();
  var requestInformation = JSON.parse(request.responseText);
  var sunriseTime = requestInformation.results.sunrise;
  alert("The sunrise time is " + sunriseTime);
}

function sunsetTime () {
  var lat = document.getElementById ("lat").value;
  var lng = document.getElementById ("lng").value;
  var query = "https://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng;
  //gets us to doc that has infor about user lat/long value
  var request = new XMLHttpRequest();
  request.open('GET', query, false);
  request.send();
  var requestInformation = JSON.parse(request.responseText);
  var sunsetTime = requestInformation.results.sunset;
  alert("The sunset time is " + sunsetTime);
}
