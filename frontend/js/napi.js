

$(document).ready(function () {
    var url = 'https://newsapi.org/v2/everything?' +
    'q=Sepsis&' +
    'sortBy=popularity&' +
    'language=en&' +
    'apiKey=3ac7f3bd3e4042f98b5bfcfc30dde1e7';

    // var req = new Request(url);

    $.ajax({
        type: "GET",
        url: url,
        success: function(data) {
            console.log(data);
            for (var i=2; i< 4; i++) {
                $('#newsDiv').append(`
                  <div class="row">
                    <div class=" col-5 uk-card uk-card-default uk-card-hover uk-width-1-2@m" style="margin-left: 8%;" >
                        <div class="uk-card-header" style="height:481px;">
                            <div class="uk-grid-small uk-flex-middle">
                                <div class="uk-width-auto">
                                    <img class="uk-border-circle" style="width:90%;height:300px;" src="${data.articles[i]['urlToImage']}">
                                </div>
                                <br>
                                <div class="uk-width-expand">
                                    <h3 class="uk-card-title uk-margin-remove-bottom">${data.articles[i]['title']}</h3>
                                    <p class="uk-text-meta uk-margin-remove-top"><time datetime="2016-04-01T19:00">${data.articles[i]['publishedAt']}</time></p>
                                </div>
                            </div>
                        </div>
                        <div class="uk-card-body" style="width:453px; height:205px;">
                            <p>${data.articles[i]['description']}</p>
                        </div>
                        <div class="uk-card-footer">
                            <a href="${data.articles[i]['url']}" class="uk-button uk-button-text" >Read more</a>
                        </div>

                      </div>
                      <div class=" col-5 uk-card uk-card-default uk-card-hover uk-width-1-2@m" style="margin-left: 5%;" >
                          <div class="uk-card-header" style="height:481px;">
                              <div class="uk-grid-small uk-flex-middle">
                                  <div class="uk-width-auto">
                                      <img class="uk-border-circle" style="width:90%;height:300px;" src="${data.articles[i+2]['urlToImage']}">
                                  </div>
                                  <br>
                                  <div class="uk-width-expand">
                                      <h3 class="uk-card-title uk-margin-remove-bottom">${data.articles[i+2]['title']}</h3>
                                      <p class="uk-text-meta uk-margin-remove-top"><time datetime="2016-04-01T19:00">${data.articles[i+2]['publishedAt']}</time></p>
                                  </div>
                              </div>
                          </div>
                          <div class="uk-card-body" style="width:453px; height:205px;">
                              <p>${data.articles[i+2]['description']}</p>
                          </div>
                          <div class="uk-card-footer">
                              <a href="${data.articles[i+2]['url']}" class="uk-button uk-button-text" >Read more</a>
                          </div>

                        </div>
                        <hr style="margin-top:5%;">
                    </div>





                `);
              }

        },
        error: function(error) {
            console.log(error);
        },
        dataType: 'json',
    });

});
