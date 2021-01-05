const enableScrollOnInternalLinksInMenu = function() {
    // #chi-sono
    $("li#comp-j6htgi841 a").click(function() {
        if (!$("#comp-j6w6mgxz").length) return
        $('html, body').animate({
            scrollTop: $("#comp-j6w6mgxz").offset().top - 40
        });
    })

    // #contatti
    $("li#comp-j6htgi846 a").click(function() {
        if (!$("#comp-j6w6mgyg").length) return
        $('html, body').animate({
            scrollTop: $("#comp-j6w6mgyg").offset().top - 60
        });
    })

    // #ambiti-intervento
    $("li#comp-j6htgi843 a").click(function() {
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
                // scrollTop: $("#comp-j6w6mgxz").offset().top - 45
                scrollTop: $("#comp-j6w6mgxz").offset().top - 40
            });
        }
    }, 500);

    // #contatti
    setTimeout(function () {
        if (window.location.href.endsWith("#contatti")) {
            $('html, body').animate({
                // scrollTop: $("#comp-j6w6mgyg").offset().top - 90
                scrollTop: $("#comp-j6w6mgyg").offset().top - 60
            });
        }
    }, 500);

    // #ambiti-intervento
    setTimeout(function () {
        if (window.location.href.endsWith("#ambiti-intervento")) {
            $('html, body').animate({
                // scrollTop: $("#comp-j6w85rn2").offset().top - 90
                scrollTop: $("#comp-j6w85rn2").offset().top - 50
            });
        }
    }, 500);
}

$(document).ready(function() {
    enableScrollOnInternalLinksInMenu()
    scrollOnPageLoadIfHashInLocation()
});