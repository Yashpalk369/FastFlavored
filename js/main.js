/**
 * Core JS Engine
 * Features: Theme toggle, mobile menu, live search & category filtering, and newsletter handling.
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initMobileMenu();
  initStickyHeader();
  initDailyHeroRecipe();
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

  const closeMenu = () => {
    navLinks.classList.remove('active');
    menuBtn.classList.remove('active');
    menuBtn.setAttribute('aria-expanded', 'false');
  };

  menuBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isExpanded = navLinks.classList.toggle('active');
    menuBtn.classList.toggle('active', isExpanded);
    menuBtn.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
  });

  document.addEventListener('click', (e) => {
    if (!menuBtn.contains(e.target) && !navLinks.contains(e.target)) {
      closeMenu();
    }
  });

  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', closeMenu);
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

/* 24-Hour Daily Rotating Hero Recipe Engine */
function initDailyHeroRecipe() {
  const heroSection = document.getElementById('heroSection');
  const heroTitle = document.getElementById('heroTitle');
  const heroDescription = document.getElementById('heroDescription');
  const heroTag = document.getElementById('heroTag');
  const heroPrimaryBtn = document.getElementById('heroPrimaryBtn');
  const heroImage = document.getElementById('heroImage');

  if (!heroSection || !heroTitle || !heroPrimaryBtn || !heroImage) return;

  // Extract all recipe cards (filtering out non-recipe guides)
  const cards = Array.from(document.querySelectorAll('#articleGrid .article-card'));
  const recipes = cards.map(card => {
    const link = card.querySelector('.card-title a');
    const badge = card.querySelector('.card-badge');
    const excerpt = card.querySelector('.card-excerpt');
    const img = card.querySelector('.card-image-wrap img');
    const isGuide = card.querySelector('.read-link')?.textContent.toLowerCase().includes('guide');

    return {
      title: link ? link.textContent.trim() : '',
      url: link ? link.getAttribute('href') : '',
      badge: badge ? badge.textContent.trim() : 'Fast Dinners',
      excerpt: excerpt ? excerpt.textContent.trim() : '',
      image: img ? img.getAttribute('src') : '',
      imageAlt: img ? img.getAttribute('alt') : '',
      isGuide: Boolean(isGuide)
    };
  }).filter(r => r.title && r.url && !r.isGuide);

  if (!recipes.length) return;

  // Calculate days elapsed in UTC so the hero recipe rotates exactly every 24 hours at midnight
  const now = new Date();
  const dayNumber = Math.floor(Date.UTC(now.getFullYear(), now.getMonth(), now.getDate()) / 86400000);
  const totalCount = recipes.length;
  const cycleIndex = ((dayNumber % totalCount) + totalCount) % totalCount;
  const cycleNumber = Math.floor(dayNumber / totalCount);

  // Deterministic Fisher-Yates shuffle seeded per cycle:
  // Guarantees all recipes are featured once per cycle with ZERO back-to-back repeats!
  let seed = Math.abs(((cycleNumber + 1) * 9301 + 49297) % 233280);
  function prng() {
    seed = (seed * 9301 + 49297) % 233280;
    return seed / 233280;
  }

  const order = Array.from({ length: totalCount }, (_, i) => i);
  for (let i = order.length - 1; i > 0; i--) {
    const j = Math.floor(prng() * (i + 1));
    [order[i], order[j]] = [order[j], order[i]];
  }

  const dailyRecipe = recipes[order[cycleIndex]];
  if (!dailyRecipe) return;

  // Smoothly update Hero Section
  heroTitle.textContent = dailyRecipe.title;
  if (heroDescription && dailyRecipe.excerpt) {
    heroDescription.textContent = dailyRecipe.excerpt;
  }
  if (heroTag) {
    heroTag.innerHTML = `<i class="fa-solid fa-sparkles"></i> Recipe of the Day &bull; ${dailyRecipe.badge}`;
  }
  heroPrimaryBtn.setAttribute('href', dailyRecipe.url);
  heroPrimaryBtn.innerHTML = `Cook Tonight's Recipe <i class="fa-solid fa-arrow-right"></i>`;
  heroImage.setAttribute('src', dailyRecipe.image);
  heroImage.setAttribute('alt', dailyRecipe.imageAlt || dailyRecipe.title);
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

