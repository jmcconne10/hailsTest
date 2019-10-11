document.getElementById('postData').addEventListener('submit', postData);
function postData(event) {
    event.preventDefault();

    //grabbing input from form
    let rideDate = document.getElementById('rideDate').value;
    let startTime = document.getElementById('startTime').value;
    let endTime = document.getElementById('endTime').value;


    //Need to get the submitter from the login and increment the jobID
    let name = "Danny";

    //Call to hailsSubmit-API
    fetch('https://ox08an4tsf.execute-api.us-east-1.amazonaws.com/test/test', {
        method: 'POST',
        headers: new Headers(),
        body: JSON.stringify({ name, rideDate, startTime, endTime }),
        mode: 'cors',
    })
        .then(
          function(response) {
            console.log(rideDate + startTime);
            if (response.status !== 200) {
              console.log('Looks like there was a problem. Status Code: ' +
                response.status);
              return;
            }

            // Examine the text in the response
            response.json()
            .then(function(data) {
              console.log(data);
              let output = JSON.stringify(data);
              var myObj = JSON.parse(output);
              document.getElementById("response").innerHTML = "name: " + myObj.name + "<p>Ride Date Time: " + myObj.rideDateTime+ "</p>";
            });
          }
        )

        //.then((data) => alert('jobID: ' + jobID + '\nrideDate: ' + rideDate + '\nstartTime: '+ startTime +'\nendTime: ' + endTime))
        .catch((err) => console.log(err))
}
