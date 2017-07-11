Chart.defaults.animation.duration = 0 // general animation time
Chart.defaults.hover.animationDuration = 0 // duration of animations when hovering an item
Chart.defaults.responsiveAnimationDuration = 0 // animation duration after a resize

$.datepicker.setDefaults({
    minDate: new Date(2016, 8, 1),
    maxDate: new Date(2017, 4, 31),
    duration: "fast",
    showAnim: ""
});

var chartData = {
    labels: [],
    datasets: [{
    label: 'temperature',
    data: [],
    fill: false,
    // line color; red, opacity: 40%
    borderColor: "rgba(255, 0, 0, 0.4)",
    pointBorderColor: "rgba(255, 0, 0, 0.6)",
    pointBackgroundColor: "rgba(255, 0, 0, 0.6)",
    pointHoverBorderColor: "rgba(255, 0, 0, 1)",
    pointHoverBackgroundColor: "rgba(255, 0, 0, 1)"
    },
    {
    label: 'humidity',
    data: [],
    fill: false,
    // line color; blue, opacity: 40%
    borderColor: "rgba(0, 0, 255, 0.4)",
    pointBorderColor: "rgba(0, 0, 255, 0.6)",
    pointBackgroundColor: "rgba(0, 0, 255, 0.6)",
    pointHoverBorderColor: "rgba(0, 0, 255, 1)",
    pointHoverBackgroundColor: "rgba(0, 0, 255, 1)"
    }]
  },
  ctx = document.getElementById('lineChart').getContext("2d"),
  lineChart = new Chart(ctx, {
    type: 'line',
    data: chartData,
    options: {
        elements: {
            line: {
                tension: 0 // disables bezier curves
            }
        }
    }
  }),
  startAt = $( "#startAt" ).datepicker().on( "change", function() {
    endAt.datepicker( "option", "minDate", getDate( this ) );
  }),
  endAt = $( "#endAt" ).datepicker().on( "change", function() {
    startAt.datepicker( "option", "maxDate", getDate( this ) );
  });



function asyncDrawChart(apiUrl) {
    $.get( apiUrl ).done(function( atmoData ) {
        //console.log( atmoData.map(i => i['datetime']) );
        lineChart.data.labels = atmoData.map(function(i){ return i['datetime'] });
        lineChart.data.datasets[0].data = atmoData.map(function(i){ return i['temp'] });
        lineChart.data.datasets[1].data = atmoData.map(function(i){ return i['humd'] });
        lineChart.update(0);
    });
};

function getDate( element ) {
    var dateFormat = "mm/dd/yy",
      date;
    try {
        date = $.datepicker.parseDate( dateFormat, element.value );
    }
    catch( error ) {
        date = null;
    }
    return date;
};
