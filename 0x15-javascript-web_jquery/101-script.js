$(document).ready(function () {
  const $ul = $('UL.my_list');

  $('DIV#add_item').on('click', function () {
    $ul.append('<li>Item</li>');
  });

  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });

  $('DIV#clear_list').on('click', function () {
    $ul.empty();
  });
});
