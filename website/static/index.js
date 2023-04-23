function vymazPizzu(pizzaId) {
  fetch("/vymaz-pizzu", {
    method: "POST",
    body: JSON.stringify({ pizzaId: pizzaId }),
  }).then((_res) => {
    window.location.href = "/kosik";
  });
}
function vymazRezervaciu(rezervaciaId) {
  fetch("/vymaz-rezervaciu", {
    method: "POST",
    body: JSON.stringify({ rezervaciaId: rezervaciaId }),
  }).then((_res) => {
    window.location.href = "/kosik";
  });
}
function zaplatit() {
  fetch("/zaplatit", {
    method: "POST",
  }).then((_res) => {
    window.location.href = "/kosik";
  });
}