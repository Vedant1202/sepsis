
if (!checkData('user')) {
  if (!checkData('newMissingMID')) {
    Nav.assign('home.html');
  }
}



$('#submit').click(function () {

  var loc = $('#loc').val().trim(),
      time = $('#time').val().trim(),
      info = $('#info').val().trim();


  if (loc && time && info) {

    $.ajax({
      type: "POST",
      url: url + 'report/add',
      data: {
        'skey': getData('user').skey,
        'uid': getData('user').uid,
        'time': time,
        'loc': loc,
        'info': info,
        'mid': getData('newMissingMID').mid,
      },
      success: function(data) {
        alert('Report added succesfully');
        deleteData('newMissingMID');
        Nav.assign('home.html');
      },
      error: function(error) {
        console.log(error);
      },
      dataType: 'json'
    });

  } else {
    alert('Please fill in the required fields');
  }
});















//
