// Smooth scroll for Home page navigation
// Only runs on the Home page

document.addEventListener('DOMContentLoaded', function() {
      // Sticky Social Bar minimize logic
      const socialBarToggle = document.getElementById('social-bar-toggle');
      const socialBarLinks = document.getElementById('social-bar-links');
      const socialBarArrow = document.getElementById('social-bar-arrow');
      let socialBarMinimized = false;
      if (socialBarToggle && socialBarLinks && socialBarArrow) {
        socialBarToggle.addEventListener('click', function() {
          socialBarMinimized = !socialBarMinimized;
          if (socialBarMinimized) {
            socialBarLinks.classList.add('hidden');
            socialBarArrow.classList.remove('fa-chevron-right');
            socialBarArrow.classList.add('fa-chevron-left');
            socialBarToggle.title = 'Show Social Bar';
          } else {
            socialBarLinks.classList.remove('hidden');
            socialBarArrow.classList.remove('fa-chevron-left');
            socialBarArrow.classList.add('fa-chevron-right');
            socialBarToggle.title = 'Minimize Social Bar';
          }
        });
      }
    // Carousel Banner logic
    const carouselImages = [
      document.getElementById('carousel-img-0'),
      document.getElementById('carousel-img-1')
    ];
    let currentIndex = 0;
    function showCarouselImage(idx) {
      carouselImages.forEach((img, i) => {
        if (img) img.classList.toggle('hidden', i !== idx);
      });
    }
    function nextCarousel() {
      currentIndex = (currentIndex + 1) % carouselImages.length;
      showCarouselImage(currentIndex);
    }
    function prevCarousel() {
      currentIndex = (currentIndex - 1 + carouselImages.length) % carouselImages.length;
      showCarouselImage(currentIndex);
    }
    // Arrow button listeners
    const prevBtn = document.getElementById('carousel-prev');
    const nextBtn = document.getElementById('carousel-next');
    if (prevBtn && nextBtn) {
      prevBtn.addEventListener('click', prevCarousel);
      nextBtn.addEventListener('click', nextCarousel);
    }
    // Auto-slide every 15 seconds
    setInterval(nextCarousel, 15000);
    showCarouselImage(currentIndex);
  function isHomePage() {
    return window.location.pathname === '/' || window.location.pathname === '/home';
  }

  // For all links with data-scroll
  document.querySelectorAll('a[data-scroll]').forEach(function(link) {
    const sectionId = link.getAttribute('data-scroll');
    link.addEventListener('click', function(e) {
      if (isHomePage()) {
        // Only scroll if section exists
        const section = document.getElementById(sectionId);
        if (section) {
          e.preventDefault();
          section.scrollIntoView({ behavior: 'smooth' });
        }
      } else {
        // If not on home, go to home with hash
        if (sectionId) {
          link.setAttribute('href', '/#' + sectionId);
        }
        // Let default navigation happen
      }
    });
  });

  // If loaded with a hash, scroll to section (for /#section links)
  if (isHomePage() && window.location.hash) {
    const id = window.location.hash.replace('#', '');
    const section = document.getElementById(id);
    if (section) {
      setTimeout(function() {
        section.scrollIntoView({ behavior: 'smooth' });
      }, 200);
    }
  }
});
