const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.ajax({ url }).done(function (data) {
  $('DIV#character').text(data.name);
});
