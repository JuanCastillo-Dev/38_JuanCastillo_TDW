function validateForm() {
    const title = document.getElementById('title').value.trim();
    const image = document.getElementById('image').value;

    if (title === "") {
        alert("Por favor, ingresa un título para la imagen.");
        return false;
    }

    if (image === "") {
        alert("Por favor, selecciona un archivo de imagen.");
        return false;
    }

    return true;
}