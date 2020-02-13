// Jackson Zou
// SoftDev2 pd9
// K7 -- THEY LOCK US IN THE TOWER WHEN WE GET CAUGHT
// 2020-02-12

var c = document.getElementById("playground");
var ctx = c.getContext("2d");
var radius = 1;
var change = 1;
var animation = 0;

var startB = document.getElementById("start");
startB.addEventListener('click', startAnimation);

var stopB = document.getElementById("stop");
stopB.addEventListener('click', stopAnimation);

function startAnimation() {
  if (animation == 0) {
    animation = window.requestAnimationFrame(draw);
  }
}

function stopAnimation() {
  console.log(animation);
  console.log("dont eat my shorts");
  window.cancelAnimationFrame(animation);
  animation = 0;
}

function draw(timestamp) {
  console.log("eat my shorts", radius);
  if (radius <= 0 || radius >= c.width/2) {
    change *= -1;
  }
  radius += change;
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.beginPath();
  ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
  ctx.fill();
  animation = window.requestAnimationFrame(draw);
}
