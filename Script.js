document.addEventListener('DOMContentLoaded', () => {

    // --- Core Section Switching Logic ---
    const allSections = document.querySelectorAll('main section');
    const navLinks = document.querySelectorAll('.nav-link');

    // Function to show only the selected section
    const showSection = (targetId) => {
        // Hide all sections first
        allSections.forEach(section => {
            section.classList.add('hidden');
        });
        
        // Show the target section
        const targetSection = document.getElementById(targetId);
        if (targetSection) {
            targetSection.classList.remove('hidden');
        }
    };
    
    // Handle navigation clicks
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault(); // Stop default anchor link behavior
            const targetId = link.getAttribute('data-section-id');
            showSection(targetId);
            
            // Close mobile menu after clicking a link
            const mobileMenu = document.getElementById('mobile-menu');
            if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
            }

            // Scroll to the top of the new section (below the fixed header)
            window.scrollTo(0, 0); 
        });
    });

    // Initialize: Show the home section on load
    showSection('home');
    
    // --- Theme Toggle Logic ---
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    const bodyElement = document.body; // Changed from htmlElement to bodyElement to match CSS selector body.dark-mode

    // Check localStorage for theme preference or system preference
    const isDarkMode = localStorage.getItem('theme') === 'dark' || 
                       (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);

    // Apply initial theme state
    if (isDarkMode) {
        bodyElement.classList.add('dark-mode');
        moonIcon.classList.add('hidden');
        sunIcon.classList.remove('hidden');
    } else {
        bodyElement.classList.remove('dark-mode');
        moonIcon.classList.remove('hidden');
        sunIcon.classList.add('hidden');
    }

    // Toggle theme on button click
    themeToggle.addEventListener('click', () => {
        if (bodyElement.classList.contains('dark-mode')) {
            bodyElement.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
            moonIcon.classList.remove('hidden');
            sunIcon.classList.add('hidden');
        } else {
            bodyElement.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
            moonIcon.classList.add('hidden');
            sunIcon.classList.remove('hidden');
        }
    });

    // --- Mobile Menu Toggle Logic (remains the same) ---
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
    
    // --- REMOVED: Code Modal Logic ---
});