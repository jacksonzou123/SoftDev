var foo = function() {
  console.log("diagnostic info here");
  return 0;
};

var fact = function(n) {
  if (n < 2) {
    return 1;
  }
  else {
    return n * fact(n-1);
  }
};

var fibonacci = function(n) {
  if (n <= 2) {
    return 1;
  }
  else {
    return fibonacci(n-1) + fibonacci(n-2);
  }
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
      return i;
    }
    i--;
  }
  return 1;
}

var randomStudent = function() {
  return studentList[Math.floor(Math.random()*studentList.length)];
}

var studentList = ["jegg", "jackson", "derek", "bleek", "bop", "water"];
