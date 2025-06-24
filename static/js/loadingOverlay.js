// Show the loading overlay
function showLoadingOverlay(message = "Submitting your order...") {
  const overlay = document.getElementById("loadingOverlay");
  const textElement = overlay?.querySelector(".loading-text");

  if (overlay) {
    if (textElement) textElement.textContent = message;
    overlay.classList.remove("d-none");
  }
}

// Hide the loading overlay
function hideLoadingOverlay() {
  const overlay = document.getElementById("loadingOverlay");
  if (overlay) overlay.classList.add("d-none");
}
