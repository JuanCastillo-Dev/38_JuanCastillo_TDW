// Acción 1: Mostrar un mensaje
document.getElementById('btn-mensaje').addEventListener('click', () => {
    alert('¡Bienvenido al sistema de Renace Cañete!');
});

// Acción 2: Cambiar contenido del texto en el DOM
document.getElementById('btn-contenido').addEventListener('click', () => {
    const descripcion = document.getElementById('descripcion');
    descripcion.textContent = 'Estado: Catálogo de productos agrícolas actualizado.';
});

// Acción 3: Modificar estilo dinámicamente
document.getElementById('btn-estilo').addEventListener('click', () => {
    const tarjeta = document.getElementById('card');
    tarjeta.classList.toggle('border-emerald-500');
    tarjeta.classList.toggle('border-4');
    
    const titulo = document.getElementById('titulo');
    titulo.style.color = '#059669';
});