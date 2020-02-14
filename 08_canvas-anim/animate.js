// Jackson Zou
// SoftDev2 pd9
// K8 -- WHAT IS IT SAVING THE SCREEN FROM?
// 2020-02-13

var c = document.getElementById("playground");
var ctx = c.getContext("2d");

var radius = 1, change = 1, animation = 0; //variables for circle
var x = 0, y = 0, dX = 3, dY = 2;
var logo = new Image();
logo.src = "logo_dvd.jpg";
var mode = 1; //0 = circle, 1 = dvd

var startB = document.getElementById("start");
startB.addEventListener('click', function(e) {startAnimation(0)});

var waitB = document.getElementById("wait");
waitB.addEventListener('click', function(e) {startAnimation(1)});

var stopB = document.getElementById("stop");
stopB.addEventListener('click', stopAnimation);

function startAnimation(num) {
  if (animation == 0 || num != mode) {
    if (mode == 1) {
      radius = 1;
      change = 1;
    }
    if (mode == 0) {

    }
    console.log(num);
    mode = num;
    window.cancelAnimationFrame(animation);
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
  ctx.clearRect(0, 0, c.width, c.height);
  if (mode == 0) {
    //console.log("eat my shorts", radius);
    if (radius <= 0 || radius >= c.width/2) {
      change *= -1;
    }
    radius += change;
    ctx.beginPath();
    ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
    ctx.fill();
  }
  if (mode == 1) {
    if (x < 0 || x + 100 >= c.width) {
      dX *= -1;
    }
    if (y < 0 || y + 70 >= c.height) {
      dY *= -1;
    }
    x += dX;
    y += dY;
    ctx.drawImage(logo, x, y, 100, 70);
  }
  animation = window.requestAnimationFrame(draw);
}
