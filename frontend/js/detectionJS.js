function rand() {
  return Math.random();
}

var df = '';
var patientName = '';

$(document).ready(function() {

  $.ajax({
    type: "POST",
    url: 'http://localhost:5000/dataframe',
    data: {
      'pid': getData('patient').pid,
      'uid': getData('user').uid,
      'skey': getData('user').skey
    },
    success: function(data) {
      console.log(data);

      patientName = data.patient[0][1] + ' ' + data.patient[0][2];

      $('#nameCard').html('');
      $('#nameCard').html(`
          <h4 class="uk-card-title">Name:</h4>
          <div class="row">
            <div class="col-7" style="padding-top: 10%;">
              <h4 style="color:#3498db;"><a href="patient_profile.html">${data.patient[0][1]} ${data.patient[0][2]}</a></h4>
            </div>
            <div class="col-5">
              <div class="uk-inline uk-light">
                <img class="rounded-circle" src="${data.patient[0][11]}" alt="">
              </div>
            </div>
          </div>
        `);

      df = {
        'actual': JSON.parse(data.data.actual),
        'critical': JSON.parse(data.data.critical),
        'predictions': JSON.parse(data.data.predictions)
      };

      console.log(df);
      var mult = 0.033333;
      t = new Date();

      var layout = {
          shapes: [
              {
                  type: 'rect',
                  xref: 'x',
                  yref: 'paper',
                  x0: t,
                  y0: 0,
                  x1: addMinutes(t, mult),
                  y1: 1,
                  fillcolor: '#d3d3d3',
                  opacity: 0.2,
                  line: {
                      width: 0
                  }
              },
          ],
      };

      $('#graphHR').html('');
      $('#graphTP').html('');
      $('#graphRR').html('');

      Plotly.plot('graphHR', [{
          x: [subtractMinutes(t, mult*6), subtractMinutes(t, mult*5), subtractMinutes(t, mult*4), subtractMinutes(t, mult*3),
              subtractMinutes(t, mult*2), subtractMinutes(t, mult)],
          y: Object.values(df.actual.heartrate).map(Number).slice(1),
          name: 'Actual',
          type: 'scatter'
        }, {
          x: [],
          y: [],
          name: 'Prediction',
          type: 'scatter'
      }]);

      Plotly.plot('graphTP', [{
          x: [subtractMinutes(t, mult*6), subtractMinutes(t, mult*5), subtractMinutes(t, mult*4), subtractMinutes(t, mult*3),
              subtractMinutes(t, mult*2), subtractMinutes(t, mult)],
          y: Object.values(df.actual.temperature).map(Number).slice(1),
          name: 'Actual',
          type: 'scatter'
        }, {
          x: [],
          y: [],
          name: 'Prediction',
          type: 'scatter'
      }]);

      Plotly.plot('graphRR', [{
          x: [subtractMinutes(t, mult*6), subtractMinutes(t, mult*5), subtractMinutes(t, mult*4), subtractMinutes(t, mult*3),
              subtractMinutes(t, mult*2), subtractMinutes(t, mult)],
          y: Object.values(df.actual.respiration).map(Number).slice(1),
          name: 'Actual',
          type: 'scatter'
        }, {
          x: [],
          y: [],
          name: 'Prediction',
          type: 'scatter'
      }]);

        // var xstart = Object.keys(df.actual.heartrate).map(Number).slice(1)[5];
        var cnt = 0;

        var interval = setInterval(function() {

          time = new Date();
          var olderTime = subtractMinutes(time, 1);
          var futureTime = addMinutes(time, 1);

          var minuteView = {
                'xaxis': {
                  type: 'date',
                  range: [olderTime,futureTime]
                },
                'shapes': []
              };

          Plotly.relayout('graphHR', minuteView);
          Plotly.relayout('graphTP', minuteView);
          Plotly.relayout('graphRR', minuteView);

           minuteView = {
                'xaxis': {
                  type: 'date',
                  range: [olderTime,futureTime]
                },
                'shapes[0]': {
                    type: 'rect',
                    // x-reference is assigned to the x-values
                    xref: 'x',
                    // y-reference is assigned to the plot paper [0,1]
                    yref: 'paper',
                    x0: subtractMinutes(time, 100),
                    y0: 0,
                    x1: time,
                    y1: 1,
                    fillcolor: '#7a7a7a',
                    opacity: 0.3,
                    line: {
                        width: 0
                  }
                },
              };

          Plotly.relayout('graphHR', minuteView);
          Plotly.relayout('graphTP', minuteView);
          Plotly.relayout('graphRR', minuteView);

          $('#hrVal').html(Math.round((Object.values(df.predictions.heartrate).map(Number)[cnt + 7] + Number.EPSILON) * 100) / 100);
          $('#rrVal').html(Math.round((Object.values(df.predictions.respiration).map(Number)[cnt + 7] + Number.EPSILON) * 100) / 100);
          $('#tpVal').html(Math.round((Object.values(df.predictions.temperature).map(Number)[cnt + 7] + Number.EPSILON) * 100) / 100);

          Plotly.extendTraces('graphHR', {
            x: [[time], [addMinutes(time, mult*6)]],
            y: [[Object.values(df.predictions.heartrate).map(Number)[cnt + 7]], [Object.values(df.predictions.heartrate).map(Number)[cnt + 13]]]
          }, [0, 1], 10);

          Plotly.extendTraces('graphTP', {
            x: [[time], [addMinutes(time, mult*6)]],
            y: [[Object.values(df.predictions.temperature).map(Number)[cnt + 7]], [Object.values(df.predictions.temperature).map(Number)[cnt + 13]]]
          }, [0, 1], 10);

          Plotly.extendTraces('graphRR', {
            x: [[time], [addMinutes(time, mult*6)]],
            y: [[Object.values(df.predictions.respiration).map(Number)[cnt + 7]], [Object.values(df.predictions.respiration).map(Number)[cnt + 13]]]
          }, [0, 1], 10);


          cnt++;
          if(cnt === 34) clearInterval(interval);
        }, 1*10*1000);

    },
    error: function(error) {
      console.log(error);
    },
    dataType: 'json',
  });
});


function addMinutes(date, minutes) {
    return new Date(date.getTime() + minutes*60000);
}

function subtractMinutes(date, minutes) {
    return new Date(date.getTime() - minutes*60000);
}

$('#downloadPDF').click(function () {
  // var doc = new jsPDF();
  // var source = window.document.getElementsByTagName("body")[0];
  // doc.fromHTML(
  //     source,
  //     15,
  //     15,
  //     function(dispose) {
  //       // dispose: object with X, Y of the last line add to the PDF
  //       //          this allow the insertion of new lines after html
  //       // pdf.save('Test.pdf');
  //
  //       if (navigator.msSaveBlob) {
  //           var string = doc.output('datauristring');
  //       } else {
  //           var string = doc.output('bloburi');
  //       }
  //
  //       $('.previewIFRAME').attr('src', string);
  //   }
  //   );

  // var pdf = new jsPDF('p','pt','a4');


  // html2canvas($('body')[0]).then(function (canvas){
  //           // onrendered: function(canvas) {
  //           var pdf = new jsPDF("l", "mm", "a4");
  //           // var imgData = canvas.toDataURL('image/jpeg', 1.0);
  //           // pdf.addImage(imgData, 'JPEG', 10, 10, 180, 150);  // 180x150 mm @ (10,10)mm
  //           pdf.addHTML(document.body);
  //             pdf.output('datauri');
  //             pdf.save('a4.pdf');
  //           // due to lack of documentation; try setting w/h based on unit
  //           // pdf.output("dataurlnewwindow");
  //           // pdf.save('a4.pdf');
  //
  //         // }
  //       });
  html2canvas(document.body).then(function(canvas) {
      // document.body.appendChild(canvas);
      var date = new Date();
      var filename = 'Analysis for ' + patientName + ' on ' + date.toGMTString() + '.png';
      saveAs(canvas.toDataURL(), filename);
  });

// doc.save('a4.pdf');
//   doc.output("dataurlnewwindow");
});

function saveAs(uri, filename) {

    var link = document.createElement('a');

    if (typeof link.download === 'string') {

        link.href = uri;
        link.download = filename;

        //Firefox requires the link to be in the body
        document.body.appendChild(link);

        //simulate click
        link.click();

        //remove the link when done
        document.body.removeChild(link);

    } else {

        window.open(uri);

    }
}

//
