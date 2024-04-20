document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const weatherDiv = document.getElementById('weather');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const cityInput = document.getElementById('city');
        const city = cityInput.value.trim();
        const response = await fetch(`/weather?city=${city}`);
        const data = await response.json();
        weatherDiv.textContent = data.message;
    });
});
