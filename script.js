(() => {
  const form = document.querySelector("#booking-form");
  const status = document.querySelector("#form-status");
  const success = document.querySelector("#booking-success");
  const button = form.querySelector('button[type="submit"]');
  const buttonMarkup = button.innerHTML;
  const spend = document.querySelector("#spend");
  const spendNote = document.querySelector("#spend-note");
  const platformChecks = [...form.querySelectorAll('input[name="platforms"]')];
  const otherCheck = document.querySelector("#platform-other");
  const otherField = document.querySelector("#other-platform-field");
  const otherInput = document.querySelector("#other-platform");
  const mobileBooking = document.querySelector("#mobile-booking");
  const hero = document.querySelector(".hero");
  const booking = document.querySelector("#booking");

  spend.addEventListener("change", () => {
    spendNote.hidden = spend.value !== "under-5k";
  });

  const updatePlatforms = () => {
    const selected = platformChecks.some((check) => check.checked);
    platformChecks[0].setCustomValidity(selected ? "" : "Choose at least one platform.");
    otherField.hidden = !otherCheck.checked;
    otherInput.required = otherCheck.checked;
    if (!otherCheck.checked) otherInput.value = "";
  };
  platformChecks.forEach((check) => check.addEventListener("change", updatePlatforms));
  updatePlatforms();

  if ("IntersectionObserver" in window) {
    let heroVisible = true;
    let bookingVisible = false;
    const updateMobileBooking = () => {
      mobileBooking.hidden = heroVisible || bookingVisible;
    };
    const observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.target === hero) heroVisible = entry.isIntersecting;
        if (entry.target === booking) bookingVisible = entry.isIntersecting;
      }
      updateMobileBooking();
    }, { threshold: 0.05 });
    observer.observe(hero);
    observer.observe(booking);
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    status.textContent = "";
    status.dataset.state = "";

    updatePlatforms();
    if (!form.reportValidity()) return;

    const endpoint = window.siteConfig?.bookingEndpoint?.trim();
    if (!endpoint) {
      status.textContent = "This form isn’t connected yet. Your enquiry was not sent.";
      status.dataset.state = "error";
      return;
    }

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    if (data.companyFax) return;
    delete data.companyFax;
    data.platforms = formData.getAll("platforms");
    if (!data.otherPlatform) delete data.otherPlatform;

    button.disabled = true;
    button.textContent = "Sending…";
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 30000);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(data),
        signal: controller.signal,
      });
      if (!response.ok) throw new Error(`Submission failed: ${response.status}`);
      form.reset();
      spendNote.hidden = true;
      updatePlatforms();
      form.hidden = true;
      success.hidden = false;
      success.focus();
    } catch {
      status.textContent = "Your enquiry wasn’t sent. Please try again later.";
      status.dataset.state = "error";
    } finally {
      window.clearTimeout(timeout);
      button.disabled = false;
      button.innerHTML = buttonMarkup;
    }
  });
})();
