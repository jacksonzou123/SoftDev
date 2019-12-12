var foo = function() {
  console.log("diagnostic info here");
  return 0;
};

var fact = function(n) {
  var final = 1;
  while (n > 1) {
    final *= n;
    n--;
  }
  console.log(final);
  return final;
};

var fibonacci = function(n) {
  var list = [1, 1];
  //console.log(list);
  var i = 2;
  while (i < n) {
    list.push(list[i-1] + list[i-2]);
    //console.log(list);
    i++;
  }
  console.log(list[n-1]);
  return list[n-1];
}

var gcd = function(a, b) {
  if (a < b) {
    i = a;
  }
  else {
    i = b;
  }
  while (i > 1) {
    if (a % i == 0 && b % i == 0) {
      console.log(i);
      return i;
    }
    i--;
  }
  console.log(1);
  return 1;
}

var randomStudent = function() {
  final = studentList[Math.floor(Math.random()*studentList.length)]
  console.log(final);
  return final;
}

var studentList = ["jegg", "jackson", "derek", "bleek", "bop", "water"];

var getrandStudent = document.getElementById("randstudent");
getrandStudent.addEventListener('click', randomStudent);

var fibinput = document.getElementById("fibinput");
console.log(fibinput);
var getfib = document.getElementById("fib");
getfib.addEventListener('click', function() {fibonacci(20)});

var getgcd = document.getElementById("gcd");
getgcd.addEventListener('click', function() {gcd(20, 39)});

var getfactorial = document.getElementById("fact");
getfactorial.addEventListener('click', function() {fact(23)});
