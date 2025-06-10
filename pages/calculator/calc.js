function add() {
    a = document.getElementById("a-input").value;
    b = document.getElementById("b-input").value;
    document.getElementById("result-input").value = parseInt(a)
    + parseInt(b);
    return false;
};

document.getElementById("submit-button").onclick = add;
    