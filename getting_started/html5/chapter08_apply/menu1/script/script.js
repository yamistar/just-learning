// JavaScript Document
jQuery(document).ready (function () {
    $('.nav>li')
      .mouseover (function () {
        $(this).find('.submenu').stop().slideDown (500);
      })
      .mouseout (function () {
        $ (this).find('.submenu').stop().slideUp (500);
      });
  });
  