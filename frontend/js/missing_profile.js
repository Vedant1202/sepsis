

if (checkData('missing-mid-details')) {
  if (checkData('user')) {
    fetch_missing_profile_reg();
  } else {
    fetch_missing_profile_unreg();
  }
} else {
  Nav.assign('home.html');
}





function fetch_missing_profile_reg() {
  $.ajax({
    type: "POST",
    url: url + 'missing/fetch/profile/reg',
    data: {
      'skey': getData('user').skey,
      'uid': getData('user').uid,
      'mid': getData('missing-mid-details').mid
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-profile-reg').html();
        var missingPerson = data.data;

        var personData = {
          'mid': missingPerson[0],
          'fname': missingPerson[1],
          'lname': missingPerson[2],
          'uid': missingPerson[3],
          'medications': missingPerson[4],
          'prescribed_by': missingPerson[5],
          'conditions': missingPerson[6],
          'height': missingPerson[7],
          'weight': missingPerson[8],
          'identifications': missingPerson[9],
          'eye_color': missingPerson[10],
          'skin_color': missingPerson[11],
          'hair_color': missingPerson[12],
          'date_created':  moment.unix(missingPerson[13]).format("MM/DD/YYYY"),
          'address': missingPerson[14],
          'city': missingPerson[15],
          'age': missingPerson[16],
          'gender': missingPerson[17],
          'alias': missingPerson[18],
          'nationality': missingPerson[19],
          'languages_known': missingPerson[20],
          'med_hist': missingPerson[21],
          'other_med': missingPerson[22],
          'fam_phone': missingPerson[23],
          'pol_phone': missingPerson[24],
          'pol_address': missingPerson[25],
          'profImg': missingPerson[26]
        };

        var html = Mustache.render(template, personData);
        $('.main').append(html);

      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



function fetch_missing_profile_reg_report() {
  $.ajax({
    type: "POST",
    url: url + 'missing/report/fetch',
    data: {
      'skey': getData('user').skey,
      'uid': getData('user').uid,
      'mid': getData('missing-mid-details').mid
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-profile-reg').html();
        var missingPerson = data.data;

        var personData = {
          'mid': missingPerson[0],
          'fname': missingPerson[1],
          'lname': missingPerson[2],
          'uid': missingPerson[3],
          'medications': missingPerson[4],
          'prescribed_by': missingPerson[5],
          'conditions': missingPerson[6],
          'height': missingPerson[7],
          'weight': missingPerson[8],
          'identifications': missingPerson[9],
          'eye_color': missingPerson[10],
          'skin_color': missingPerson[11],
          'hair_color': missingPerson[12],
          'date_created':  moment.unix(missingPerson[13]).format("MM/DD/YYYY"),
          'address': missingPerson[14],
          'city': missingPerson[15],
          'age': missingPerson[16],
          'gender': missingPerson[17],
          'alias': missingPerson[18],
          'nationality': missingPerson[19],
          'languages_known': missingPerson[20],
          'med_hist': missingPerson[21],
          'other_med': missingPerson[22],
          'fam_phone': missingPerson[23],
          'pol_phone': missingPerson[24],
          'pol_address': missingPerson[25],
          'profImg': missingPerson[26]
          
        };

        var html = Mustache.render(template, personData);
        $('.main').append(html);

      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}





function fetch_missing_profile_unreg() {
  $.ajax({
    type: "POST",
    url: url + 'missing/fetch/profile/unreg',
    data: {
      'mid': getData('missing-mid-details').mid
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-profile-unreg').html();
        var missingPerson = data.data;

        var personData = {
          'mid': missingPerson[0],
          'fname': missingPerson[1],
          'lname': missingPerson[2],
          'uid': missingPerson[3],
          'medications': missingPerson[4],
          'conditions': missingPerson[5],
          'height': missingPerson[6],
          'weight': missingPerson[7],
          'identifications': missingPerson[8],
          'eye_color': missingPerson[9],
          'skin_color': missingPerson[10],
          'hair_color': missingPerson[11],
          'date_created': missingPerson[12],
          'city': missingPerson[13],
          'age': missingPerson[14],
          'gender': missingPerson[15],
        };

        var html = Mustache.render(template, personData);
        $('.main').append(html);

      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



















//
