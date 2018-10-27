var map;
var marker_list;
var rectangle_list = [];
var directionsService;

function initialize() {
  var latlng = new google.maps.LatLng(79.02913665771484, 88.66764068603516);
  var options = {
//    noClear : true,
    zoom: 10,
    center: latlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById("map_canvas"), options);
  map.setOptions(getMapOptionDefault());
  marker_list = new google.maps.MVCArray();
  directionsService = new google.maps.DirectionsService();
  render();
}

function render() {
  $.getJSON('GW1AM2_201810160147_199D_L2SGSSTLB3300300-2.json') // json読み込み開始
    .done(function(json){ // jsonの読み込みに成功した時
      console.log('成功');
      for (n = 0; n < json.length; n++){
        south = json[n].lat - 0.5;
        north = json[n].lat + 0.5;
        west = json[n].lng - 0.5;
        east = json[n].lng + 0.5;
        opacity = json[n].geo / 1000;
        val = "ice depth : " + json[n].geo;
        console.log(val);
        var rectangle = new google.maps.Rectangle({
           map: map,
           strokeOpacity: opacity,
           strokeColor: '#0000FF',
           fillOpacity: opacity,
           fillColor: '#0000FF',
           bounds: {
             south: south,
             west: west,
             north: north,
             east: east
           },
           title: val
        });
        rectangle_list.push(rectangle);
      }
    })
    .fail(function(){ // jsonの読み込みに失敗した時
      console.log('失敗');
    })
    .always(function(){ // 成功/失敗に関わらず実行
      console.log('必ず実行される');
    });
}
