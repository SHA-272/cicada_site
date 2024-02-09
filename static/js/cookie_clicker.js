let clickCount = 0;

const maxClicks = 100;

function setClicks(number) {
  document.getElementById("clickCount").textContent = "Click count: " + number;
}

function yes() {
  clickCount++;
  setClicks(clickCount);

  if (clickCount === maxClicks) {
    clickCount = 0;
    setClicks(clickCount);
    alert("Congratulations! You got one cookie");
  }
}

function no() {
  clickCount = 0;
  setClicks(clickCount);
  alert("You're a terrible person.");
}
