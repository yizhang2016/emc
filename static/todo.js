function getNums()
{
    var NRequest = document.getElementById("description").value;

    // Send data to database.
     var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function()
    {
        if(xhttp.readyState == 4 && xhttp.status == 200)
        {
            console.log(xhttp.responseText);

            // output ans
            document.getElementById("outputRes").innerHTML = xhttp.responseText;



        }
    };

    var sendParameters = "?n="+NRequest;

    xhttp.open("GET", "/getFibonacciNums/"+sendParameters, true);
    xhttp.send();
}
