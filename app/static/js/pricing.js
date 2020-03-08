var selector = document.getElementsByName("Tow Type").values;
console.log("The value");
console.log(selector);

function whichOption()
{
    if (selector == "CHP")
    {
        console.log("CHP read");
    }
    if (selector == "FPD")
    {
        console.log("FPD read");
    }
    if (selector == "Personal")
    {
        console.log("Personal read");
    }
}