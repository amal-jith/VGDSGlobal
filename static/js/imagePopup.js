
  document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");
    const closeBtn = document.querySelector(".close-btn-svg");

    document.querySelectorAll(".image-popup").forEach(imgDiv => {
      imgDiv.addEventListener("click", function () {
        const imageUrl = this.getAttribute("data-image");
        modalImg.src = imageUrl;
        modal.classList.remove("d-none");
      });
    });

    closeBtn.onclick = function () {
      modal.classList.add("d-none");
    };

    modal.onclick = function (e) {
      if (e.target === modal) {
        modal.classList.add("d-none");
      }
    };
  });

