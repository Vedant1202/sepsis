
// if (checkData('user')) {
//   $('#login').addClass('hidden');
// } else {
//   $('#signout').addClass('hidden');
// }
//
// deleteData('laptopDetails');
// deleteData('compare');
//

$(document).ready(function () {
  // if (checkData('user')) {
  //   fetchCart(getData('user')[1].uid, true);
  // }

  // setTimeout(function () {
  // $('#pdirectory').html('<div class="uk-spinner"></div>');

      $.ajax({
        type: "POST",
        url: 'http://localhost:5000/patient/my/fetch',
        data: {
          'uid': getData('user').uid,
          'skey': getData('user').skey
        },
        success: function(data) {
          // console.log(JSON.parse(data[0]));
          console.log(data.data[0]);
          $('#pdirectory').html('');
          for (var i = 0; i < data.data.length; i++) {
            var patient = data.data[i];
            $('#pdirectory').append(

              `
                <div class="row" style="cursor: pointer;" onclick="setData('patient', JSON.stringify({'pid': ${patient[0]}})); Nav.assign('patient_profile.html');">
                  <div class="col-4">
                    <img src="" class="laptops" style="width: 70%;">
                  </div>
                  <div class="col-4" >
                    <strong>${patient[1]} ${patient[2]}</strong>
                    <ul>
                      <li style="padding-bottom:10px;">${patient[3]}</li>
                      <li style="padding-bottom:10px;">${patient[5]}</li>
                      <li style="padding-bottom:10px;">${patient[4]}</li>
                    </ul>
                  </div>
                  <div class="col-2">


                    <ul>

                      <li style="padding-bottom:10px;padding-top:40px;">${patient[6]}</li>
                      <li style="padding-bottom:10px;">${patient[9]}</li>

                    </ul>

                  </div>

                </div>
              <hr>
              `
            );
          }
        }
      });
});


function searchPatient(elem) {
  console.log($('#missingKey').val().trim());
  $('#pdirectory').html(`
    <div class="container" align="center" style="padding-top: 10%; padding-bottom: 10%;">
      <div uk-spinner="ratio: 5"></div>
    </div>
    `);
  $.ajax({
    type: "POST",
    url: 'http://localhost:5000/patient/my/search',
    data: {
      'keyword': $('#missingKey').val().trim(),
      'uid': getData('user').uid,
      'skey': getData('user').skey
    },
    success: function(data) {
      // console.log(JSON.parse(data[0]));
      console.log(data.data[0]);
      $('#pdirectory').html('');
      for (var i = 0; i < data.data.length; i++) {
        var patient = data.data[i];
        $('#pdirectory').append(

          `
            <div class="row" style="cursor: pointer;" onclick="setData('pdirectory', JSON.stringify({'pid': ${patient[0]}})); Nav.assign('patient_profile.html');">
              <div class="col-4">
                <img src="" class="laptops" style="width: 70%;">
              </div>
              <div class="col-4" >
                <strong>${patient[1]} ${patient[2]}</strong>
                <ul>
                  <li style="padding-bottom:10px;">${patient[3]}</li>
                  <li style="padding-bottom:10px;">${patient[5]}</li>
                  <li style="padding-bottom:10px;">${patient[4]}</li>
                </ul>
              </div>
              <div class="col-2">


                <ul>

                  <li style="padding-bottom:10px;padding-top:40px;">${patient[6]}</li>
                  <li style="padding-bottom:10px;">${patient[9]}</li>

                </ul>

              </div>

            </div>
          <hr>
          `
        );
      }
    }
  });

}



//
