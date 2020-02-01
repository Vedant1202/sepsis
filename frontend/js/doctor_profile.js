




// if (!checkData('user')) {
//   Nav.assign('login-register.html');
// }


$(document).ready(function () {

    $.ajax({
      type: "POST",
      url: url + 'user/fetch',
      data: {
        'skey': getData('user').skey,
        'uid': getData('user').uid,
      },
      success: function(data) {
        if (data) {
          console.log(data);
          var template = $('#profile').html();
          var missingPerson = data.data;
          console.log(missingPerson);

          var personData = {
            'fname': missingPerson[1],
            'lname': missingPerson[2],
            'specialization': missingPerson[3],
            'email': missingPerson[4],
            'experience': missingPerson[10],
            'registration': missingPerson[12],

            'email': missingPerson[4],
            'phone': missingPerson[9],
            'filename': missingPerson[13],
            // 'city': missingPerson[9],
            'dob': missingPerson[8]
          };

          var html = Mustache.render(template, personData);
          $('.main').html('');
          $('.main').append(html);

        }
      },
     error: function(error) {
       console.log(error);
     },
     dataType: 'json',
    });

});










//
