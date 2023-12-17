const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherbox = document.querySelector('.weather-box');
const weatherdetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');
const cityhide = document.querySelector('.city-hide');

search.addEventListener('click', () => {
    const APIKey = 'bcff5c03848be6ed219fb471c8b11fcd';
    const city = document.querySelector('.search-box input').value;

    if (city == '')
        return;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${APIKey}`)
        .then(response => response.json())
        .then(json => {
            //when error
            if (json.cod == '404') {
                cityhide.textContent = city;
                container.style.height = '400px';
                weatherbox.classList.remove('active');
                weatherdetails.classList.remove('active');
                error404.classList.add('active');
                return;
            }
            //when it can find a country
            container.style.height = '555px';
            weatherbox.classList.add('active');
            weatherdetails.classList.add('active');
            error404.classList.remove('active');


            const image = document.querySelector('.weather-box img');
            const temperature = document.querySelector('.weather-box .temperature');
            const description = document.querySelector('.weather-box .description');
            const humidity = document.querySelector('.weather-details .humidity span');
            const wind = document.querySelector('.weather-details .wind span');

            if (cityhide.textContent == city) {
                return;
            }
            else {
                cityhide.textContent = city;

                container.style.height = '555px';
                container.classList.add('active');
                weatherbox.classList.add('active');
                weatherdetails.classList.add('active');
                error404.classList.remove('active');

                setTimeout(() => {
                    container.classList.remove('active');
                }, 2500);

                switch (json.weather[0].main) {
                    case 'Clear':
                        image.src = 'Image/clear.png';
                        break;

                    case 'Rain':
                        image.src = 'Image/rainy.png';
                        break;

                    case 'Snow':
                        image.src = 'Image/snowy.png';
                        break;

                    case 'Mist':
                        image.src = 'Image/windy.png';
                        break;

                    case 'Haze':
                        image.src = 'Image/windy.png';
                        break;

                    default:
                        image.src = 'Image/sunny.png';
                }

                temperature.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
                description.innerHTML = `${json.weather[0].description}`;
                humidity.innerHTML = `${json.main.humidity}%`;
                wind.innerHTML = `${parseInt(json.wind.speed)}Km/h`;
            }
            const infoweather = document.querySelector('.info-weather');
            const infohumidity = document.querySelector('.info-humidity');
            const infowind = document.querySelector('.info-wind');

            const cloneinfoweather = infoweather.cloneNode(true);
            const cloneinfohumidity = infohumidity.cloneNode(true);
            const cloneinfowind = infowind.cloneNode(true);

            cloneinfoweather.id = 'clone-info-weather';
            cloneinfoweather.classList.add('active-clone');

            cloneinfohumidity.id = 'clone-info-humidity';
            cloneinfohumidity.classList.add('active-clone');

            cloneinfowind.id = 'clone-info-wind';
            cloneinfowind.classList.add('active-clone');

            setTimeout(() => {
                infoweather.insertAdjacentElement("afterend", cloneinfoweather);
                infohumidity.insertAdjacentElement("afterend", cloneinfohumidity);
                infowind.insertAdjacentElement("afterend", cloneinfowind);
            }, 2200);

            const Cloneinfoweather = document.querySelectorAll('.info-weather.active-clone');
            const Totalcloneinfoweather = Cloneinfoweather.length;
            const Firstcloneinfoweather = Cloneinfoweather[0];

            const Cloneinfohumidity = document.querySelectorAll('.info-humidity.active-clone');
            const Firstcloneinfohumidity = Cloneinfohumidity[0];

            const Cloneinfowind = document.querySelectorAll('.info-humidity.active-clone');
            const Firstcloneinfowind = Cloneinfowind[0];

            if (Totalcloneinfoweather > 0) {
                Firstcloneinfoweather.classList.remove('active-clone');
                Firstcloneinfohumidity.classList.remove('active-clone');
                Firstcloneinfowind.classList.remove('active-clone');

                setTimeout(() => {
                    Firstcloneinfoweather.remove();
                    Firstcloneinfohumidity.remove();
                    Firstcloneinfowind.remove();
                }, 2200);
            }


        });
});
