// Validar que el tipo de mantención esté seleccionado
function validateForm() {
    var tipoMantencion = document.getElementById("tipoMantencion").value;
    if (tipoMantencion === "") {
        alert("Por favor, seleccione el tipo de mantención.");
        return false;
    }

    // Si la mantención es a domicilio, validar que se haya ingresado una dirección
    if (tipoMantencion === "domicilio") {
        var direccion = document.getElementById("direccion").value;
        if (direccion === "") {
            alert("Por favor, ingrese la dirección.");
            return false;
        }
    }

    return true;
}

// Mostrar y ocultar el campo de dirección según el tipo de mantención
document.getElementById("tipoMantencion").addEventListener("change", function() {
    var tipoMantencion = this.value;
    var direccionDiv = document.getElementById("direccionDiv");
    if (tipoMantencion === "domicilio") {
        direccionDiv.style.display = "block";
    } else {
        direccionDiv.style.display = "none";
    }
});

// Validar correo electrónico
function validarCorreo() {
    var correo = document.getElementById('email').value;
    var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    var emailError = document.getElementById('emailError');

    if (regex.test(correo)) {
        emailError.innerHTML = '';
        return true;
    } else {
        emailError.innerHTML = 'Por favor, ingrese un correo electrónico válido.';
        return false;
    }
}

// Event listener para el envío del formulario
document.getElementById('mantencionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío automático del formulario

    if (validateForm() && validarCorreo()) {
        guardarDatos(); // Llamar a la función para guardar los datos si la validación es exitosa
    }
});

// Función para guardar datos del formulario
function guardarDatos() {
    var nombre = document.getElementById('nombre').value;
    var email = document.getElementById('email').value;
    var telefono = document.getElementById('telefono').value;
    var tipoMantencion = document.getElementById('tipoMantencion').value;
    var direccion = document.getElementById('direccion').value;
    var fecha = document.getElementById('fecha').value;

    var datosFormulario = {
        nombre: nombre,
        email: email,
        telefono: telefono,
        tipoMantencion: tipoMantencion,
        direccion: direccion,
        fecha: fecha
    };

    var datosGuardados = localStorage.getItem('datosMantencion');

    if (datosGuardados) {
        var formularios = JSON.parse(datosGuardados);
        formularios.push(datosFormulario);
        localStorage.setItem('datosMantencion', JSON.stringify(formularios));
    } else {
        var formularios = [datosFormulario];
        localStorage.setItem('datosMantencion', JSON.stringify(formularios));
    }

    alert('Datos enviados.');
}