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

    /* ===================== CONTACT PAGE UX ===================== */
    if (document.body.classList.contains("contact-page")) {

        const contactForm = document.querySelector('form[action*="contact"]');
        const submitBtn = document.getElementById("contactSubmitBtn");
        const successAlert = document.querySelector(".contact-glass-card .alert-success");

        /* Disable submit button after click to prevent duplicates */
        if (contactForm && submitBtn) {
            contactForm.addEventListener("submit", () => {
                submitBtn.disabled = true;
                submitBtn.style.pointerEvents = "none";
            });
        }

        /* Auto-dismiss success message after 4 seconds */
        if (successAlert) {
            setTimeout(() => {
                successAlert.style.opacity = "1";

                requestAnimationFrame(() => {
                    successAlert.style.transition = "opacity 0.5s ease";
                    successAlert.style.opacity = "0";
                });

                setTimeout(() => {
                    successAlert.remove();
                }, 500);

            }, 4000);
        }
    }

});
