function valida_form(x, y) {
  return $(x).val().match(y) ? true : false;
}
var correo_admin = "admin@gmail.com";
var contra_admin = "TokinoSora";
var a = "";

$(function () {
  $("#form").submit(function (e) {
    e.preventDefault();
    var valido = true;
    if (!valida_form("#floatingInput", correo_admin)) {
      valido = false;
      $("#floatingInput").addClass("error_input");
    }
    if (!valida_form("#floatingPassword", contra_admin)) {
      valido = false;
      $("#floatingPassword").addClass("error_input");
    }
    if (!valido) {
      e.preventDefault();
    } else {
      window.location.href = "../../html/index2/index2.html";
      alert("Login correcto");
    }
  });
});

$(function () {
  $("#form2").submit(function (e) {
    e.preventDefault();
    var valido = true;
    if (!valida_form("#firstName", a)) {
      valido = false;
    }
    if (!valida_form("#lastName", a)) {
      valido = false;
    }
    if (!valida_form("#username", a)) {
      valido = false;
    }
    if (!valida_form("#address", a)) {
      valido = false;
    }
    if (!valido) {
      e.preventDefault();
    } else {
      alert("Trabajo subido");
    }
  });
});

$(function () {
  $("#form3").submit(function (e) {
    e.preventDefault();
    var valido = true;
    if (!valida_form("#country", a)) {
      valido = false;
    }
    if (!valida_form("#username", a)) {
      valido = false;
    }
    if (!valido) {
      e.preventDefault();
    } else {
      alert("Comentario subido");
    }
  });
});
