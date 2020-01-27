 




// if (!checkData('user')) {
//   Nav.assign('login-register.html');
// }


$(document).ready(function () {

    $.ajax({
      type: "POST",
      url: 'http://localhost:5000/patient/fetch/profile',
      data: {
        // 'skey': getData('user').skey,
        'pid': getData('patient').pid,
      },
      success: function(data) {
        if (data) {
          console.log(data);
          var template = $('#patient_profile').html();
          var patients = data.data[0];

          var personData = {
            // 'username': patients[1],
            'fname': patients[1],
            'lname': patients[2],
            // 'email': patients[3],
            'gender':patients[3],
            'phone': patients[4],
            // 'phone': missingPerson[5],
            // 'city': patients[9],
            'dob': patients[5],
            'bgroup':patients[6],
            'medhist':patients[7],
            'roa':patients[8],
            'allergies':patients[9]

          };

          var html = Mustache.render(template, personData);
          $('.main').append(html);

        }
      },
     error: function(error) {
       console.log(error);
     },
     dataType: 'json',
    });

});


$(document).ready(function () {

    $.ajax({
      type: "POST",
      url: 'http://localhost:5000/patient/update',
      data: {
        // 'skey': getData('user').skey,
        'pid': getData('patient').pid,
      },
      success: function(data) {
        if (data) {
          console.log(data);
          var template = $('#patient_profile').html();
          var patients = data.data;

          var personData = {
            // 'username': patients[1],
            'fname': patients[1],
            'lname': patients[2],
            // 'email': patients[3],
            'gender':patients[3],
            'phone': patients[4],
            // 'phone': missingPerson[5],
            // 'city': patients[9],
            'dob': patients[5],
            'bgroup':patients[6],
            'medhist':patients[7],
            'roa':patients[8],
            'allergies':patients[9]

          };

          var html = Mustache.render(template, personData);
          $('.results').append(html);

        }
      },
     error: function(error) {
       console.log(error);
     },
     dataType: 'json',
    });

});









//
