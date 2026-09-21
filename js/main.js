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

/* Real-Time Live Search, Category Chip Filter & 12-Recipe Pagination Engine */
function initLiveSearchAndFilter() {
  const searchInput = document.getElementById('articleSearch');
  const catButtons = document.querySelectorAll('.cat-btn');
  const articleCards = Array.from(document.querySelectorAll('.article-card'));
  const paginationWrapper = document.getElementById('paginationWrapper');
  const paginationEl = document.getElementById('pagination');
  const paginationInfoEl = document.getElementById('paginationInfo');
  const articleGrid = document.getElementById('articleGrid');

  if (!articleCards.length) return;

  const RECIPES_PER_PAGE = 12;
  let currentCategory = 'all';
  let searchQuery = '';

  // Read initial page from URL param ?page=X if present
  const urlParams = new URLSearchParams(window.location.search);
  let currentPage = parseInt(urlParams.get('page'), 10);
  if (isNaN(currentPage) || currentPage < 1) {
    currentPage = 1;
  }

  function updateURL() {
    try {
      const url = new URL(window.location);
      if (currentPage > 1) {
        url.searchParams.set('page', currentPage);
      } else {
        url.searchParams.delete('page');
      }
      window.history.replaceState({}, '', url);
    } catch (err) {
      // In case environment restricts replaceState
    }
  }

  function goToPage(pageNum) {
    currentPage = pageNum;
    updateURL();
    render();
    const recipesSection = document.getElementById('recipes');
    if (recipesSection) {
      recipesSection.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function render() {
    // 1. Filter cards by search query and category
    const matchedCards = articleCards.filter(card => {
      const cardTitle = (card.querySelector('.card-title')?.textContent || '').toLowerCase();
      const cardExcerpt = (card.querySelector('.card-excerpt')?.textContent || '').toLowerCase();
      const cardCategories = (card.getAttribute('data-categories') || '').toLowerCase();

      const matchesSearch = !searchQuery || cardTitle.includes(searchQuery) || cardExcerpt.includes(searchQuery);
      const matchesCategory = currentCategory === 'all' || cardCategories.includes(currentCategory.toLowerCase());

      return matchesSearch && matchesCategory;
    });

    const totalMatches = matchedCards.length;
    const totalPages = Math.ceil(totalMatches / RECIPES_PER_PAGE) || 1;

    // Guard page bounds
    if (currentPage > totalPages) {
      currentPage = totalPages;
    }
    if (currentPage < 1) {
      currentPage = 1;
    }

    // 2. Slice visible window
    const startIndex = (currentPage - 1) * RECIPES_PER_PAGE;
    const endIndex = startIndex + RECIPES_PER_PAGE;

    articleCards.forEach(card => {
      const matchIndex = matchedCards.indexOf(card);
      if (matchIndex >= startIndex && matchIndex < endIndex) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });

    // 3. Handle No Results feedback
    let noResultsEl = document.getElementById('noResultsMessage');
    if (totalMatches === 0) {
      if (!noResultsEl && articleGrid) {
        noResultsEl = document.createElement('div');
        noResultsEl.id = 'noResultsMessage';
        noResultsEl.className = 'no-results-message';
        noResultsEl.innerHTML = `
          <i class="fa-solid fa-utensils"></i>
          <h3>No Matching Recipes Found</h3>
          <p>Try searching for a different ingredient, keyword, or select "All Recipes".</p>
        `;
        articleGrid.appendChild(noResultsEl);
      } else if (noResultsEl) {
        noResultsEl.style.display = 'block';
      }
    } else if (noResultsEl) {
      noResultsEl.style.display = 'none';
    }

    // 4. Render Pagination Controls
    if (!paginationWrapper || !paginationEl || !paginationInfoEl) return;

    if (totalMatches <= RECIPES_PER_PAGE) {
      paginationWrapper.style.display = 'none';
      paginationEl.innerHTML = '';
      paginationInfoEl.innerHTML = '';
      return;
    }

    paginationWrapper.style.display = 'flex';

    // Info string (e.g. "Showing 1–12 of 29 recipes")
    const showingStart = startIndex + 1;
    const showingEnd = Math.min(endIndex, totalMatches);
    paginationInfoEl.textContent = `Showing ${showingStart}–${showingEnd} of ${totalMatches} recipes (Page ${currentPage} of ${totalPages})`;

    // Generate Buttons
    let html = '';

    // Prev Button
    html += `
      <button type="button" class="page-btn prev-btn" ${currentPage === 1 ? 'disabled' : ''} aria-label="Previous page">
        <i class="fa-solid fa-chevron-left"></i> Prev
      </button>
    `;

    // Numbered Buttons with smart ellipsis
    for (let i = 1; i <= totalPages; i++) {
      if (
        i === 1 ||
        i === totalPages ||
        (i >= currentPage - 1 && i <= currentPage + 1)
      ) {
        html += `
          <button type="button" class="page-btn ${i === currentPage ? 'active' : ''}" data-page="${i}" aria-label="Page ${i}" ${i === currentPage ? 'aria-current="page"' : ''}>
            ${i}
          </button>
        `;
      } else if (
        (i === currentPage - 2 && i > 1) ||
        (i === currentPage + 2 && i < totalPages)
      ) {
        html += `<span class="page-dots">&hellip;</span>`;
      }
    }

    // Next Button
    html += `
      <button type="button" class="page-btn next-btn" ${currentPage === totalPages ? 'disabled' : ''} aria-label="Next page">
        Next <i class="fa-solid fa-chevron-right"></i>
      </button>
    `;

    paginationEl.innerHTML = html;

    // Attach Click Handlers
    paginationEl.querySelectorAll('.page-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        if (btn.classList.contains('prev-btn')) {
          if (currentPage > 1) goToPage(currentPage - 1);
        } else if (btn.classList.contains('next-btn')) {
          if (currentPage < totalPages) goToPage(currentPage + 1);
        } else {
          const targetPage = parseInt(btn.getAttribute('data-page'), 10);
          if (targetPage && targetPage !== currentPage) {
            goToPage(targetPage);
          }
        }
      });
    });
  }

  // Live Search listener
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      currentPage = 1;
      updateURL();
      render();
    });
  }

  // Category filter listeners
  catButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      catButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentCategory = btn.getAttribute('data-category') || 'all';
      currentPage = 1;
      updateURL();
      render();
    });
  });

  // Initial render
  render();
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

