$(document).ready(function () {

    $.ajax({
      type: "POST",
      url: 'http://localhost:5000/user/update',
      data: {
        // 'skey': getData('user').skey,
        'uid': getData('user').uid,
      },
      success: function(data) {
        if (data) {
          console.log(data);
          var template = $('#doctor_profile').html();
          var users = data.data;

          var personData = {
            // 'username': patients[1],
            'fname': users[1],
            'lname': users[2],
            'dept' : users[3],
            'email': users[4],
            // 'password' : users[5],
            'type': users[5],
            'gender':users[6],
            'dob' : users[7],
            'phone': users[8],
            // 'phone': missingPerson[5],
            // 'city': patients[9],
            // 'dob': patients[],
            'specialization':users[9],
            'experience':users[10],
            'registration':users[11]
// _fname, _lname , _dept, _dob, _gender, _phone , _type , _specialization, _experience , _registration,
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
