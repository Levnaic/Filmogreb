// ee
function ee() {
  document.body.style.backgroundImage = "url('./img/ee.jpg')";

  setTimeout(() => {
    document.body.style.backgroundImage = "";
  }, 70);
}

intervalEe = setInterval(ee, 300000);

// form submit
document.getElementById("movie-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const title = document.getElementById("title").value;

  fetch("http://localhost:5000/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title: title }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("response").innerText = data.message;
      document.getElementById("title").value = ""; // Clear the input field
    })
    .catch((error) => console.error("Error:", error));
});
