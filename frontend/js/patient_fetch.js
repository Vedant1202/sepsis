




// if (!checkData('user')) {
//   Nav.assign('login-register.html');
// }


$(document).ready(function () {

  // alert('Gello')
    $.ajax({
      type: "POST",
      url: 'http://localhost:5000/patient/fetch/profile',
      data: {
        // 'skey': getData('user').skey,
        'pid': getData('patient').pid,
        'skey': getData('user').skey,
        'uid': getData('user').uid
      },
      success: function(data) {
        if (data) {
          console.log(data);
          $('.patient_profile').html('');

          var template = $('#patient_profile').html();
          var patients = data.data[0];

          var personData = {
            // 'username': patients[1],
            'fname': patients[1],
            'lname': patients[2],
            // 'email': patients[3],
            'gender':patients[3],
            'dob': patients[4],
            'phone': patients[5],
            // 'phone': missingPerson[5],
            // 'city': patients[9],
            'bgroup':patients[6],
            'medhist':patients[7],
            'roa':patients[8],
            'allergies':patients[9],
            'filename': patients[11]
          };

          var html = Mustache.render(template, personData);
          $('.patient_profile').append(html);

          var reportTemplate = $('#report-template').html();

          $('#reportsTable').html('');
          for (var i = 0; i < data.data.length; i++) {
            var reports = data.data[i];

            var reportData = {
              'title': reports[14],
              'date': reports[15],
              'reportURL': reports[18]
            };

            var reportHtml = Mustache.render(reportTemplate, reportData);
            $('#reportsTable').append(reportHtml);
          }

        }
      },
     error: function(error) {
       console.log(error);
     },
     dataType: 'json',
    });

  });



  $('#uploadReport').click(function () {

    var date = new Date();
    var title = $('#title').val().trim();

    var fd = new FormData();
    fd.append('title', title);
    fd.append('date', String(date).slice(4, 15));
    fd.append('profImg', document.getElementById('reportFile').files[0]);
    fd.append('pid', getData('patient').pid);
    fd.append('skey', getData('user').skey);
    fd.append('uid', getData('user').uid);

    $('#uploadReport').html(`
        <div uk-spinner="ratio: 1"></div>
      `);


    // alert('Gello')
      $.ajax({
        type: "POST",
        url: 'http://localhost:5000/patient/report/add',
        data: fd,
        success: function(data) {
          if (data) {
            alert('Done upload');
            window.location.reload();
          }
        },
       error: function(error) {
         console.log(error);
       },
       dataType: 'json',
       processData: false,
       contentType: false
      });

    });







//
