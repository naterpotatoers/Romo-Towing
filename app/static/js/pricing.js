function getPricing() {
    var obj = document.getElementById("towType");
    var towType = obj.options[obj.selectedIndex].text;
    if (towType == "CHP") {
        document.getElementById("showPrice").innerHTML = towType + " $300";
    }
    else if (towType == "FPD") {
        document.getElementById("showPrice").innerHTML = towType + " $300";
    }
    else {
        document.getElementById("showPrice").innerHTML = towType + " $300/hr";
    }
}