fetch('https://o3wnr9f61e.execute-api.us-east-1.amazonaws.com/test/test')
    .then(function (res) {
        return res.json();
    })
    .then(function (data) {
        let result = ``;
        data.forEach((user) => {
            const { name, rideDate, startTime, endTime } = user
            result +=
                `<div class="lists">
                    <h5> Ride Date: ${rideDate} </h5>
                    <ul class="w3-ul">
                        <li> Ride Date: ${startTime}</li>
                        <li> Start Time: ${endTime} </li>
                    </ul>
                 </div>`;
            document.getElementById('myRides').innerHTML = result;
        });
    })
