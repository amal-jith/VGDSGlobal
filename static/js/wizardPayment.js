document.addEventListener("DOMContentLoaded", () => {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

  const fullNameInput = document.querySelector("#paymentFullName");
  const emailInput = document.querySelector("#paymentEmail");
  const phoneInput = document.querySelector("#paymentPhone");

  const promoInput = document.querySelector(".promo-input");
  const promoApplyBtn = document.querySelector(".promo-apply-btn");

  const agreeTerms = document.querySelector("#agreeTermsCheckbox");
  const marketingConsent = document.querySelector("#marketingConsentCheckbox");

  const submitOrderBtn = document.querySelector(".submit-my-btn");
  const successOverlay = document.querySelector("#orderSuccess");

  const prevBtn = document.querySelector("#step-payment .previous-btn");

  const presentationWizard = JSON.parse(localStorage.getItem("presentationWizard")) || {};

  // ✅ Show estimated price
  function updateEstimatedPriceFinalStep() {
      const estimatedPriceElem = document.querySelector("#estimatedPrice");
      const wizardData = JSON.parse(localStorage.getItem("presentationWizard")) || {};
      const price = wizardData?.delivery?.estimatedText;

      if (estimatedPriceElem) {
        estimatedPriceElem.textContent = price ? price : "$0"; // or "N/A" if you prefer
      }
    }

// Call once on load
updateEstimatedPriceFinalStep();

  // ✅ Previous button functionality
  prevBtn?.addEventListener("click", () => {
    document.querySelector("#step-payment").classList.add("d-none");
    document.querySelector("#step-files-details").classList.remove("d-none");
  });

  // ✅ Promo code apply logic
  promoApplyBtn.addEventListener("click", () => {
    const code = promoInput.value.trim();
    if (code) {
      if (!presentationWizard.payment) presentationWizard.payment = {};
      presentationWizard.payment.promoCode = code;
      localStorage.setItem("presentationWizard", JSON.stringify(presentationWizard));
      promoInput.classList.add("is-valid");
    } else {
      promoInput.classList.remove("is-valid");
    }
  });

  submitOrderBtn.addEventListener("click", (e) => {
  e.preventDefault();

  const fullName = fullNameInput.value.trim();
  const email = emailInput.value.trim();
  const phone = phoneInput.value.trim();
  const agreed = agreeTerms.checked;

  if (!fullName || !email || !phone || !agreed) {
    alert("Please fill all required fields and accept the terms.");
    return;
  }

  // ✅ Build latest payment data
  const paymentData = {
    fullName,
    email,
    phone,
    promoCode: promoInput.value.trim(),
    agreedToTerms: agreed,
    receiveMarketingEmails: marketingConsent.checked
  };

  // ✅ Update localStorage with latest payment info
  const presentationWizard = JSON.parse(localStorage.getItem("presentationWizard")) || {};
  presentationWizard.payment = paymentData;
  localStorage.setItem("presentationWizard", JSON.stringify(presentationWizard));

  // ✅ Re-fetch latest from localStorage (most reliable way)
  const latestData = JSON.parse(localStorage.getItem("presentationWizard"));
  console.log("🟢 Submitting Application Data:", latestData); // Optional debug log

  const formData = new FormData();
  formData.append("application", JSON.stringify(latestData));

  if (window.presentationWizardStyleFile) {
    formData.append("style_file", window.presentationWizardStyleFile);
  }

  if (window.presentationWizardPresentationFile) {
    formData.append("presentation_file", window.presentationWizardPresentationFile);
  }

  if (
    latestData.filesDetails &&
    latestData.filesDetails.instructions
  ) {
    formData.append("google_link", latestData.filesDetails.instructions);
  }

  showLoadingOverlay(); // Show while waiting


  fetch("/submit_order/", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken
    },
    body: formData
  })
    .then(response => {
      if (!response.ok) throw new Error("Submission failed");
      return response.json();
    })
    .then(data => {
        hideLoadingOverlay(); // ✅ HIDE loading screen after success!
        successOverlay.classList.remove("d-none");
        // localStorage.removeItem("presentationWizard"); // Optional cleanup
      })
    .catch(error => {
      hideLoadingOverlay();
      console.error("🔴 Error during form submission:", error);
      alert("There was an error submitting your order. Please try again.");
    });
});

});
