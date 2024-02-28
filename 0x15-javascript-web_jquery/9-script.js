const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.ajax({ url }).done(function (data) {
    $('DIV#hello').text(data.hello);
  });
});
