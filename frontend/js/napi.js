

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
            for (var i=2; i< 6; i++) {
                $('#newsDiv').append(`

                    <div class="uk-card uk-card-default uk-width-1-2@m">
                        <div class="uk-card-header">
                            <div class="uk-grid-small uk-flex-middle" uk-grid>
                                <div class="uk-width-auto">
                                    <img class="uk-border-circle" width="40" height="40" src="${data.articles[i]['urlToImage']}">
                                </div>
                                <div class="uk-width-expand">
                                    <h3 class="uk-card-title uk-margin-remove-bottom">${data.articles[i]['title']}</h3>
                                    <p class="uk-text-meta uk-margin-remove-top"><time datetime="2016-04-01T19:00">${data.articles[i]['publishedAt']}</time></p>
                                </div>
                            </div>
                        </div>
                        <div class="uk-card-body">
                            <p>${data.articles[i]['description']}</p>
                        </div>
                        <div class="uk-card-footer">
                            <a href="${data.articles[i]['url']}" class="uk-button uk-button-text">Read more</a>
                        </div>
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
