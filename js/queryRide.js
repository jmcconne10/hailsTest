fetch('https://w7m4ccxruf.execute-api.us-east-1.amazonaws.com/prod/rides')
    .then(function (res) {
        return res.json();
    })
    .then(function (data) {
        let result = ``;
        data.forEach((user) => {
            const { status, rideDate, startTime, endTime } = user
            result +=
                `<div class="lists">
                    <h5> Ride Date: ${rideDate} </h5>
                    <ul class="w3-ul">
                        <li> Ride Date: ${startTime}</li>
                        <li> Start Time: ${endTime} </li>
                        <li> Status: ${status} </li>
                    </ul>
                 </div>`;
            document.getElementById('myRides').innerHTML = result;
        });
    })
