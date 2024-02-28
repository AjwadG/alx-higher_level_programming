const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.ajax({ url }).done(function (data) {
  $('DIV#hello').text(data.hello);
});
