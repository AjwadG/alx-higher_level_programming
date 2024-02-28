$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').on('click', great());
  $('INPUT#language_code').on('keypress', function (key) {
    if (key.which === 13) {
      great();
    }
  });
  function great () {
    const lang = $('INPUT#language_code').val();
    $.ajax({ url, data: { lang } }).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
