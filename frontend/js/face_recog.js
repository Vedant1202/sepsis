//



if (checkData('user')) {
  $('#logInBtn').addClass('uk-hidden');
} else {
  Nav.assign('home.html');
  $('#profileBtn').addClass('uk-hidden');
  $('#watchingMenu').addClass('uk-hidden');
  $('#faceRecogMenu').addClass('uk-hidden');
  $('#logout').addClass('uk-hidden');
}


$('#logInBtn').click(function () {
  Nav.assign('login-register.html');
});


$('#submit').click(function functionName() {

  fd = new FormData();
  fd.append('profImg', document.getElementById('profImgUpload').files[0]);

  $('#resCont').html('<div class="col-12" align="center"><span uk-spinner="ratio: 5"></span></div>');

  $.ajax({
    type: "POST",
    url: url + 'face_recog',
    data: fd,
    success: function(data) {

      if (data) {

        // var template =
        console.log(data);
        var template = $('#results').html();
        $('#resCont').html('');
        for (var i = 0; i < data.matched.length; i++) {
          var missingPerson = data.matched[i];

          var personData = {
            'mid': missingPerson[0],
            'profImg': missingPerson[2],
            'fname': missingPerson[3],
            'lname': missingPerson[4],
          };


          var html = Mustache.render(template, personData);
          $('#resCont').append(html);

      }
    } else {
        $('#resCont').html('Some error... Please refresh');
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



function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imgDisplay')
                .attr('src', e.target.result);
                // .width(150)
                // .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}














//
