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
    $("a#menu-link-chi-sono").click(function() {
        if (!$("#chi-sono").length) return
        $('html, body').animate({
            scrollTop: $("#chi-sono").offset().top - 60
        });
    })

    $("a#menu-link-contatti").click(function() {
        if (!$("#contatti").length) return
        $('html, body').animate({
            scrollTop: $("#contatti").offset().top - 60
        });
    })

    $("a#menu-link-ambiti-intervento").click(function() {
        if (!$("#ambiti-intervento").length) return
        $('html, body').animate({
            scrollTop: $("#ambiti-intervento").offset().top - 50
        });
    })
}

$(document).ready(function() {
    showMobileMenuOnSandwichClick()
    hideMobileMenuOnLinkClick()
    enableScrollOnInternalLinksInMenu()
});