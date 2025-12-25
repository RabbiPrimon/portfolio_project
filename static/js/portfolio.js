// Portfolio Interactive Features - Pythonic v2
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize AOS (Animate On Scroll)
    AOS.init({
        duration: 800,
        easing: 'ease-out',
        once: true,
        offset: 100
    });

    // Sticky Navigation with Sharper Glassmorphism
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.background = 'rgba(1, 4, 9, 0.95)';
                navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.5)';
            } else {
                navbar.style.background = 'rgba(13, 17, 23, 0.8)';
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // Unified Tech Filter (General Logic)
    window.filterTech = function(category) {
        const items = document.querySelectorAll('.tech-item');
        const tabs = document.querySelectorAll('.skill-tab');
        
        tabs.forEach(tab => {
            if (tab.innerText.includes(category) || (category === 'all' && tab.innerText === 'all_tech')) {
                tab.classList.add('active');
            } else {
                tab.classList.remove('active');
            }
        });

        items.forEach(item => {
            if (category === 'all' || item.getAttribute('data-category') === category) {
                item.style.display = 'block';
                item.style.opacity = '1';
                item.style.transform = 'translateY(0)';
            } else {
                item.style.display = 'none';
                item.style.opacity = '0';
                item.style.transform = 'translateY(20px)';
            }
        });
        AOS.refresh();
    };

    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    const offsetTop = target.offsetTop - 80;
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Form Color Sync
    const pyInputs = document.querySelectorAll('.form-control');
    pyInputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.style.borderColor = 'var(--py-blue)';
            input.style.boxShadow = 'var(--glow-blue)';
        });
        input.addEventListener('blur', () => {
            input.style.borderColor = 'var(--glass-border)';
            input.style.boxShadow = 'none';
        });
    });

    console.log('🐍 Pythonic Portfolio Engine Activated');
});
