
var url = "http://127.0.0.1:5000/";


//Navigation functions

var Nav = /** @class */ (function() {
    function Nav() {}
    Nav.assign = function(url) {
        window.location.assign(url);
    };
    Nav.replace = function(url) {
        window.location.replace(url);
    };
    Nav.back = function () {
      window.history.back();
    };
    Nav.open = function(url) {
        window.open(url, '_blank', 'location=no');
    };
    Nav.close = function() {
        window.close();
    };
    return Nav;
}());


//Cache storage Functions

function setData(cname, cvalue) {
    window.localStorage.setItem(cname, JSON.stringify(cvalue));
}

function getData(cname) {
    return JSON.parse(JSON.parse(window.localStorage.getItem(cname)));
}

function checkData(cname) {
    var user = getData(cname);
    if (user != null) {
        return true;
    } else {
        return false;
    }
}

function deleteData(cname) {
    window.localStorage.removeItem(cname);
}

// Function to check syntax of email. Returns true if
// email has atleast one '@' and  atleast one '.' followed by some string.

function checkEmail(email) { // Pass in elements as jQuery selectors
  var re = /\S+@\S+\.\S+/;

  if (re.test(email)) {
    return true;
  } else {
    return false;
  }
}


function logout() {
  $.ajax({
    type: "POST",
    url: url + 'logout',
    data: {
      'skey': getData('user').skey,
      'uid': getData('user').uid,
    },
    success: function(data) {
      if (data) {
        deleteData('user');
        Nav.assign('home.html');
      }
    },
   error: function(error) {
     console.log(error);
   },
   dataType: 'json'
  });
}



//
