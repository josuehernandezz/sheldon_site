// slider.js

generateSliderIndicators(document.getElementById('num_pics'));

function generateSliderIndicators(numPicsElement) {
    // Get the number of pictures from the provided DOM element
    var numPictures = parseInt(numPicsElement.innerText.trim());

    // Get the slider indicators container
    var sliderIndicators = document.getElementById('sliderIndicators');

    // Clear any existing content in the container
    sliderIndicators.innerHTML = '';

    // Loop through the number of pictures and create the buttons dynamically
    for (var i = 0; i < numPictures; i++) {
        var button = document.createElement('button');
        button.setAttribute('type', 'button');
        button.setAttribute('class', 'w-3 h-3 rounded-full');
        button.setAttribute('aria-label', 'Slide ' + (i + 1));
        button.setAttribute('data-carousel-slide-to', i);

        // Set the first button as active, others as inactive
        if (i === 0) {
            button.setAttribute('aria-current', 'true');
        } else {
            button.setAttribute('aria-current', 'false');
        }

        // Append the button to the slider indicators container
        sliderIndicators.appendChild(button);
    }
}
