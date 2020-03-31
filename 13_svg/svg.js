var svg = document.getElementById("vimage");

var draw = function(e) {
  console.log(e.target)
  if (e.target == svg) {
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    var x = e.offsetX;
    var y = e.offsetY;
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "10");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    svg.appendChild(c);
  }

  else {
    if (e.target.getAttribute("fill") == "blue") {
      e.target.setAttribute("fill", "violet");
    }
    else {
      svg.removeChild(e.target)
      var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
      var x = Math.floor(Math.random() * 500);
      var y = Math.floor(Math.random() * 500);
      c.setAttribute("cx", x);
      c.setAttribute("cy", y);
      c.setAttribute("r", "10");
      c.setAttribute("fill", "blue");
      c.setAttribute("stroke", "black");
      svg.appendChild(c);
    }
  }
}

var clear = function(e) {
  while (svg.lastChild) {
    svg.removeChild(svg.lastChild);
  }
}

document.getElementById("clear").addEventListener('click',clear);
svg.addEventListener('click', draw);
