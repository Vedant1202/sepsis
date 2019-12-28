//


if (checkData('user')) {
  $('#logInBtn').addClass('uk-hidden');
} else {
  $('#profileBtn').addClass('uk-hidden');
  $('#watchingMenu').addClass('uk-hidden');
  $('#faceRecogMenu').addClass('uk-hidden');
  $('#logout').addClass('uk-hidden');
}

$('#logInBtn').click(function () {
  Nav.assign('login-register.html');
});

$(document).ready(function () {

  if (checkData('user')) {
    fetch_reg(0);
  } else {
    fetch_unreg(0);
  }

});




$('#searchMissing').click(function () {
  var keyword = $('#missingKey').val().trim();
  if (keyword) {
    $('#card-container').html('');

    if (checkData('user')) {
      fetch_query_reg(keyword, 0);
    } else {
      fetch_query_unreg(keyword, 0);
    }
  }

});


function details(elem) {
  var mid = parseInt(elem.id.split('-')[1]);
  setData('missing-mid-details', JSON.stringify({'mid': mid}));
  Nav.assign('missing_profile.html');
}


function fetch_reg(start) {
  $.ajax({
    type: "POST",
    url: url + 'missing/fetch/reg',
    data: {
      'skey': getData('user').skey,
      'uid': getData('user').uid,
      'start': start
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-card-reg').html();
        for (var i = 0; i < data.data.length; i++) {
          var missingPerson = data.data[i];

          var personData = {
            'mid': missingPerson[0],
            'fname': missingPerson[1],
            'lname': missingPerson[2],
            'age': missingPerson[16],
            'gender': missingPerson[17],
            'address': missingPerson[14],
            'city': missingPerson[15],
            'profImg': missingPerson[26]
          };

          var html = Mustache.render(template, personData);
          $('#card-container').append(html);

        }
      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



function fetch_unreg(start) {
  $.ajax({
    type: "POST",
    url: url + 'missing/fetch/unreg',
    data: {
      'start': start
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-card-unreg').html();
        for (var i = 0; i < data.data.length; i++) {
          var missingPerson = data.data[i];

          var personData = {
            'mid': missingPerson[0],
            'fname': missingPerson[1],
            'lname': missingPerson[2],
            'age': missingPerson[11],
            'gender': missingPerson[12],
            'city': missingPerson[10],
            'profImg': missingPerson[13]
          };

          var html = Mustache.render(template, personData);
          $('#card-container').append(html);

        }
      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



function fetch_query_reg(keyword, start) {
  $.ajax({
    type: "POST",
    url: url + 'missing/search/reg',
    data: {
      'skey': getData('user').skey,
      'uid': getData('user').uid,
      'start': start,
      'keyword': $('#missingKey').val().trim()
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-card-reg').html();
        for (var i = 0; i < data.data.length; i++) {
          var missingPerson = data.data[i];

          var personData = {
            'mid': missingPerson[0],
            'fname': missingPerson[1],
            'lname': missingPerson[2],
            'age': missingPerson[16],
            'gender': missingPerson[17],
            'address': missingPerson[14],
            'city': missingPerson[15],
            'profImg': missingPerson[26]
          };

          var html = Mustache.render(template, personData);
          $('#card-container').append(html);

        }
      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



function fetch_query_unreg(keyword, start) {
  $.ajax({
    type: "POST",
    url: url + 'missing/search/unreg',
    data: {
      'start': start,
      'keyword': $('#missingKey').val().trim()
    },
    success: function(data) {
      if (data) {
        console.log(data);
        var template = $('#missing-card-unreg').html();
        for (var i = 0; i < data.data.length; i++) {
          var missingPerson = data.data[i];

          var personData = {
            'mid': missingPerson[0],
            'fname': missingPerson[1],
            'lname': missingPerson[2],
            'age': missingPerson[11],
            'gender': missingPerson[12],
            'city': missingPerson[10]
          };

          var html = Mustache.render(template, personData);
          $('#card-container').append(html);

        }
      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}












//
