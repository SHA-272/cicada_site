const images = [
  "../static/images/qr_0_0.png",
  "../static/images/qr_0_1.png",
  "../static/images/qr_0_2.png",
  "../static/images/qr_1_0.png",
  "../static/images/qr_1_1.png",
  "../static/images/qr_1_2.png",
  "../static/images/qr_2_0.png",
  "../static/images/qr_2_1.png",
  "../static/images/qr_2_2.png",
];

function getRandomPosition(max) {
  return Math.random() * max;
}

images.forEach((imagePath, index) => {
  const img = new Image();
  img.src = imagePath;
  img.alt = "Moving Image";

  // Set initial position and speed for each image
  let x = getRandomPosition(window.innerWidth / 2);
  let y = getRandomPosition(window.innerHeight / 2);
  let speedX = (Math.random() - 0.5) * 20; // Random speed between -5 and 5
  let speedY = (Math.random() - 0.5) * 20;

  img.style.left = x + "px";
  img.style.top = y + "px";
  img.classList.add("moving-image");

  document.body.appendChild(img);

  function moveImage() {
    x += speedX;
    y += speedY;

    // Bounce off the horizontal edges
    if (x < 0 || x + img.width > window.innerWidth) {
      speedX = -speedX;
    }

    // Bounce off the vertical edges
    if (y < 0 || y + img.height > window.innerHeight) {
      speedY = -speedY;
    }

    img.style.left = x + "px";
    img.style.top = y + "px";

    requestAnimationFrame(moveImage);
  }

  moveImage();
});
