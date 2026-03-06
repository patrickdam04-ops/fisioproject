/* ═══════════════════════════════════════════════════════════════════
   FISIOPROJECT — JavaScript Interactions
   ═══════════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', () => {

    // ─── Navbar scroll effect ───
    const navbar = document.getElementById('navbar');
    const handleNavbarScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 60);
    };
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });
    handleNavbarScroll();

    // ─── Mobile Hamburger Menu ───
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('navMenu');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navMenu.classList.toggle('open');
        navbar.classList.toggle('menu-open', navMenu.classList.contains('open'));
        document.body.style.overflow = navMenu.classList.contains('open') ? 'hidden' : '';
    });

    // Close menu on link click
    navMenu.querySelectorAll('.navbar__link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navMenu.classList.remove('open');
            navbar.classList.remove('menu-open');
            document.body.style.overflow = '';
        });
    });

    // ─── Smooth Scroll for anchor links ───
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const target = document.querySelector(anchor.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // ─── Intersection Observer: Animate on Scroll ───
    const animatedElements = document.querySelectorAll('.animate-on-scroll');

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));

    // ─── Counter Animation ───
    const counterElements = document.querySelectorAll('[data-target]');

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const target = parseFloat(el.getAttribute('data-target'));
                const hasDecimal = el.getAttribute('data-decimal') === "true";
                const suffix = el.getAttribute('data-suffix') || '';
                animateCounter(el, target, hasDecimal, suffix);
                counterObserver.unobserve(el);
            }
        });
    }, { threshold: 0.5 });

    counterElements.forEach(el => counterObserver.observe(el));

    function animateCounter(element, target, hasDecimal, suffix) {
        const duration = 2000;
        const start = performance.now();

        function update(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);

            // Ease out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = eased * target;

            if (hasDecimal) {
                element.textContent = current.toFixed(1) + suffix;
            } else {
                element.textContent = Math.round(current) + suffix;
            }

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                element.textContent = (hasDecimal ? target.toFixed(1) : target) + suffix;
            }
        }

        requestAnimationFrame(update);
    }

    // ─── Reviews Auto-Scroll Carousel (Continuous) ───
    const track = document.getElementById('reviewsTrack');
    const carousel = document.getElementById('reviewsCarousel');

    if (track && carousel) {
        const cards = Array.from(track.children);
        const cardCount = cards.length;

        // Duplicate cards for seamless infinite loop
        cards.forEach(card => {
            const clone = card.cloneNode(true);
            clone.setAttribute('aria-hidden', 'true');
            track.appendChild(clone);
        });

        // Initialize continuous animation
        let animation;

        function initContinuousScroll() {
            if (animation) animation.cancel();

            // Calculate exact distance to scroll (width of all original items + gaps)
            const firstOriginal = track.children[0];
            const firstClone = track.children[cardCount];
            const distance = firstClone.offsetLeft - firstOriginal.offsetLeft;

            // Use Web Animations API for smooth continuous scrolling
            animation = track.animate(
                [
                    { transform: 'translateX(0px)' },
                    { transform: `translateX(-${distance}px)` }
                ],
                {
                    // Adjust duration to change scrolling speed (e.g., 35000ms = 35 seconds for one full loop)
                    duration: 45000,
                    iterations: Infinity,
                    easing: 'linear'
                }
            );
        }

        // Wait for layout to be ready to calculate offset correctly
        setTimeout(initContinuousScroll, 100);

        // Recalculate on resize
        window.addEventListener('resize', () => {
            initContinuousScroll();
        });

        // Pause on hover
        carousel.addEventListener('mouseenter', () => { if (animation) animation.pause(); });
        carousel.addEventListener('mouseleave', () => { if (animation) animation.play(); });
    }

    // ─── Sticky WhatsApp Bar (Mobile) ───
    const stickyWhatsapp = document.getElementById('stickyWhatsapp');
    if (stickyWhatsapp) {
        const showStickyAfter = 600;

        const handleStickyScroll = () => {
            stickyWhatsapp.classList.toggle('visible', window.scrollY > showStickyAfter);
        };

        window.addEventListener('scroll', handleStickyScroll, { passive: true });
        handleStickyScroll();
    }

    // ─── Active nav link highlighting ───
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.navbar__link');

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.toggle('active',
                        link.getAttribute('href') === `#${id}`
                    );
                });
            }
        });
    }, {
        threshold: 0.3,
        rootMargin: '-80px 0px -50% 0px'
    });

    sections.forEach(section => sectionObserver.observe(section));

});
