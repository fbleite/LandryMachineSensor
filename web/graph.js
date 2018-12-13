
function init() {
	/*fetch('https://hfg6wwwhx1.execute-api.us-east-1.amazonaws.com/prod/getLatestLaundryStatus')
	.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		runningMessage = "Laundry Machine ";
		if (JSON.stringify(myJson['body']['machineStatusOn']) == true) {
			runningMessage = runningMessage + "is running!";
		} else  {
			runningMessage = runningMessage + "is NOT running!";
		}
		document.getElementById("machineStatus").innerHTML = runningMessage;
		document.getElementById("timestamp").innerHTML = "Timestamp: " + myJson['body']['timestamp'];
	});
*/
	canvas = document.getElementById("myCanvas");
	ctx = canvas.getContext("2d");
	adjustCanvasSize ();
	intensityPoints = getMockLaundryDataPoints();
	intensityPoints = intensityPoints.sort(compareIntensityPoints);
	plotPoints(intensityPoints);

}

function compareIntensityPoints(a,b) {
  if (a.timestamp < b.timestamp)
    return -1;
  if (a.timestamp > b.timestamp)
    return 1;
  return 0;
}

function plotPoints(intensityPoints) {
	var maxIntensity = 3 + Math.ceil(intensityPoints.reduce(function (a, b) { return a.intensity > b.intensity ? a : b; }).intensity);
	var YPixelsPerIntensity = (canvas.height - (upperMargin + lowerMargin))/maxIntensity;
	var XPixelsPerPeriod = (canvas.width - (rightMargin + leftMargin))/intensityPoints.length;
	ctx.beginPath();
	ctx.moveTo(0 + leftMargin, canvas.height - lowerMargin - intensityPoints[0].intensity * YPixelsPerIntensity);
	for (var i = 1; i < intensityPoints.length; i++) {
		ctx.lineTo(i*XPixelsPerPeriod +leftMargin, canvas.height - lowerMargin - intensityPoints[i].intensity * YPixelsPerIntensity);
	}
	ctx.stroke();
	ctx.font = "15px Arial";
	ctx.fillText(maxIntensity, leftMargin - 30, upperMargin + 15);
}

function adjustCanvasSize () {
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

window.addEventListener("resize", function() {
	adjustCanvasSize ();
	plotPoints(intensityPoints);
});

function IntensityPoint(machineOn, timestamp, intensity) {
	this.machineOn = machineOn;
	this.timestamp = timestamp;
	this.intensity = intensity;
}

function getLaundryDataPoints() {
	fetch('https://hfg6wwwhx1.execute-api.us-east-1.amazonaws.com/prod/getlaundrystatusrange')
	.then(function(response) {
		return response.json();
	})
	.then(function(dataPoints) {
		console.log(dataPoints['body'][1]['timestamp']);
		document.getElementById("here").innerHTML = JSON.stringify(dataPoints['body']);
	});

}

var mockTimestamp = new Date(Date.parse("2018-12-12T19:03:24.384950"));
var mockIntensity = 3;

function getMockLaundryDataPoints() {
	for (var i=0; i <=(800*240); i ++) {
		intensityPoints.push(new IntensityPoint(false, mockTimestamp, mockIntensity));
		mockTimestamp.setSeconds(mockTimestamp.getSeconds() + 15);
		mockIntensity = mockIntensity + Math.random() - 0.5;
		if (mockIntensity < 0){
			mockIntensity ++;
		}
	}
	return intensityPoints;
}

var canvas = null;
var ctx = null;
var intensityPoints = [];
var lowerMargin = null;
var upperMargin = null;
var rightMargin = null;
var leftMargin = null;
window.onload = init;
