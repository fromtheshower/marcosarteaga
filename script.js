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
  const language = form.querySelector('input[name="locale"]')?.value || "en";
  const messages = {
    en: {
      platformRequired: "Choose at least one platform.",
      notConnected: "This form isn’t connected yet. Your enquiry was not sent.",
      sending: "Sending…",
      sendFailed: "Your enquiry wasn’t sent. Please try again later.",
    },
    fr: {
      platformRequired: "Choisissez au moins une plateforme.",
      notConnected: "Ce formulaire n’est pas encore connecté. Votre demande n’a pas été envoyée.",
      sending: "Envoi en cours…",
      sendFailed: "Votre demande n’a pas été envoyée. Réessayez plus tard.",
    },
    es: {
      platformRequired: "Selecciona al menos una plataforma.",
      notConnected: "El formulario aún no está conectado. Tu consulta no se ha enviado.",
      sending: "Enviando…",
      sendFailed: "Tu consulta no se ha enviado. Vuelve a intentarlo más tarde.",
    },
  }[language] || {
    platformRequired: "Choose at least one platform.",
    notConnected: "This form isn’t connected yet. Your enquiry was not sent.",
    sending: "Sending…",
    sendFailed: "Your enquiry wasn’t sent. Please try again later.",
  };

  spend.addEventListener("change", () => {
    spendNote.hidden = spend.value !== "under-5k";
  });

  const updatePlatforms = () => {
    const selected = platformChecks.some((check) => check.checked);
    platformChecks[0].setCustomValidity(selected ? "" : messages.platformRequired);
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
      status.textContent = messages.notConnected;
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
    button.textContent = messages.sending;
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
      status.textContent = messages.sendFailed;
      status.dataset.state = "error";
    } finally {
      window.clearTimeout(timeout);
      button.disabled = false;
      button.innerHTML = buttonMarkup;
    }
  });
})();
