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


$( document ).ready(function() {
    showMobileMenuOnSandwichClick()
    hideMobileMenuOnLinkClick()
});