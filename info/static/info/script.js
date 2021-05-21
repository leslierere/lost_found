// Event handling
document.addEventListener("DOMContentLoaded",
  function (event) {
    // show the div on click: ref: https://stackoverflow.com/questions/31826469/how-to-display-a-div-only-when-a-button-is-clicked
    function sayHello (event) {
      this.textContent = "Map shown!";
       // var message = '<iframe src=\"{{ site.get_real_map_url }}\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\"></iframe>';
       //  console.log(message);
      document
        .getElementById("map-tile")
        .style.display = 'block';
    }

    // Unobtrusive event binding
    document.querySelector("#map_button")
      .addEventListener("click", sayHello);

  }
);



// document.querySelector("button")
//   .onclick = sayHello;




