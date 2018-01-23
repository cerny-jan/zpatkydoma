var $portfolio;
var $masonry_block;
var $portfolio_selectors;
var $portfolio_selectors_li;
var $blog;
var hashfilter;

$(document).ready(function () {

    /*==============================================================*/
    //Smooth Scroll - START CODE
    /*==============================================================*/
    jQuery('.inner-top').smoothScroll({
        speed: 900,
        offset: -68
    });

    /*==============================================================*/
    //Shrink nav on scroll - START CODE
    /*==============================================================*/

    if ($(window).scrollTop() > 10) {
        $('nav').addClass('shrink-nav');
    } else {
        $('nav').removeClass('shrink-nav');
    }

    /*==============================================================*/
    //Set Parallax - START CODE
    /*==============================================================*/
    SetParallax();
    /*==============================================================*/
    //WOW Animation  - START CODE
    /*==============================================================*/

    var wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 90,
        mobile: false,
        live: true
    });
    wow.init();
    /*==============================================================*/
    //Parallax - START CODE
    /*==============================================================*/

    var $elem = $('#content');
    $('#scroll_to_top').fadeIn('slow');
    $('#nav_down').fadeIn('slow');
    $(window).bind('scrollstart', function () {
        $('#scroll_to_top,#nav_down').stop().animate({'opacity': '0.2'});
    });
    $(window).bind('scrollstop', function () {
        $('#scroll_to_top,#nav_down').stop().animate({'opacity': '1'});
    });
    $('#nav_down').click(
            function (e) {
                $('html, body').animate({scrollTop: $elem.height()}, 800);
            }
    );
    $('#scroll_to_top').click(
            function (e) {
                $('html, body').animate({scrollTop: '0px'}, 800);
            }
    );
});

function isScrolledIntoView(elem) {
    try {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(elem).height();

        return ((elemTop <= docViewBottom) && (elemBottom >= docViewTop));
    }
    catch (ex) {
        return false;
    }


}

/*==============================================================*/
//Navigation - START CODE
/*==============================================================*/
// Shrink nav on scroll
$(window).scroll(function () {
    if ($(window).scrollTop() > 10) {
        $('nav').addClass('shrink-nav');
    } else {
        $('nav').removeClass('shrink-nav');
    }
});
/*==============================================================*/
//Parallax - START CODE
/*==============================================================*/
//

$('.parallax-fix').each(function () {
    if ($(this).children('.parallax-background-img').length) {
        var imgSrc = jQuery(this).children('.parallax-background-img').attr('src');
        jQuery(this).css('background', 'url("' + imgSrc + '")');
        jQuery(this).children('.parallax-background-img').remove();
        $(this).css('background-position', '50% 0%');
    }

});
var IsParallaxGenerated = false;
function SetParallax() {
    if ($(window).width() > 1030 && !IsParallaxGenerated) {
        $('.parallax1').parallax("50%", 0.1);
        $('.parallax2').parallax("50%", 0.2);
        $('.parallax3').parallax("50%", 0.3);
        $('.parallax4').parallax("50%", 0.4);
        $('.parallax5').parallax("50%", 0.5);
        $('.parallax6').parallax("50%", 0.6);
        $('.parallax7').parallax("50%", 0.7);
        $('.parallax8').parallax("50%", 0.8);
        $('.parallax9').parallax("50%", 0.05);
        $('.parallax10').parallax("50%", 0.02);
        $('.parallax11').parallax("50%", 0.01);
        $('.parallax12').parallax("50%", 0.099);
        IsParallaxGenerated = true;
    }
}
/*==============================================================*/
//Mobile Toggle Control - START CODE
/*==============================================================*/

$('.mobile-toggle').click(function () {
    $('nav').toggleClass('open-nav');
});
$('.dropdown-arrow').click(function () {
    if ($('.mobile-toggle').is(":visible")) {
        if ($(this).children('.dropdown').hasClass('open-nav')) {
            $(this).children('.dropdown').removeClass('open-nav');
        } else {
            $('.dropdown').removeClass('open-nav');
            $(this).children('.dropdown').addClass('open-nav');
        }
    }
});

/*==============================================================*/
//Smooth Scroll - START CODE
/*==============================================================*/
var scrollAnimationTime = 1200,
        scrollAnimation = 'easeInOutExpo';
$('a.scrollto').bind('click.smoothscroll', function (event) {
    event.preventDefault();
    var target = this.hash;
    $('html, body').stop()
            .animate({
                'scrollTop': $(target)
                        .offset()
                        .top
            }, scrollAnimationTime, scrollAnimation, function () {
                window.location.hash = target;
            });
});
// Inner links
$('.inner-link').smoothScroll({
    speed: 900,
    offset: -0
});

    $('.section-link').smoothScroll({
        speed: 900,
        offset: 1
    });
// Scroll To Down
function scrollToDown() {
    var target = $('#features');
    $('html, body').animate({scrollTop: $(target).offset().top}, 800);
}
function scrollToDownSection() {
    var target = $('#about');
    $('html, body').animate({scrollTop: $(target).offset().top}, 800);
}

/*==============================================================*/
//Window Resize Events - START CODE
/*==============================================================*/
$(window).resize(function () {
    //Position Fullwidth Subnavs fullwidth correctly
    $('.dropdown-fullwidth').each(function () {
        $(this).css('width', $('.row').width());
        var subNavOffset = -($('nav .row').innerWidth() - $('.menu').innerWidth() - 15);
        $(this).css('left', subNavOffset);
    });
    if ($(window).width() >= 992 && $('.navbar-collapse').hasClass('in')) {
        $('.navbar-collapse').removeClass('in');
        //$('.navbar-collapse').removeClass('in').find('ul.dropdown-menu').removeClass('in').parent('li.dropdown').addClass('open');
        $('.navbar-collapse ul.dropdown-menu').each(function () {
            if ($(this).hasClass('in')) {
                $(this).removeClass('in'); //.parent('li.dropdown').addClass('open');
            }
        });
        $('ul.navbar-nav > li.dropdown > a.dropdown-toggle').addClass('collapsed');
        $('.logo').focus();
        $('.navbar-collapse a.dropdown-toggle').removeClass('active');
    }

    setTimeout(function () {
        SetParallax();
    }, 1000);
});
/*==============================================================*/
//Scroll To Top - START CODE
/*==============================================================*/
$(window).scroll(function () {
    if ($(this)
            .scrollTop() > 100) {
        $('.scrollToTop')
                .fadeIn();
    } else {
        $('.scrollToTop')
                .fadeOut();
    }
});
//Click event to scroll to top
$('.scrollToTop').click(function () {
    $('html, body').animate({
        scrollTop: 0
    }, 1000);
    return false;
});
/*==============================================================*/
//Scroll To Top - END CODE
/*==============================================================*/

$('nav.full-width-pull-menu ul.panel-group li.dropdown a.dropdown-toggle').click(function () {
    if ($(this).parent('li').find('ul.dropdown-menu').length > 0)
    {
        if ($(this).parent('li').hasClass('open')) {
            $(this).parent('li').removeClass('open');
        }
        else{
            $(this).parent('li').addClass('open');
        }
    }
});
