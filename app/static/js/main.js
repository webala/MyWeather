const form = document.querySelector('#region-form');
const infoText = document.querySelector('#info-text');
let weatherShowcase = document.querySelector('.weather-showcase');
const hamburgerMenu = document.querySelector('.humbuger-menu');

const menuBtn = document.querySelector('.menu-btn');
const closeBtn = document.querySelector('.close-btn');
menuBtn.addEventListener('click', () => {
    hamburgerMenu.classList.add('humbuger-active');
});
closeBtn.addEventListener('click', () => {
    hamburgerMenu.classList.remove('humbuger-active');
});

form.addEventListener('submit', (e) => {
    console.log('Handling Submit');
    infoText.classList.remove('d-none')
    infoText.classList.add('active')
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);

    const entries = formData.entries();
    const regionData = Object.fromEntries(entries);
    

    getWeather(regionData).then((data) => {
        
        infoText.classList.add('d-none');
        infoText.classList.remove('active');
        weatherShowcase.classList.remove('d-none');
        weatherShowcase.classList.add('active');
        document.querySelector('.temp').innerHTML = data.temperature;
        document.querySelector('.temp-min').innerHTML = data.temperature_min;
        document.querySelector('.temp-max').innerHTML = data.temperature_max;
        document.querySelector('.humidity').innerHTML = data.humidity;
        document.querySelector('.visibility').innerHTML = data.visibility;
        document.querySelector('.wind-speed').innerHTML = data.wind_speed;
        document.querySelector('.counrty').innerHTML = `${data.region} ${data.country}`;
    })
})




async function getWeather (data) {
    console.log('Get weather called');
    let response = await fetch('/weather', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })

    if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
    }

    return await response.json();
}


