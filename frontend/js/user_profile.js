




if (!checkData('user')) {
  Nav.assign('login-register.html');
}


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

          var personData = {
            'username': missingPerson[1],
            'fname': missingPerson[2],
            'lname': missingPerson[3],
            'email': missingPerson[4],
            'phone': missingPerson[5],
            // 'phone': missingPerson[5],
            'city': missingPerson[9],
            'dob': missingPerson[12]
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
