// script.js

function sendPostRequest() {
    var hotelInput = document.getElementById('hotelInput').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:8000/rec', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                displayRecommendedRestaurants(response.recommendations);
            } else {
                console.error('Error:', xhr.statusText);
            }
        }
    };

    xhr.onerror = function() {
        console.error('Request failed');
    };

    var requestData = JSON.stringify({ hotel_name: hotelInput });
    xhr.send(requestData);
}

function displayRecommendedRestaurants(restaurants) {
    var resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "";

    var heading = document.createElement('h2');
    heading.textContent = 'Recommended Restaurants:';
    resultDiv.appendChild(heading);

    restaurants.forEach(function(restaurant) {
        var containerDiv = document.createElement('div');
        var imgElement = document.createElement('img');
        imgElement.src = restaurant.link;
        imgElement.alt = restaurant.name;
        imgElement.style.maxWidth = '200px';
        imgElement.style.maxHeight = '150px';
        imgElement.style.marginRight = '10px';

        var nameElement = document.createElement('p');
        nameElement.textContent = restaurant.name;

        containerDiv.appendChild(imgElement);
        containerDiv.appendChild(nameElement);

        resultDiv.appendChild(containerDiv);
    });
}