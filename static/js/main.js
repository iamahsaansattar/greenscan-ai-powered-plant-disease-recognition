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
    const commentField = document.getElementById("commentField");
    const charCount = document.getElementById("charCount");

    if (commentField && charCount) {
        commentField.addEventListener("input", () => {
            charCount.textContent = commentField.value.length;
        });
    }

    /* ===================== CONTACT FORM UX (HOME + CONTACT) ===================== */
    if (
        document.body.classList.contains("contact-page") ||
        document.body.classList.contains("home-page")
    ) {

        const contactForm = document.querySelector('form[action*="contact"]');
        const submitBtn = document.getElementById("contactSubmitBtn");

        /* Disable submit button after click to prevent duplicates */
        if (contactForm && submitBtn) {
            contactForm.addEventListener("submit", () => {
                submitBtn.disabled = true;
                submitBtn.style.pointerEvents = "none";
            });
        }

    }

});
