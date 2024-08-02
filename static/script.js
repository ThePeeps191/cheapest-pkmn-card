function searchfunc() {
	var x = "/get/"
	var y = document.getElementById("cardname").value;
  document.getElementById("cardname").value = "";
	window.open(window.location.href + x + y, '_blank').focus();
  document.getElementById("cardname").value = "";
}

var input = document.getElementById("cardname");
input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    document.getElementById("searchbutton").click();
  }
});