type = ['primary', 'info', 'success', 'warning', 'danger'];

demo = {
  initPickColor: function() {
    $('.pick-class-label').click(function() {
      var new_class = $(this).attr('new-class');
      var old_class = $('#display-buttons').attr('data-class');
      var display_div = $('#display-buttons');
      if (display_div.length) {
        var display_buttons = display_div.find('.btn');
        display_buttons.removeClass(old_class);
        display_buttons.addClass(new_class);
        display_div.attr('data-class', new_class);
      }
    });
  },

  initDocChart: function() {
    chartColor = "#FFFFFF";

    // General configuration for the charts with Line gradientStroke
    gradientChartOptionsConfiguration = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      tooltips: {
        bodySpacing: 4,
        mode: "nearest",
        intersect: 0,
        position: "nearest",
        xPadding: 10,
        yPadding: 10,
        caretPadding: 10
      },
      responsive: true,
      scales: {
        yAxes: [{
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        }],
        xAxes: [{
          display: 0,
          gridLines: 0,
          ticks: {
            display: false
          },
          gridLines: {
            zeroLineColor: "transparent",
            drawTicks: false,
            display: false,
            drawBorder: false
          }
        }]
      },
      layout: {
        padding: {
          left: 0,
          right: 0,
          top: 15,
          bottom: 15
        }
      }
    };

    ctx = document.getElementById('lineChartExample').getContext("2d");

    gradientStroke = ctx.createLinearGradient(500, 0, 100, 0);
    gradientStroke.addColorStop(0, '#80b6f4');
    gradientStroke.addColorStop(1, chartColor);

    gradientFill = ctx.createLinearGradient(0, 170, 0, 50);
    gradientFill.addColorStop(0, "rgba(128, 182, 244, 0)");
    gradientFill.addColorStop(1, "rgba(249, 99, 59, 0.40)");

    myChart = new Chart(ctx, {
      type: 'line',
      responsive: true,
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        datasets: [{
          label: "Active Users",
          borderColor: "#f96332",
          pointBorderColor: "#FFF",
          pointBackgroundColor: "#f96332",
          pointBorderWidth: 2,
          pointHoverRadius: 4,
          pointHoverBorderWidth: 1,
          pointRadius: 4,
          fill: true,
          backgroundColor: gradientFill,
          borderWidth: 2,
          data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 630]
        }]
      },
      options: gradientChartOptionsConfiguration
    });
  },






  initDashboardPageCharts: function() {

    gradientChartOptionsConfigurationWithTooltipBlue = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#2380f7"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#2380f7"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipPurple = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 60,
            suggestedMax: 125,
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(225,78,202,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9a9a9a"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipOrange = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 110,
            padding: 20,
            fontColor: "#ff8a76"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(220,53,69,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#ff8a76"
          }
        }]
      }
    };

    gradientChartOptionsConfigurationWithTooltipGreen = {
      maintainAspectRatio: false,
      legend: {
        display: false
      },

      tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.0)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 50,
            suggestedMax: 60,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],

        xAxes: [{
          barPercentage: 1.6,
          gridLines: {
            drawBorder: false,
            color: 'rgba(0,242,195,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }]
      }
    };


    gradientBarChartConfiguration = {
        maintainAspectRatio: false,
        legend: {
            display: false
        },
        tooltips: {
        backgroundColor: '#f5f5f5',
        titleFontColor: '#333',
        bodyFontColor: '#666',
        bodySpacing: 4,
        xPadding: 12,
        mode: "nearest",
        intersect: 0,
        position: "nearest"
      },
      responsive: true,
      scales: {
        yAxes: [{
          gridLines: {
            drawBorder: false,
            color: 'rgba(29,140,248,0.1)',
            zeroLineColor: "transparent",
          },
          ticks: {
            suggestedMin: 0,
            suggestedMax: 60,
            padding: 20,
            fontColor: "#9e9e9e"
          }
        }],
          xAxes: [{

              gridLines: {
                  drawBorder: false,
                  color: 'rgba(29,140,248,0.1)',
                  zeroLineColor: "transparent",
              },
              ticks: {
                  padding: 20,
                  fontColor: "#9e9e9e",
              }
          }]

      }
    };

      Chart.pluginService.register({
          beforeDraw: function (chart) {
              if (chart.config.options.elements.center) {
                  // Get ctx from string
                  var ctx = chart.chart.ctx;

                  // Get options from the center object in options
                  var centerConfig = chart.config.options.elements.center;
                  var fontStyle = centerConfig.fontStyle || 'Arial';
                  var txt = centerConfig.text;
                  var color = centerConfig.color || '#000';
                  var maxFontSize = centerConfig.maxFontSize || 75;
                  var sidePadding = centerConfig.sidePadding || 20;
                  var sidePaddingCalculated = (sidePadding / 100) * (chart.innerRadius * 2)
                  // Start with a base font of 30px
                  ctx.font = "30px " + fontStyle;

                  // Get the width of the string and also the width of the element minus 10 to give it 5px side padding
                  var stringWidth = ctx.measureText(txt).width;
                  var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

                  // Find out how much the font can grow in width.
                  var widthRatio = elementWidth / stringWidth;
                  var newFontSize = Math.floor(30 * widthRatio);
                  var elementHeight = (chart.innerRadius * 2);

                  // Pick a new font size so it will not be larger than the height of label.
                  var fontSizeToUse = Math.min(newFontSize, elementHeight, maxFontSize);
                  var minFontSize = centerConfig.minFontSize;
                  var lineHeight = centerConfig.lineHeight || 25;
                  var wrapText = false;

                  if (minFontSize === undefined) {
                      minFontSize = 20;
                  }

                  if (minFontSize && fontSizeToUse < minFontSize) {
                      fontSizeToUse = minFontSize;
                      wrapText = true;
                  }

                  // Set font settings to draw it correctly.
                  ctx.textAlign = 'center';
                  ctx.textBaseline = 'middle';
                  var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
                  var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
                  ctx.font = fontSizeToUse + "px " + fontStyle;
                  ctx.fillStyle = color;

                  if (!wrapText) {
                      ctx.fillText(txt, centerX, centerY);
                      return;
                  }

                  var words = txt.split(' ');
                  var line = '';
                  var lines = [];

                  // Break words up into multiple lines if necessary
                  for (var n = 0; n < words.length; n++) {
                      var testLine = line + words[n] + ' ';
                      var metrics = ctx.measureText(testLine);
                      var testWidth = metrics.width;
                      if (testWidth > elementWidth && n > 0) {
                          lines.push(line);
                          line = words[n] + ' ';
                      } else {
                          line = testLine;
                      }
                  }

                  // Move the center up depending on line height and number of lines
                  centerY -= (lines.length / 2) * lineHeight;

                  for (var n = 0; n < lines.length; n++) {
                      ctx.fillText(lines[n], centerX, centerY);
                      centerY += lineHeight;
                  }
                  //Draw text in center
                  ctx.fillText(line, centerX, centerY);
              }
          }
      });

    PieChartConfiguration = {
        maintainAspectRatio: false,
        legend: {
            display: true,
            position: "bottom",
        },

        tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "nearest",
            intersect: 0,
            position: "nearest"
        },
        plugins: {
            datalabels: {
                display: true,
                align: 'bottom',
                backgroundColor: '#ccc',
                borderRadius: 3,
                font: {
                    size: 18,
                },
            },
        },
        elements: {
            center: {
                text: 'Sentiment',
                color: '#d346b1', // Default is #000000
                fontStyle: 'Arial', // Default is Arial
                sidePadding: 20, // Default is 20 (as a percentage)
                minFontSize: 12, // Default is 20 (in px), set to false and text will not wrap.
                lineHeight: 25 // Default is 25 (in px), used for when text wraps
            }
        },
        responsive: true,
      };

      var ctx = document.getElementById("chartLinePurple").getContext("2d");

      var chart_datasetspie = [];
      var chart_labelspie = [];

    var data = {
        labels: chart_labelspie,
        datasets: chart_datasetspie
      };

      var myChartpie = new Chart(ctx, {
          type: 'doughnut',
          data: data,
          options: PieChartConfiguration
      });

      $.ajax({
          type: 'GET',
          url: 'http://127.0.0.1:5000/sentimentpiechart',
          data: {},
          success: function (data) {
              updatepiechart(data)
          },
          error: function (response) {
              console.log(reponse)
          }
      });



      function updatepiechart(data) {
          $('#total_messages').text('  number of messages: ' + JSON.parse(data).data.messagesCount)

          var chart_datasets = [];
          var chart_labels = [];
          var chart_data = [];

        console.log(data)
        chart_data.push(JSON.parse(data).data.negativeCount)
        chart_data.push(JSON.parse(data).data.neutralCount)
        chart_data.push(JSON.parse(data).data.positiveCount)

        chart_labels.push(JSON.parse(data).labels.negativeLabel)
        chart_labels.push(JSON.parse(data).labels.neutralLabel)
        chart_labels.push(JSON.parse(data).labels.positiveLabel)


        chart_datasets.push({
            label: 'Sentiment',
            data: chart_data,
            backgroundColor: gradientStroke,
            borderColor: '#301934',
            borderWidth: 1,
            backgroundColor: [
                '#D30000',
                '#FFA500',
                '#00FF00'
            ],
            hoverOffset: 4
        })

        var data = myChartpie.config.data;
        data.datasets = chart_datasets;
        data.labels = chart_labels;
        myChartpie.update();
      }

      function refreshState() {
          $.ajax({
              type: 'GET',
              url: 'http://127.0.0.1:5000/getstatedatabase',
              data: {},
              success: function (data) {
                  databasestate(data)
              },
              error: function (response) {
                  console.log(reponse)
              }
          });
      }

      function databasestate(data) {
          timeStamp = data.timeStamp
          actualObject = data.actualObject
          timeStamp.replace('GMT', '')
          $('#last_time_sync').text(timeStamp)
          $('#status').text(actualObject)
      }

      setInterval(
          function () {
              refreshState()
          },
          4000  /* 10000 ms = 10 sec */
      );

      $("#sync").click(function () {


          $.ajax({
              type: 'GET',
              url: 'http://127.0.0.1:5000/updatedatabase',
              data: {},
              success: function (data) {
                  //databasestate(data)
              },
              error: function (response) {
                  console.log(reponse)
              }
          });

      });

      $.ajax({
          type: 'GET',
          url: 'http://127.0.0.1:5000/messagebychat',
          data: {},
          success: function (data) {
              addChatsToPostTable(data)
          },
          error: function (response) {
              console.log(reponse)
          }
      });


      function addChatsToPostTable(data) {
          $('#posttable').empty()
          $.each(JSON.parse(data).data, function (index, element) {
              $('#posttable').append(`<tr><td>${JSON.parse(element).chatName}</td>  <td>${JSON.parse(element).messages}</td>  <td>${JSON.parse(element).precentOfTotal}</td> </tr>`);
          });
      }

    //add chats to filter
    function addChatsToFilter(data) {
        $('#select_chat').empty()
        $.each(JSON.parse(data).data, function (index, element) {
            $('#select_chat').append(`<option value="${JSON.parse(element).chatId}">
                                    ${JSON.parse(element).chatName}
                                </option>`);
        });
      }

      var chatFilter = []
      var timerange = 24
    //filter chats
      $("#filter_chat").click(function () {
        chatFilter = []
        $('#select_chat option').each(function () {
            chatFilter.push({ 'chatId': this.value, 'chatName': this.innerText, 'option': ($(this).is(':selected'))})
        });
        updatetextnumberoffilteredchats()
        filterdata()
      });

      function updatetextnumberoffilteredchats() {
          if (chatFilter.filter(x => x.option).length > 0) {
              $('#number_filtered_chats').text('show ' + chatFilter.filter(x => x.option).length + ' chats')
          } else {
              $('#number_filtered_chats').text('show all chats')
          }
      }

      $("#clear_filter_chats").click(function () {
          $('#select_chat option').each(function () {
              this.selected = false
          });
          chatFilter = []
          updatetextnumberoffilteredchats()
          filterdata()
      });

      function filterdata() {
          $.ajax({
              url: '/messagelinediagram',
              type: 'POST',
              data: JSON.stringify({
                  'chatFilter': chatFilter,
                  'timerange': timerange,
              }),
              contentType: 'application/json;charset=UTF-8',
              cache: false,
              success: function (data) {
                  updatelinediagram(data)
              },
              error: function (response) {
                  console.log(reponse)
              }
          });

          $.ajax({
              url: '/sentimentpiechart',
              type: 'POST',
              data: JSON.stringify({
                  'chatFilter': chatFilter,
                  'timerange': timerange,
              }),
              contentType: 'application/json;charset=UTF-8',
              cache: false,
              success: function (data) {
                  updatepiechart(data)
              },
              error: function (response) {
                  console.log(response)
              }
          });

          $.ajax({
              type: 'POST',
              url: 'http://127.0.0.1:5000/messagebychat',
              data: JSON.stringify({
                  'chatFilter': chatFilter,
                  'timerange': timerange,
              }),
              contentType: 'application/json;charset=UTF-8',
              cache: false,
              success: function (data) {
                  addChatsToPostTable(data)
              },
              error: function (response) {
                  console.log(reponse)
              }
          });
      }


    var colorArray = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
        '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
        '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
        '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
        '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
        '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
        '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
        '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
        '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
        '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];

      var chart_datasets = [];
      var chart_labels = [];

    $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:5000/messagelinediagram',
        data: { },
        success: function (data) {
            updatelinediagram(data)
            addChatsToFilter(data)
        },
        error: function (response) {
            console.log(reponse)
        }
    });

    function updatelinediagram(data) {
        var count = 0
        var chart_datasets = [];
        var chart_labels = [];
        var chart_data = [];
        $.each(JSON.parse(data).data, function (index, element) {
            chart_data = []
            $.each(JSON.parse(element).messages, function (index, element1) {
                chart_data.push(JSON.parse(element1).number)
                console.log(JSON.parse(element))
            });
            chart_datasets.push({
                label: JSON.parse(element).chatName,
                fill: true,
                backgroundColor: gradientStroke,
                borderColor: colorArray[count],
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: colorArray[count],
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: '#d346b1',
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
                fill: false,
                data: chart_data,
            })
            count++
        });
        $.each(JSON.parse(data).labels, function (index, element) {
            chart_labels.push(JSON.parse(element).date)
        });
        var data = myChartData.config.data;
        data.datasets = chart_datasets;
        data.labels = chart_labels;
        myChartData.update();
      }



    var ctx = document.getElementById("chartBig1").getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
    gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors



    var config = {
        type: 'line',
        data: {
            labels: chart_labels,
            datasets: chart_datasets
        },
        options: gradientChartOptionsConfigurationWithTooltipPurple
    };
    var myChartData = new Chart(ctx, config);

      $("#0").click(function () {
        timerange = 24
        filterdata()
    });

    $("#1").click(function() {
        timerange = 12
        filterdata()
    });

    $("#2").click(function() {
        timerange = 6
        filterdata()
    });


      var labelsbarchart = []
      var datasetsbarchart = []

    var ctx = document.getElementById("CountryChart").getContext("2d");

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(0.7, 'rgba(248,40,29,0.4)');
    gradientStroke.addColorStop(0.5, 'rgba(248,40,29,0.2)');
      gradientStroke.addColorStop(0, 'rgba(248,40,29,0.0)'); //res colors

      var myChartBar = new Chart(ctx, {
          type: 'bar',
          responsive: true,
          legend: {
              display: true
          },
          data: {
              labels: labelsbarchart,
              datasets: datasetsbarchart
          },
          options: gradientBarChartConfiguration
      });

      $.ajax({
        type: 'GET',
            url: 'http://127.0.0.1:5000/negativesentimentbarchart',
                data: { },
        success: function (data) {
            updatebarchart(data)
        },
        error: function (response) {
            console.log(reponse)
        }
      });

    function truncate(str, n){
        return (str.length > n) ? str.slice(0, n-1) + '..' : str;
    };


      function updatebarchart(data) {
          var chart_datasets = [];
          var chart_labels = [];
          var chart_data = [];

          $('#total_negative_messages').text(' total ' + JSON.parse(data).totalnegativemessages + ' negative messages')
          chart_data.push(JSON.parse(JSON.parse(data).data[0]).num)
          chart_data.push(JSON.parse(JSON.parse(data).data[1]).num)
          chart_data.push(JSON.parse(JSON.parse(data).data[2]).num)
          chart_data.push(JSON.parse(JSON.parse(data).data[3]).num)
          chart_data.push(JSON.parse(JSON.parse(data).data[4]).num)


          chart_labels.push(truncate(JSON.parse(JSON.parse(data).labels)[0], 15))
          chart_labels.push(truncate(JSON.parse(JSON.parse(data).labels)[1], 15))
          chart_labels.push(truncate(JSON.parse(JSON.parse(data).labels)[2], 15))
          chart_labels.push(truncate(JSON.parse(JSON.parse(data).labels)[3], 15))
          chart_labels.push(truncate(JSON.parse(JSON.parse(data).labels)[4], 15))

          chart_datasets.push({
              label: "Negative messages",
              fill: true,
              backgroundColor: gradientStroke,
              hoverBackgroundColor: gradientStroke,
              borderColor: '#f11e1f',
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: chart_data
          })

          var data = myChartBar.config.data;
          data.datasets = chart_datasets;
          data.labels = chart_labels;
          myChartBar.update();
        }
    },

  initGoogleMaps: function() {
    var myLatlng = new google.maps.LatLng(40.748817, -73.985428);
    var mapOptions = {
      zoom: 13,
      center: myLatlng,
      scrollwheel: false, //we disable de scroll over the map, it is a really annoing when you scroll through page
      styles: [{
          "elementType": "geometry",
          "stylers": [{
            "color": "#1d2c4d"
          }]
        },
        {
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#8ec3b9"
          }]
        },
        {
          "elementType": "labels.text.stroke",
          "stylers": [{
            "color": "#1a3646"
          }]
        },
        {
          "featureType": "administrative.country",
          "elementType": "geometry.stroke",
          "stylers": [{
            "color": "#4b6878"
          }]
        },
        {
          "featureType": "administrative.land_parcel",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#64779e"
          }]
        },
        {
          "featureType": "administrative.province",
          "elementType": "geometry.stroke",
          "stylers": [{
            "color": "#4b6878"
          }]
        },
        {
          "featureType": "landscape.man_made",
          "elementType": "geometry.stroke",
          "stylers": [{
            "color": "#334e87"
          }]
        },
        {
          "featureType": "landscape.natural",
          "elementType": "geometry",
          "stylers": [{
            "color": "#023e58"
          }]
        },
        {
          "featureType": "poi",
          "elementType": "geometry",
          "stylers": [{
            "color": "#283d6a"
          }]
        },
        {
          "featureType": "poi",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#6f9ba5"
          }]
        },
        {
          "featureType": "poi",
          "elementType": "labels.text.stroke",
          "stylers": [{
            "color": "#1d2c4d"
          }]
        },
        {
          "featureType": "poi.park",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#023e58"
          }]
        },
        {
          "featureType": "poi.park",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#3C7680"
          }]
        },
        {
          "featureType": "road",
          "elementType": "geometry",
          "stylers": [{
            "color": "#304a7d"
          }]
        },
        {
          "featureType": "road",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#98a5be"
          }]
        },
        {
          "featureType": "road",
          "elementType": "labels.text.stroke",
          "stylers": [{
            "color": "#1d2c4d"
          }]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry",
          "stylers": [{
            "color": "#2c6675"
          }]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#9d2a80"
          }]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry.stroke",
          "stylers": [{
            "color": "#9d2a80"
          }]
        },
        {
          "featureType": "road.highway",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#b0d5ce"
          }]
        },
        {
          "featureType": "road.highway",
          "elementType": "labels.text.stroke",
          "stylers": [{
            "color": "#023e58"
          }]
        },
        {
          "featureType": "transit",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#98a5be"
          }]
        },
        {
          "featureType": "transit",
          "elementType": "labels.text.stroke",
          "stylers": [{
            "color": "#1d2c4d"
          }]
        },
        {
          "featureType": "transit.line",
          "elementType": "geometry.fill",
          "stylers": [{
            "color": "#283d6a"
          }]
        },
        {
          "featureType": "transit.station",
          "elementType": "geometry",
          "stylers": [{
            "color": "#3a4762"
          }]
        },
        {
          "featureType": "water",
          "elementType": "geometry",
          "stylers": [{
            "color": "#0e1626"
          }]
        },
        {
          "featureType": "water",
          "elementType": "labels.text.fill",
          "stylers": [{
            "color": "#4e6d70"
          }]
        }
      ]
    };

    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
      position: myLatlng,
      title: "Hello World!"
    });

    // To add the marker to the map, call setMap();
    marker.setMap(map);
  },

  showNotification: function(from, align) {
    color = Math.floor((Math.random() * 4) + 1);

    $.notify({
      icon: "tim-icons icon-bell-55",
      message: "Welcome to <b>Black Dashboard</b> - a beautiful freebie for every web developer."

    }, {
      type: type[color],
      timer: 8000,
      placement: {
        from: from,
        align: align
      }
    });
  },

  initSpecificChatPageCharts: function () {

        gradientChartOptionsConfigurationWithTooltipBlue = {
            maintainAspectRatio: false,
            legend: {
                display: false
            },

            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            responsive: true,
            scales: {
                yAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.0)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        suggestedMin: 60,
                        suggestedMax: 125,
                        padding: 20,
                        fontColor: "#2380f7"
                    }
                }],

                xAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#2380f7"
                    }
                }]
            }
        };

        gradientChartOptionsConfigurationWithTooltipPurple = {
            maintainAspectRatio: false,
            legend: {
                display: true,
                fill: true
            },

            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            responsive: true,
            scales: {
                yAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.0)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        suggestedMin: 60,
                        suggestedMax: 125,
                        padding: 20,
                        fontColor: "#9a9a9a"
                    }
                }],

                xAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(225,78,202,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#9a9a9a"
                    }
                }]
            }
        };

        gradientChartOptionsConfigurationWithTooltipOrange = {
            maintainAspectRatio: false,
            legend: {
                display: false
            },

            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            responsive: true,
            scales: {
                yAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.0)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        suggestedMin: 50,
                        suggestedMax: 110,
                        padding: 20,
                        fontColor: "#ff8a76"
                    }
                }],

                xAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(220,53,69,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#ff8a76"
                    }
                }]
            }
        };

        gradientChartOptionsConfigurationWithTooltipGreen = {
            maintainAspectRatio: false,
            legend: {
                display: false
            },

            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            responsive: true,
            scales: {
                yAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.0)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        suggestedMin: 50,
                        suggestedMax: 60,
                        padding: 20,
                        fontColor: "#9e9e9e"
                    }
                }],

                xAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(0,242,195,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#9e9e9e"
                    }
                }]
            }
        };


        gradientBarChartConfiguration = {
            maintainAspectRatio: false,
            legend: {
                display: false
            },
            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            responsive: true,
            scales: {
                yAxes: [{
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        suggestedMin: 0,
                        suggestedMax: 60,
                        padding: 20,
                        fontColor: "#9e9e9e"
                    }
                }],
                xAxes: [{

                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.1)',
                        zeroLineColor: "transparent",
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#9e9e9e",
                    }
                }]

            }
        };

        Chart.pluginService.register({
            beforeDraw: function (chart) {
                if (chart.config.options.elements.center) {
                    // Get ctx from string
                    var ctx = chart.chart.ctx;

                    // Get options from the center object in options
                    var centerConfig = chart.config.options.elements.center;
                    var fontStyle = centerConfig.fontStyle || 'Arial';
                    var txt = centerConfig.text;
                    var color = centerConfig.color || '#000';
                    var maxFontSize = centerConfig.maxFontSize || 75;
                    var sidePadding = centerConfig.sidePadding || 20;
                    var sidePaddingCalculated = (sidePadding / 100) * (chart.innerRadius * 2)
                    // Start with a base font of 30px
                    ctx.font = "30px " + fontStyle;

                    // Get the width of the string and also the width of the element minus 10 to give it 5px side padding
                    var stringWidth = ctx.measureText(txt).width;
                    var elementWidth = (chart.innerRadius * 2) - sidePaddingCalculated;

                    // Find out how much the font can grow in width.
                    var widthRatio = elementWidth / stringWidth;
                    var newFontSize = Math.floor(30 * widthRatio);
                    var elementHeight = (chart.innerRadius * 2);

                    // Pick a new font size so it will not be larger than the height of label.
                    var fontSizeToUse = Math.min(newFontSize, elementHeight, maxFontSize);
                    var minFontSize = centerConfig.minFontSize;
                    var lineHeight = centerConfig.lineHeight || 25;
                    var wrapText = false;

                    if (minFontSize === undefined) {
                        minFontSize = 20;
                    }

                    if (minFontSize && fontSizeToUse < minFontSize) {
                        fontSizeToUse = minFontSize;
                        wrapText = true;
                    }

                    // Set font settings to draw it correctly.
                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    var centerX = ((chart.chartArea.left + chart.chartArea.right) / 2);
                    var centerY = ((chart.chartArea.top + chart.chartArea.bottom) / 2);
                    ctx.font = fontSizeToUse + "px " + fontStyle;
                    ctx.fillStyle = color;

                    if (!wrapText) {
                        ctx.fillText(txt, centerX, centerY);
                        return;
                    }

                    var words = txt.split(' ');
                    var line = '';
                    var lines = [];

                    // Break words up into multiple lines if necessary
                    for (var n = 0; n < words.length; n++) {
                        var testLine = line + words[n] + ' ';
                        var metrics = ctx.measureText(testLine);
                        var testWidth = metrics.width;
                        if (testWidth > elementWidth && n > 0) {
                            lines.push(line);
                            line = words[n] + ' ';
                        } else {
                            line = testLine;
                        }
                    }

                    // Move the center up depending on line height and number of lines
                    centerY -= (lines.length / 2) * lineHeight;

                    for (var n = 0; n < lines.length; n++) {
                        ctx.fillText(lines[n], centerX, centerY);
                        centerY += lineHeight;
                    }
                    //Draw text in center
                    ctx.fillText(line, centerX, centerY);
                }
            }
        });

        PieChartConfiguration = {
            maintainAspectRatio: false,
            legend: {
                display: true,
                position: "bottom",
            },

            tooltips: {
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,
                xPadding: 12,
                mode: "nearest",
                intersect: 0,
                position: "nearest"
            },
            plugins: {
                datalabels: {
                    display: true,
                    align: 'bottom',
                    backgroundColor: '#ccc',
                    borderRadius: 3,
                    font: {
                        size: 18,
                    },
                },
            },
            elements: {
                center: {
                    text: 'Sentiment',
                    color: '#d346b1', // Default is #000000
                    fontStyle: 'Arial', // Default is Arial
                    sidePadding: 20, // Default is 20 (as a percentage)
                    minFontSize: 12, // Default is 20 (in px), set to false and text will not wrap.
                    lineHeight: 25 // Default is 25 (in px), used for when text wraps
                }
            },
            responsive: true,
        };

        function refreshState() {
            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:5000/getstatedatabase',
                data: {},
                success: function (data) {
                    databasestate(data)
                },
                error: function (response) {
                    console.log(reponse)
                }
            });
        }

        function databasestate(data) {
            timeStamp = data.timeStamp
            actualObject = data.actualObject
            timeStamp.replace('GMT', '')
            $('#last_time_sync').text(timeStamp)
            $('#status').text(actualObject)
        }

        setInterval(
            function () {
                refreshState()
            },
            4000  /* 10000 ms = 10 sec */
        );

        $("#sync").click(function () {


            $.ajax({
                type: 'GET',
                url: 'http://127.0.0.1:5000/updatedatabase',
                data: {},
                success: function (data) {
                    //databasestate(data)
                },
                error: function (response) {
                    console.log(reponse)
                }
            });

        });

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/mostUsedWords',
            data: {},
            success: function (data) {
                addChatsToPostTable(data)
            },
            error: function (response) {
                console.log(reponse)
            }
        });


        function addChatsToPostTable(data) {
            $('#posttable').empty()
            $.each(JSON.parse(data).data, function (index, element) {
                var row = "<tr><td>" + JSON.parse(element).date + "</td>"
                $.each(JSON.parse(element).mostUsedCombination, function (index1, element1) {
                    row += "<td>" + element1.replaceAll('"', '') + "</td>"
                });
                row += "</tr>"
                $('#posttable').append(row);
            });
      }

      $.ajax({
          type: 'GET',
          url: 'http://127.0.0.1:5000/chats',
          data: {},
          success: function (data) {
              addChatsToFilter(data)
          },
          error: function (response) {
              console.log(reponse)
          }
      });

        //add chats to filter
        function addChatsToFilter(data) {
            $('#select_chat').empty()
            $.each(JSON.parse(data).data, function (index, element) {
                $('#select_chat').append(`<option value="${JSON.parse(element).chatId}">
                                    ${JSON.parse(element).chatName}
                                </option>`);
                if (JSON.parse(element).selected) {
                    $('#select_chat').val(JSON.parse(element).chatId).change();
                }
            });
            filterchats()
        }

        var chatFilter = []
        var sentimentFilter = []
        var timerange = 24
        //filter chats
        $("#filter_chat").click(function () {
            filterchats()
        });

      function filterchats() {
          chatFilter = []
          sentimentFilter = []
          $('#select_chat option').each(function () {
              chatFilter.push({ 'chatId': this.value, 'chatName': this.innerText, 'option': $('#select_chat').find(":selected").val() == this.value })
          });
          $('#select_sentiment option').each(function () {
              sentimentFilter.push({ 'sentimentId': this.value, 'sentiment': this.innerText, 'option': $('#select_sentiment').find(":selected").val() == this.value })
          });

          updatetextnumberoffilteredchats()
          filterdata()
      }

      function updatetextnumberoffilteredchats() {
          selectedchat = ""
          selectedsentiment = ""
          $.each(chatFilter, function (index, element) {
              console.log(element.chatId)
              if (element.option) {
                  selectedchat = element.chatName
              }
          });

          $.each(sentimentFilter, function (index, element) {
              if (element.option) {
                  selectedsentiment = element.sentiment
              }
          });
          $('#number_filtered_chats').text('show ' + selectedchat + ' sentiment ' + selectedsentiment)
      }

        $("#clear_filter_chats").click(function () {
            $('#select_chat option').each(function () {
                this.selected = false
            });
            chatFilter = []
            updatetextnumberoffilteredchats()
            filterdata()
        });

        function filterdata() {
            $.ajax({
                url: '/sentimentmessageslinediagram',
                type: 'POST',
                data: JSON.stringify({
                    'chatFilter': chatFilter,
                    'sentimentFilter': sentimentFilter,
                    'timerange': timerange,
                }),
                contentType: 'application/json;charset=UTF-8',
                cache: false,
                success: function (data) {
                    updatelinediagram(data)
                },
                error: function (response) {
                    console.log(reponse)
                }
            });

            $.ajax({
                url: '/MostUsedVerbs',
                type: 'POST',
                data: JSON.stringify({
                    'chatFilter': chatFilter,
                    'sentimentFilter': sentimentFilter,
                    'timerange': timerange,
                }),
                contentType: 'application/json;charset=UTF-8',
                cache: false,
                success: function (data) {
                    updatewordcloud(data)
                },
                error: function (response) {
                    console.log(response)
                }
            });

            $.ajax({
                url: '/MostUsedLocations',
                type: 'POST',
                data: JSON.stringify({
                    'chatFilter': chatFilter,
                    'sentimentFilter': sentimentFilter,
                    'timerange': timerange,
                }),
                contentType: 'application/json;charset=UTF-8',
                cache: false,
                success: function (data) {
                    console.log(data)
                    updatewordcloudLocation(data)
                },
                error: function (response) {
                    console.log(response)
                }
            });

            $.ajax({
                url: '/MostUsedEntities',
                type: 'POST',
                data: JSON.stringify({
                    'chatFilter': chatFilter,
                    'sentimentFilter': sentimentFilter,
                    'timerange': timerange,
                }),
                contentType: 'application/json;charset=UTF-8',
                cache: false,
                success: function (data) {
                    updatewordcloudEntities(data)
                },
                error: function (response) {
                    console.log(response)
                }
            });

            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:5000/mostUsedWords',
                data: JSON.stringify({
                    'chatFilter': chatFilter,
                    'sentimentFilter': sentimentFilter,
                    'timerange': timerange,
                }),
                contentType: 'application/json;charset=UTF-8',
                cache: false,
                success: function (data) {
                    console.log(data)
                    addChatsToPostTable(data)
                },
                error: function (response) {
                    console.log(reponse)
                }
            });
        }


        var colorArray = ['#FF6633', '#8E1600', '#808080', '#0B6623', '#00B3E6',
            '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
            '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
            '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
            '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
            '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
            '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
            '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
            '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
            '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];

        var chart_datasets = [];
        var chart_labels = [];

      /*  $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/messagelinediagram',
            data: {},
            success: function (data) {
                updatelinediagram(data)
                //addChatsToFilter(data)
            },
            error: function (response) {
                console.log(reponse)
            }
        });*/

        function updatelinediagram(data) {
            var count = 0
            var chart_datasets = [];
            var chart_labels = [];
            var chart_data = [];
            $.each(JSON.parse(data).data, function (index, element) {
                chart_data = []
                $.each(JSON.parse(element).messages, function (index, element1) {
                    chart_data.push(JSON.parse(element1).number)
                    console.log(JSON.parse(element))
                });
                chart_datasets.push({
                    label: JSON.parse(element).chatName,
                    fill: true,
                    backgroundColor: colorArray[JSON.parse(element).chatId],
                    borderColor: colorArray[JSON.parse(element).chatId],
                    borderWidth: 2,
                    borderDash: [],
                    borderDashOffset: 0.0,
                    pointBackgroundColor: colorArray[JSON.parse(element).chatId],
                    pointBorderColor: 'rgba(255,255,255,0)',
                    pointHoverBackgroundColor: '#d346b1',
                    pointBorderWidth: 20,
                    pointHoverRadius: 4,
                    pointHoverBorderWidth: 15,
                    pointRadius: 4,
                    fill: false,
                    data: chart_data,
                })
                count++
            });
            $.each(JSON.parse(data).labels, function (index, element) {
                chart_labels.push(JSON.parse(element).date)
            });
            var data = myChartData.config.data;
            data.datasets = chart_datasets;
            data.labels = chart_labels;
            myChartData.update();
        }



        var ctx = document.getElementById("chartBig1").getContext('2d');

        var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(1, 'rgba(72,72,176,0.1)');
        gradientStroke.addColorStop(0.4, 'rgba(72,72,176,0.0)');
        gradientStroke.addColorStop(0, 'rgba(119,52,169,0)'); //purple colors



        var config = {
            type: 'line',
            data: {
                labels: chart_labels,
                datasets: chart_datasets
            },
            options: gradientChartOptionsConfigurationWithTooltipPurple
        };
        var myChartData = new Chart(ctx, config);

        $("#0").click(function () {
            timerange = 24
            filterdata()
        });

        $("#1").click(function () {
            timerange = 12
            filterdata()
        });

        $("#2").click(function () {
            timerange = 6
            filterdata()
        });

        var labelswordcloud = []
        var datasetswordcloud= []

        var ctx = document.getElementById("verbsWordCloud").getContext("2d");

        var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

        gradientStroke.addColorStop(0.7, 'rgba(248,40,29,0.4)');
        gradientStroke.addColorStop(0.5, 'rgba(248,40,29,0.2)');
        gradientStroke.addColorStop(0, 'rgba(248,40,29,0.0)'); //res colors

        var myWordCloud = new Chartc(ctx, {
            type: 'wordCloud',
            responsive: true,
            maintainAspectRatio: false,

            data: {
                labels: labelswordcloud,
                datasets: datasetswordcloud
            },
            options: {
                title: {
                    display: false,
                    text: "Most used verbs"
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                let label = context.dataset.label || '';
                                label += ((context.raw -12 ) / 2)
                                return label;
                            }
                        }
                    }
                }
            }
        });

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/MostUsedVerbs',
            data: {},
            success: function (data) {
                updatewordcloud(data)
            },
            error: function (response) {
                console.log(reponse)
            }
        });

        function updatewordcloud(data) {
            var chart_datasets = [];
            var chart_labels = [];
            var chart_data = [];


            $.each(JSON.parse(data).data, function (index, element) {
                chart_data.push(12 + (parseInt(element) * 2))
            });

            $.each(JSON.parse(data).labels, function (index, element) {
                chart_labels.push(element.replaceAll('"', ''))
            });

            if (chart_data.length < 1) {
                chart_labels = ['Verbs not found']
                chart_data = [40]
            }

            chart_datasets.push({
                label: "",
                fill: true,
                backgroundColor: gradientStroke,
                hoverBackgroundColor: gradientStroke,
                borderColor: '#f11e1f',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                data: chart_data
            })

            var data = myWordCloud.config.data;
            data.datasets = chart_datasets;
            data.labels = chart_labels;
            myWordCloud.update();
        }

        var labelswordcloudEntities = []
        var datasetswordcloudEntities = []

        var ctxEntities = document.getElementById("entitiesWordCloud").getContext("2d");

        var gradientStrokeEntities = ctxEntities.createLinearGradient(0, 230, 0, 50);

        gradientStrokeEntities.addColorStop(0.7, 'rgba(248,40,29,0.4)');
        gradientStrokeEntities.addColorStop(0.5, 'rgba(248,40,29,0.2)');
        gradientStrokeEntities.addColorStop(0, 'rgba(248,40,29,0.0)'); //res colors

        var myWordCloudEntities = new Chartc(ctxEntities, {
            type: 'wordCloud',
            responsive: true,
            maintainAspectRatio: false,

            data: {
                labels: labelswordcloudEntities,
                datasets: datasetswordcloudEntities
            },
            options: {
                title: {
                    display: false,
                    text: "Most used entities"
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                let label = context.dataset.label || '';
                                label += ((context.raw -12) / 2)
                                return label;
                            }
                        }
                    }
                }
            }
        });

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/MostUsedEntities',
            data: {},
            success: function (data) {
                updatewordcloudEntities(data)
            },
            error: function (response) {
                console.log(reponse)
            }
        });

        function updatewordcloudEntities(data) {
            var chart_datasets = [];
            var chart_labels = [];
            var chart_data = [];
            $.each(JSON.parse(data).data, function (index, element) {
                chart_data.push(12 + (parseInt(element) * 2))
            });

            $.each(JSON.parse(data).labels, function (index, element) {
                chart_labels.push(element.replaceAll('"', ''))
            });

            if (chart_data.length < 1) {
                chart_labels = ['Entities not found']
                chart_data = [40]
            }

            chart_datasets.push({
                label: "",
                fill: true,
                backgroundColor: gradientStrokeEntities,
                hoverBackgroundColor: gradientStrokeEntities,
                borderColor: '#f11e1f',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                data: chart_data
            })

            var data = myWordCloudEntities.config.data;
            data.datasets = chart_datasets;
            data.labels = chart_labels;
            myWordCloudEntities.update();
        }

        var labelswordcloudLocation = []
        var datasetswordcloudLocation = []

        var ctxLocation = document.getElementById("locationsWordCloud").getContext("2d");

        var gradientStrokeLocation = ctxLocation.createLinearGradient(0, 230, 0, 50);

        gradientStrokeLocation.addColorStop(0.7, 'rgba(248,40,29,0.4)');
        gradientStrokeLocation.addColorStop(0.5, 'rgba(248,40,29,0.2)');
        gradientStrokeLocation.addColorStop(0, 'rgba(248,40,29,0.0)'); //res colors

        var myWordCloudLocation = new Chartc(ctxLocation, {
            type: 'wordCloud',
            responsive: true,
            maintainAspectRatio: false,

            data: {
                labels: labelswordcloudLocation,
                datasets: datasetswordcloudLocation
            },
            options: {
                title: {
                    display: false,
                    text: "Most used locations"
                },
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                let label = context.dataset.label || '';
                                label += ((context.raw -12) / 2)
                                return label;
                            }
                        }
                    }
                }
            }
        });

        $.ajax({
            type: 'GET',
            url: 'http://127.0.0.1:5000/MostUsedLocations',
            data: {},
            success: function (data) {
                updatewordcloudLocation(data)
            },
            error: function (response) {
                console.log(reponse)
            }
        });

        function updatewordcloudLocation(data) {
            var chart_datasets = [];
            var chart_labels = [];
            var chart_data = [];


            $.each(JSON.parse(data).data, function (index, element) {
                chart_data.push(12 + (parseInt(element) * 2))
            });

            $.each(JSON.parse(data).labels, function (index, element) {
                chart_labels.push(element.replaceAll('"', ''))
            });

            if (chart_data.length < 1) {
                chart_labels = ['locations not found']
                chart_data = [40]
            }

            chart_datasets.push({
                label: "",
                fill: true,
                backgroundColor: gradientStrokeLocation,
                hoverBackgroundColor: gradientStrokeLocation,
                borderColor: '#f11e1f',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                data: chart_data
            })

            var data = myWordCloudLocation.config.data;
            data.datasets = chart_datasets;
            data.labels = chart_labels;
            myWordCloudLocation.update();
        }
    },


};