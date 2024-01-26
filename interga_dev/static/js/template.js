$(document).ready(function () {
  // Tema
  if (document.cookie.indexOf("tema=dark") >= 0) {
    $("#modo_escuro").addClass("fw-bold");
    $("#modo_claro").removeClass("fw-bold");
    $("#menu_tema").html('<i class="bi bi-moon-stars-fill"></i>');
    $("html").attr("data-bs-theme", "dark");
  } else {
    $("#modo_claro").addClass("fw-bold");
    $("#modo_escuro").removeClass("fw-bold");
    $("#menu_tema").html('<i class="bi bi-brightness-high-fill"></i>');
    $("html").attr("data-bs-theme", "light");
  }

  $("#modo_claro").click(function () { 
    $(this).addClass("fw-bold");
    $("#modo_escuro").removeClass("fw-bold");
    $("#menu_tema").html('<i class="bi bi-brightness-high-fill"></i>');
    $("html").attr("data-bs-theme", "light");
    document.cookie = "tema=light";
  });
  $("#modo_escuro").click(function () { 
    $(this).addClass("fw-bold");
    $("#modo_claro").removeClass("fw-bold");
    $("#menu_tema").html('<i class="bi bi-moon-stars-fill"></i>');
    $("html").attr("data-bs-theme", "dark");
    document.cookie = "tema=dark";
  });
});