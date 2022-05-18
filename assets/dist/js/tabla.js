$(document).ready(function () {
  //obtenemos el valor de los input

  $("#adicionar").click(function () {
    var nombre = document.getElementById("firstName").value;
    var apellido = document.getElementById("lastName").value;
    var descripcion = document.getElementById("username").value;
    var img = document.getElementById("img").value;
    var fecha = document.getElementById("address").value;
    var categoria = document.getElementById("country").value;
    var i = 1; //contador para asignar id al boton que borrara la fila
    var a = "";
    var fila =
      '<tr id="row' +
      i +
      '"><td>' +
      nombre +
      "</td><td>" +
      apellido +
      "</td><td>" +
      descripcion +
      "</td><td>" +
      img +
      "</td><td>" +
      fecha +
      "</td><td>" +
      categoria +
      '</td><td><button type="button" name="remove" id="' +
      i +
      '" class="btn btn-danger btn_remove">Quitar</button></td></tr>'; //esto seria lo que contendria la fila

    i++;

    $("#mytable tr:first").after(fila);
    $("#adicionados").text(""); //esta instruccion limpia el div adicioandos para que no se vayan acumulando
    var nFilas = $("#mytable tr").length;
    $("#adicionados").append(nFilas - 1);
    //le resto 1 para no contar la fila del header
    document.getElementById("lastName").value = "";
    document.getElementById("username").value = "";
    document.getElementById("firstName").value = "";
    document.getElementById("img").value = "";
    document.getElementById("address").value = "";
    document.getElementById("country").value = "";
    document.getElementById("firstName").focus();
  });
  $(document).on("click", ".btn_remove", function () {
    var button_id = $(this).attr("id");
    //cuando da click obtenemos el id del boton
    $("#row" + button_id + "").remove(); //borra la fila
    //limpia el para que vuelva a contar las filas de la tabla
    $("#adicionados").text("");
    var nFilas = $("#mytable tr").length;
    $("#adicionados").append(nFilas - 1);
  });
});

//no funciona xd
$(function () {
  $("#mytable").submit(function (e) {
    e.preventDefault();
    var valido = true;
    document.getElementById("firstName").value;
    if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
      valido = false;
    }
    if (!valida_form("#firstName", a)) {
      valido = false;
    }
    if (!valido) {
      e.preventDefault();
    } else {
      alert("Puro gil");
    }
  });
});
