
  $(document).ready(function() {
    $('#testimonial-carousel').owlCarousel({
      loop: true,
      margin: 24,
      nav: false,
      dots: true,
      autoplay: true,
      autoplayTimeout: 4000,
      responsive: {
        0: { items: 1 },
        768: { items: 2 },
        1024: { items: 3 }
      }
    });
  });

