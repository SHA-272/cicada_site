let currentEquation;
let startTime;
let totalTests = 10;
let currentTest = 1;
let correctAnswers = 0;
let totalElapsedTime = 0;

function generateEquation() {
  const operand1 = Math.floor(Math.random() * (currentTest * 10)) + 1;
  const operand2 = Math.floor(Math.random() * (currentTest * 10)) + 1;
  const operator = Math.random() < 0.5 ? "+" : "-";
  currentEquation = `${operand1} ${operator} ${operand2}`;
  document.getElementById("equation").innerText =
    `${currentTest}) ` + currentEquation + " = ?";
  document.getElementById("userAnswer").value = "";
  document.getElementById("result").innerText = "";
  startTime = new Date();
  document.getElementById("userAnswer").focus();
}

function runTests() {
  if (currentTest <= totalTests) {
    document.getElementById("start").style.display = "none";
    generateEquation();
  } else if (currentTest == totalTests + 1) {
    const accuracy = (correctAnswers / totalTests) * 100;
    const averageTime = totalElapsedTime / totalTests;
    document.getElementById(
      "result"
    ).innerText = `Tests completed.\nAccuracy: ${accuracy.toFixed(
      2
    )}%\nAverage time per test: ${averageTime.toFixed(
      2
    )} seconds\nTotal elapsed time: ${totalElapsedTime.toFixed(2)} seconds`;

    if (accuracy < 100) {
      document.getElementById("total").innerText = "You have incorrect answers";
      document.getElementById("total").style.color = "red";
    } else if (totalElapsedTime >= totalTests * 2) {
      document.getElementById(
        "total"
      ).innerText = `Too slow! Maximum solution time is ${
        totalTests * 2
      } seconds`;
      document.getElementById("total").style.color = "red";
    } else
      document.getElementById("total").innerHTML =
        'Congratulations! <a href="https://cicada.krductf.ru/ee54449478c54a5a5cc4f774e3d4ba34">Next level</a>';
  }
}

function checkAnswer() {
  const userAnswer = document.getElementById("userAnswer").value;
  const correctAnswer = eval(currentEquation);
  const endTime = new Date();
  const elapsedTime = (endTime - startTime) / 1000;

  totalElapsedTime += elapsedTime;

  if (userAnswer === correctAnswer.toString()) {
    correctAnswers++;
  }

  currentTest++;
  runTests();
}
