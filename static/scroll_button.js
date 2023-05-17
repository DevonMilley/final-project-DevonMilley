// Show or hide the button based on scroll position
window.addEventListener("scroll", function() {
    scrollFunction();
  });
  
  function scrollFunction() {
    var scrollToTopBtn = document.getElementById("scrollToTopBtn");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      scrollToTopBtn.style.display = "block";
    } else {
      scrollToTopBtn.style.display = "none";
    }
  }
  
  // Scroll to the top of the page when the button is clicked
  function topFunction() {
    document.documentElement.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  
    document.body.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  }
          
    
  