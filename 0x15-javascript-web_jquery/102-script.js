$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';

  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();

    $.ajax({ url, data: { lang } }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
