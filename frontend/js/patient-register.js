
// $('#loginBtn').click(function () {
//   // alert('submit')
//
//   var username = $('#username-login').val().trim();
//   var password = $('#password-login').val();
//
//   var formData = {
//     'username': username,
//     'password': password
//   };
//
//
//   $.ajax({
//     type: "POST",
//     url: 'http://localhost:5000/login',
//     data: formData,
//     success: function(data) {
//       if (!data.valid) {
//         alert('The username or password entered is incorrect');
//       } else {
//         setData('user', JSON.stringify(data));
//         Nav.assign('home.html');
//       }
//     },
//    error: function(error) {
//      console.log(error);
//    },
//    dataType: 'json'
//   });
//
// });

// $('#username').focusout(function () {
//
//   var uname = $(this).val();
//
//   data = {
//     'username': uname
//   };
//
//   $.ajax({
//     type: "POST",
//     url: 'http://localhost:5000/user/check',
//     data: data,
//     success: function(data) {
//       if (!data.valid) {
//         // Username is already taken
//         $('#username').addClass('err');
//         $('#takenuser').addClass('showelem');
//         $('#registerBtn').prop("disabled", true);
//       } else {
//         $('#username').removeClass('err');
//         $('#takenuser').removeClass('showelem');
//       }
//     },
//    error: function(error) {
//      console.log(error);
//    },
//    dataType: 'json'
//   });
//
// });



//
// $('#password-confirm').keyup(function () {
//   var val = $(this).val();
//   var pass = $('#password').val();
//
//   if (val == pass) {
//     $('#matchpass').removeClass('showelem');
//     $('#registerBtn').prop("disabled", false);
//   } else {
//     $('#matchpass').addClass('showelem');
//     $('#registerBtn').prop("disabled", true);
//   }
//
// });

$('#phone').keyup(function () {
  var val = $(this).val().trim();

  if (val.length == 10) {
    $('#phonevalid').removeClass('showelem');
    $('#registerBtn').prop("disabled", false);
  } else {
    $('#phonevalid').addClass('showelem');
    $('#registerBtn').prop("disabled", true);
  }

});

//
//


$('#submitBtn').click(function () {
  // alert('submit')

    var fname = $('#fname').val().trim(),
        lname = $('#lname').val(),
        gender = $('#gender').val().trim(),
        // fname = $('#fname').val().trim(),
        // lname = $('#lname').val().trim(),
        phone = $('#phone').val().trim(),
        dob = $('#dob').val().trim(),
        bgroup = $('#bgroup').val().trim(),
        medhist = $('#medhist').val().trim(),
        roa = $('#roa').val().trim(),
        allergies = $('#allergies').val().trim();
        // address = $('#address').val().trim();


      if ( fname && lname && gender && phone && dob && bgroup && medhist && roa && allergies) {

          // var formData = {
          //   // 'username': username,
          //   // 'password': password,
          //   // 'email': email,
          //   'fname': fname,
          //   'lname': lname,
          //   'gender':gender,
          //   'phone': phone,
          //   'dob': dob,
          //   'bgroup':bgroup,
          //   'medhist': medhist,
          //   'roa':roa,
          //   'allergies':allergies,
          // };

          var fdt = new FormData();
          fdt.append('fname', fname);
          fdt.append('lname', lname);
          fdt.append('gender', gender);
          fdt.append('phone', phone);
          fdt.append('dob', dob);
          fdt.append('bgroup', bgroup);
          fdt.append('medhist', medhist);
          fdt.append('roa', roa);
          fdt.append('allergies', allergies);
          fdt.append('profImg', document.getElementById('profImgUpload').files[0]);
          fdt.append('uid', getData('user').uid);
          fdt.append('skey', getData('user').skey);


          // console.log(formData);

          $.ajax({
            type: "POST",
            url: 'http://localhost:5000/patient/add',
            data: fdt,
            success: function(data) {
              setData('user', JSON.stringify(data));
              Nav.assign('mypatients.html');
            },
           error: function(error) {
             console.log(error);
           },
           dataType: 'json',
           processData: false,
           contentType: false
          });

    } else {

      alert('Please check if all the fields are filled');

    }

});




//
// $('#email').keyup(function() {
//   var value = $(this).val().trim();
//   var re = /\S+@\S+\.\S+/;
//   console.log(value);
//   // console.log(value);
//   if (!re.test(value)) {
//     $('#emailvalid').addClass('showelem');
//     $('#registerBtn').prop("disabled", true);
//   } else {
//     $('#emailvalid').removeClass('showelem');
//     $('#registerBtn').prop("disabled", false);
//   }
// });










//
