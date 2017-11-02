var canvasId = document.getElementById("canvas");


function smallMap() {
  for(var i = 0; i < 3; i++) {  //i is for rows j is for columns
    for(var j = 0; j < 4; j++) {
      var mapDiv = document.createElement("div");
      mapDiv.setAttribute("id", "mapdiv" + i);
      mapDiv.innerHTML = "row: " + i + " column: " + j;
      canvasId.appendChild(mapDiv);
    }
    document.createElement("br");
  }
}
smallMap();

function carousel() {
  


}