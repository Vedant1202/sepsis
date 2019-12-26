
if (!checkData('user')) {
  Nav.assign('home.html');
}


$('#next').click(function () {

  var fname = $('#fname').val().trim(),
      lname = $('#lname').val().trim(),
      alias = $('#alias').val().trim(),
      gender = $('#gender').val().trim(),
      age = $('#age').val().trim(),
      address = $('#address').val().trim(),
      city = $('#city').val().trim(),
      nationality = $('#nationality').val().trim(),
      lang = $('#lang').val().trim(),
      height = $('#height').val().trim(),
      weight = $('#weight').val().trim(),
      identifications = $('#identifications').val().trim(),
      eye_color = $('#eye_color').val().trim(),
      skin_color = $('#skin_color').val().trim(),
      hair_color = $('#hair_color').val().trim(),
      conditions = $('#conditions').val().trim(),
      medications = $('#medications').val().trim(),
      prescribed_by = $('#prescribed_by').val().trim(),
      med_hist = $('#med_hist').val().trim(),
      other_med = $('#other_med').val().trim(),
      fam_phone = $('#fam_phone').val().trim(),
      pol_phone = $('#pol_phone').val().trim(),
      pol_address = $('#pol_address').val().trim();




    if (fname && pol_phone && pol_address) {

      var fd = new FormData();
      fd.append('skey', getData('user').skey);
      fd.append('uid', getData('user').uid);
      fd.append('fname', fname);
      fd.append('lname', lname);
      fd.append('alias', alias);
      fd.append('gender', gender);
      fd.append('age', age);
      fd.append('address', address);
      fd.append('city', city);
      fd.append('nationality', nationality);
      fd.append('languages_known', lang);
      fd.append('height', height);
      fd.append('weight', weight);
      fd.append('identifications', identifications);
      fd.append('eye_color', eye_color);
      fd.append('skin_color', skin_color);
      fd.append('hair_color', hair_color);
      fd.append('conditions', conditions);
      fd.append('medications', medications);
      fd.append('prescribed_by', prescribed_by);
      fd.append('med_hist', med_hist);
      fd.append('other_med', other_med);
      fd.append('fam_phone', fam_phone);
      fd.append('pol_phone', pol_phone);
      fd.append('pol_address', pol_address);
      // print()
      fd.append('profImg', document.getElementById('profImgUpload').files[0]);


      $.ajax({
        type: "POST",
        url: url + 'missing/add',
        data: fd,
        success: function(data) {
          if (data.valid) {
            setData('newMissingMID', JSON.stringify({'mid': data.data[0]}));
            console.log(data);
            Nav.assign('first_report.html');
          }
        },
       error: function(error) {
         console.log(error);
       },
       dataType: 'json',
       processData: false,
       contentType: false
      });

    } else {
      alert('Please fill in the required fields');
    }


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
