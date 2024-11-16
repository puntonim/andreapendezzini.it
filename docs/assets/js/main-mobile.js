const toggleMobileMenu = function() {
    $("header#SITE_HEADER_WRAPPER").toggle(0)
    $("header#SITE_HEADER_WRAPPER-mobile").toggle(0)
    $("div.mobile-menu-container").toggleClass("active")
}

const showMobileMenuOnSandwichClick = function() {
    $("nav#TINY_MENU > button").click(function() {
        toggleMobileMenu()
    })
}

const hideMobileMenuOnLinkClick = function() {
    $("header#SITE_HEADER_WRAPPER-mobile li").click(function() {
        toggleMobileMenu()
    })
}

const enableScrollOnInternalLinksInMenu = function() {
    // #chi-sono
    $("a#menu-link-chi-sono").click(function() {
        if (!$("#comp-khi93rum").length) return
        $('html, body').animate({
            scrollTop: $("#comp-khi93rum").offset().top
        });
    })

    // #contatti
    $("a#menu-link-contatti").click(function() {
        if (!$("#comp-j6w6mgyg").length) return
        $('html, body').animate({
            scrollTop: $("#comp-j6w6mgyg").offset().top - 50
        });
    })

    // #ambiti-intervento
    $("a#menu-link-ambiti-intervento").click(function() {
        if (!$("#comp-j6w85rn2").length) return
        $('html, body').animate({
            scrollTop: $("#comp-j6w85rn2").offset().top - 50
        });
    })
}

const scrollOnPageLoadIfHashInLocation = function() {
    // #chi-sono
    setTimeout(function () {
        if (window.location.href.endsWith("#chi-sono")) {
            $('html, body').animate({
                scrollTop: $("#comp-khi93rum").offset().top
            });
        }
    }, 500);

    // #contatti
    setTimeout(function () {
        if (window.location.href.endsWith("#contatti")) {
            $('html, body').animate({
                scrollTop: $("#comp-j6w6mgyg").offset().top - 50
            });
        }
    }, 500);

    // #ambiti-intervento
    setTimeout(function () {
        if (window.location.href.endsWith("#ambiti-intervento")) {
            $('html, body').animate({
                scrollTop: $("#comp-j6w85rn2").offset().top - 50
            });
        }
    }, 500);
}

const fixHeight = function() {
    $('section#comp-j6w6mgxz').parent().css("min-height", "auto");
}

const showCopyrightYear = () => {
  const year = new Date().getFullYear();
  const spans = document.querySelectorAll(".copyright-year-nim");
  spans.forEach((i) => {
    i.innerHTML = year;
  });
};

$(document).ready(function() {
    showMobileMenuOnSandwichClick();
    hideMobileMenuOnLinkClick();
    enableScrollOnInternalLinksInMenu();
    scrollOnPageLoadIfHashInLocation();
    fixHeight();
    showCopyrightYear();
});