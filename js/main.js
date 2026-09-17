/**
 * Core JS Engine
 * Features: Theme toggle, mobile menu, live search & category filtering, and newsletter handling.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initStickyHeader();
  initLiveSearchAndFilter();
  initNewsletter();
});

/* Theme Manager */
function initTheme() {
  const toggleBtn = document.getElementById('themeToggle');
  if (!toggleBtn) return;

  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.body.classList.add('dark-theme');
  }

  toggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    const isDark = document.body.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
  });
}

/* Mobile Menu Drawer */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobileMenuBtn');
  const navLinks = document.getElementById('navLinks');
  if (!menuBtn || !navLinks) return;

  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    navLinks.classList.toggle('active');
  });

  document.addEventListener('click', (e) => {
    if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
      navLinks.classList.remove('active');
    }
  });
}

/* Sticky Header Shadow */
function initStickyHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 15) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }, { passive: true });
}

/* Real-Time Live Search & Category Chip Filter */
function initLiveSearchAndFilter() {
  const searchInput = document.getElementById('articleSearch');
  const catButtons = document.querySelectorAll('.cat-btn');
  const articleCards = document.querySelectorAll('.article-card');

  if (!articleCards.length) return;

  let currentCategory = 'all';
  let searchQuery = '';

  function filterCards() {
    articleCards.forEach(card => {
      const cardTitle = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const cardExcerpt = (card.querySelector('.card-excerpt')?.textContent || '').toLowerCase();
      const cardCategories = (card.getAttribute('data-categories') || '').toLowerCase();

      const matchesSearch = !searchQuery || cardTitle.includes(searchQuery) || cardExcerpt.includes(searchQuery);
      const matchesCategory = currentCategory === 'all' || cardCategories.includes(currentCategory.toLowerCase());

      if (matchesSearch && matchesCategory) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      filterCards();
    });
  }

  catButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      catButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-category') || 'all';
      filterCards();
    });
  });
}

/* Newsletter Feedback */
function initNewsletter() {
  const form = document.getElementById('newsletterForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const input = form.querySelector('input[type="email"]');
    if (input && input.value) {
      const btn = form.querySelector('button');
      const originalText = btn.textContent;
      btn.textContent = 'Subscribed! 🎉';
      input.value = '';
      setTimeout(() => {
        btn.textContent = originalText;
      }, 3500);
    }
  });
}

/* Contact Form Feedback */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const originalText = btn.innerHTML;
    btn.innerHTML = 'Message Sent! <i class="fa-solid fa-check"></i>';
    btn.style.background = 'hsl(142, 45%, 32%)';
    form.reset();
    setTimeout(() => {
      btn.innerHTML = originalText;
      btn.style.background = '';
    }, 4000);
  });
}

/* FAQ Accordion */
function initFAQAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    if (!question) return;
    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('active');
      faqItems.forEach(i => i.classList.remove('active'));
      if (!isOpen) {
        item.classList.add('active');
      }
    });
  });
}

/* Print Recipe Button */
function initPrintButton() {
  document.querySelectorAll('.btn-print').forEach(btn => {
    btn.addEventListener('click', () => {
      window.print();
    });
  });
}

// Attach additional listeners
document.addEventListener('DOMContentLoaded', () => {
  initContactForm();
  initFAQAccordion();
  initPrintButton();
});

