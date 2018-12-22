
function init() {
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext("2d");
    printGraph();
    // getMockPointsAndPlot();

}

function printGraph() {
    adjustCanvasSize();
    getPointsAndPlot();
}

function getMockPointsAndPlot() {
    var latestStatus = getMockLatestStatus();
    updateLatestStatus(latestStatus);
    intensityPoints = getMockLaundryDataPoints();
    plotPoints(intensityPoints);
}

function getPointsAndPlot() {

    fetch('https://hfg6wwwhx1.execute-api.us-east-1.amazonaws.com/prod/getLatestLaundryStatus')
        .then(function (response) {
            return response.json();
        })
        .then(function (myJson) {
            var timestamp = myJson['body']['timestamp'];
            return new IntensityPoint(myJson['body']['machineStatusOn'], timestamp, null) ;
        })
        .then(function (latestStatus) {
            updateLatestStatus(latestStatus);
            return latestStatus;
        })
        .then(function(latestStatus) {
            getLaundryDataPoints(latestStatus);
        }) ;
}

function updateLatestStatus(latestStatus) {
    var runningMessage = "Laundry Machine ";
    if (latestStatus.machineOn == true) {
        runningMessage = runningMessage + "is running!";
    } else {
        runningMessage = runningMessage + "is NOT running!";
    }
    document.getElementById("machineStatus").innerHTML = runningMessage;
    document.getElementById("timestamp").innerHTML = "Timestamp: " + latestStatus.timestamp.toString();
}

function getMockLatestStatus() {
    var machineOn = Math.random() > 0.5 ? true : false;
    var timestamp = new Date(Date.now());
    var intensity = Math.random() * 15;
    return new IntensityPoint(machineOn, timestamp, intensity);
}

function compareIntensityPoints(a, b) {
    if (a.timestamp < b.timestamp)
        return -1;
    if (a.timestamp > b.timestamp)
        return 1;
    return 0;
}

function plotPoints(intensityPoints) {
    var maxIntensity = 3 + Math.ceil(intensityPoints.reduce(function (a, b) { return a.intensity > b.intensity ? a : b; }).intensity);
    var YPixelsPerIntensity = (canvas.height - (upperMargin + lowerMargin)) / maxIntensity;
    var XPixelsPerPeriod = (canvas.width - (rightMargin + leftMargin)) / intensityPoints.length;
    ctx.beginPath();
    ctx.moveTo(0 + leftMargin, canvas.height - lowerMargin - intensityPoints[0].intensity * YPixelsPerIntensity);
    for (var i = 1; i < intensityPoints.length; i++) {
        ctx.lineTo(i * XPixelsPerPeriod + leftMargin, canvas.height - lowerMargin - intensityPoints[i].intensity * YPixelsPerIntensity);
    }
    ctx.stroke();
    ctx.font = "15px Arial";
    ctx.fillText(maxIntensity, leftMargin - 30, upperMargin + 15);
}

function adjustCanvasSize() {
    canvas.width = window.innerWidth * 0.9;
    canvas.height = window.innerHeight * 0.4;
    lowerMargin = canvas.height * 0.1;
    upperMargin = canvas.height * 0.1;
    leftMargin = canvas.width * 0.05;
    rightMargin = canvas.width * 0.01;
    ctx.beginPath();
    ctx.moveTo(leftMargin, upperMargin);
    ctx.lineTo(canvas.width - rightMargin, upperMargin);
    ctx.lineTo(canvas.width - rightMargin, canvas.height - lowerMargin);
    ctx.lineTo(leftMargin, canvas.height - lowerMargin);
    ctx.lineTo(leftMargin, upperMargin);
    ctx.stroke();
}

function IntensityPoint(machineOn, timestamp, intensity) {
    this.machineOn = machineOn;
    this.timestamp = new Date(timestamp);
    this.timestampISO = timestamp;
    this.intensity = intensity;
}

function getLaundryDataPoints(latestStatus) {
    var url = new URL('https://hfg6wwwhx1.execute-api.us-east-1.amazonaws.com/prod/getlaundrystatusrange'),
    
    params = {timestamp:latestStatus.timestampISO, window:getWindowValue()}
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]))   

    fetch(url)
        .then(function (response) {
            return response.json();
        })
        .then(function (dataPoints) {
            intensityPoints = [];
            dataPoints['points'].forEach(point => {
                intensityPoints.push(new IntensityPoint(point['machineStatusOn'], 
                                    point['timestamp'],
                                    point['currentIntensity']));
            });
            return intensityPoints.sort(compareIntensityPoints);
        })
        .then(function (intensityPoints) {
            plotPoints(intensityPoints);
        });
}

function getWindowValue() {
    var e = document.getElementById("graphWindow");
    return e.options[e.selectedIndex].value;
}

function getMockLaundryDataPoints() {
    for (var i = 0; i <= (80 * 240); i++) {
        intensityPoints.push(new IntensityPoint(false, mockTimestamp, mockIntensity));
        mockTimestamp.setSeconds(mockTimestamp.getSeconds() + 15);
        mockIntensity = mockIntensity + Math.random() - 0.5;
        if (mockIntensity < 0) {
            mockIntensity++;
        }
    }
    return intensityPoints.sort(compareIntensityPoints);
}

var canvas = null;
var ctx = null;
var intensityPoints = [];
var lowerMargin = null;
var upperMargin = null;
var rightMargin = null;
var leftMargin = null;

var mockTimestamp = new Date(Date.parse("2018-12-12T19:03:24.384950"));
var mockIntensity = 3;


window.onload = init;

window.addEventListener("resize", function () {
    adjustCanvasSize();
    plotPoints(intensityPoints);
});
