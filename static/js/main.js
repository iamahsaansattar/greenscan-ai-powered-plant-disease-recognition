document.addEventListener("DOMContentLoaded", () => {

    /* ===================== NAVBAR HEIGHT ===================== */
    const navbar = document.querySelector(".glassy-navbar");
    if (navbar) {
        document.documentElement.style.setProperty(
            "--navbar-height",
            `${navbar.offsetHeight}px`
        );
    }

    /* ===================== CHARACTER COUNTERS ===================== */
    const homeCommentField = document.getElementById("homeCommentField");
    const homeCharCount = document.getElementById("charCount");

    if (homeCommentField && homeCharCount) {
        homeCommentField.addEventListener("input", () => {
            homeCharCount.textContent = homeCommentField.value.length;
        });
    }

    const commentField = document.getElementById("commentField");
    const contactCharCount = document.getElementById("charCount");

    if (commentField && contactCharCount) {
        commentField.addEventListener("input", () => {
            contactCharCount.textContent = commentField.value.length;
        });
    }

});
