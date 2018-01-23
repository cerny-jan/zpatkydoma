/*==============================================================
    pull menu
 ==============================================================*/

function bindEvent(e,n,t){e.addEventListener?e.addEventListener(n,t,!1):e.attachEvent&&e.attachEvent("on"+n,t)}!function(){function e(){d&&bindEvent(d,"click",n),l&&bindEvent(l,"click",n)}function n(){o?(classie.remove(t,"show-menu"),$(".full-width-pull-menu").length&&classie.remove(t,"overflow-hidden")):(classie.add(t,"show-menu"),$(".full-width-pull-menu").length&&classie.add(t,"overflow-hidden")),o=!o}var t=document.body,d=document.getElementById("open-button"),l=document.getElementById("close-button"),o=!1;e()}();
