// ee
function ee() {
  document.body.style.backgroundImage = "url('/static/img/ee.jpg')";

  setTimeout(() => {
    document.body.style.backgroundImage = "";
  }, 70);
}

intervalEe = setInterval(ee, 300000);

// form submit
document.getElementById("movie-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const title = document.getElementById("title").value;
  const resolution = document.getElementById("resolution").value || "N/A";
  const season = document.getElementById("season").value || "N/A";

  fetch("http://localhost:5000/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      title: title,
      resolution: resolution,
      season: season,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("response").innerText = data.message;
      // Clear the input field
      document.getElementById("title").value = "";
      document.getElementById("resolution").value = "";
      document.getElementById("season").value = "";
    })
    .catch((error) => console.error("Error:", error));
});
