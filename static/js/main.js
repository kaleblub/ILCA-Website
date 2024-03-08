(function ($) {
    "use strict";

    // Spinner
    // var spinner = function () {
    //     setTimeout(function () {
    //         $('#spinner').removeClass('show');
    //     }, 1);
    // };
    // spinner();

    // Initiate the wowjs (if used)
    // new WOW().init();

    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.sticky-top').css('top', '0px');
        } else {
            $('.sticky-top').css('top', '-100px');
        }
    });

    // Copy email or phone to clipboard
    function copyTextToClipboard(selector) {
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($(selector).text()).select();
        document.execCommand("copy", false, null);
        $temp.remove();
    }

    $('#copyEmail').click(function () {
        copyTextToClipboard('.email-link');
        alert('Email copied to clipboard');
    });

    $('#copyPhone').click(function () {
        copyTextToClipboard('.phone-link');
        alert('Phone number copied to clipboard');
    });

    // Dropdown on mouse hover
    $(window).on("load resize", function () {
        if (window.matchMedia("(min-width: 992px)").matches) {
            $('.dropdown').hover(
                function () {
                    const $this = $(this);
                    $this.addClass('show');
                    $this.find('.dropdown-toggle').attr("aria-expanded", "true");
                    $this.find('.dropdown-menu').addClass('show');
                },
                function () {
                    const $this = $(this);
                    $this.removeClass('show');
                    $this.find('.dropdown-toggle').attr("aria-expanded", "false");
                    $this.find('.dropdown-menu').removeClass('show');
                }
            );
        } else {
            $('.dropdown').off("mouseenter mouseleave");
        }
    });

    // Hamburger Menu
    $(document).ready(function () {
        // Function to toggle mobile menu visibility
        function toggleMobileMenu() {
            var $siteMenu = $('.site-mobile-menu');
            if ($siteMenu.hasClass('open')) {
                $siteMenu.removeClass('open');
            } else {
                $siteMenu.addClass('open');
            }
        }
    
        // Click event listener for the hamburger icon
        $('.site-menu-toggle').click(function () {
            console.log('clicked');
            toggleMobileMenu();
        });
    
        // Close mobile menu when clicking outside of it
        $(document).on('click', function (e) {
            var $siteMenu = $('.site-mobile-menu');
            if (!$siteMenu.is(e.target) && $siteMenu.has(e.target).length === 0) {
                $siteMenu.removeClass('open');
            }
        });
    });
    
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });
    

    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        console.log('clicked');
        $('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
        console.log('clicked');
        return false;
    });

    // Testimonials carousel (if used)
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        center: true,
        margin: 24,
        dots: true,
        loop: true,
        nav: false,
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            }
        }
    });

    
})(jQuery);