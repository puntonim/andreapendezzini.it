const enableScrollOnInternalLinksInMenu = function() {
    $("li#comp-khi91e6o2 a").click(function() {
        if (!$("#chi-sono").length) return
        $('html, body').animate({
            scrollTop: $("#chi-sono").offset().top - 60
        });
    })

    $("li#comp-j6htgi846 a").click(function() {
        if (!$("#contatti").length) return
        $('html, body').animate({
            scrollTop: $("#contatti").offset().top - 60
        });
    })

    $("li#comp-j6htgi843 a").click(function() {
        if (!$("#ambiti-intervento").length) return
        $('html, body').animate({
            scrollTop: $("#ambiti-intervento").offset().top - 50
        });
    })
}

$(document).ready(function() {
    enableScrollOnInternalLinksInMenu()
});