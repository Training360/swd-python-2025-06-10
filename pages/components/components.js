window.onload = function() {
    visibilityButton = document.querySelector('#visibility-button');
    visibilityButton.onclick = function() {
        var visibility = document.querySelector('#visibility-span');
        if (visibility.style.visibility === 'hidden') {
            visibility.style.visibility = 'visible';
        }
        else {
            visibility.style.visibility = 'hidden';
        }

    }

    displayButton = document.querySelector('#display-button');
    displayButton.onclick = function() {
        var display = document.querySelector('#display-span');
        if (display.style.display === 'none') {
            display.style.display = 'inline-block';
        } else {
            display.style.display = 'none';
        }
    }
}