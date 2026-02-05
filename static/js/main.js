// Smooth scroll for Home page navigation
// Only runs on the Home page

document.addEventListener('DOMContentLoaded', function() {
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
