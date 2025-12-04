document.addEventListener('DOMContentLoaded', () => {

    
    const allSections = document.querySelectorAll('main section');
    const navLinks = document.querySelectorAll('.nav-link');

    const showSection = (targetId) => {
        allSections.forEach(section => {
            section.classList.add('hidden');
        });
        

        const targetSection = document.getElementById(targetId);
        if (targetSection) {
            targetSection.classList.remove('hidden');
        }
    };
    
    
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault(); 
            const targetId = link.getAttribute('data-section-id');
            showSection(targetId);
            
            
            const mobileMenu = document.getElementById('mobile-menu');
            if (mobileMenu && !mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('hidden');
            }

            window.scrollTo(0, 0); 
        });
    });

    
    showSection('home');
    
    
    const themeToggle = document.getElementById('theme-toggle');
    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');
    const bodyElement = document.body; 

    
    const isDarkMode = localStorage.getItem('theme') === 'dark' || 
                       (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);

    
    if (isDarkMode) {
        bodyElement.classList.add('dark-mode');
        moonIcon.classList.add('hidden');
        sunIcon.classList.remove('hidden');
    } else {
        bodyElement.classList.remove('dark-mode');
        moonIcon.classList.remove('hidden');
        sunIcon.classList.add('hidden');
    }

    
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

    
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');

    mobileMenuButton.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
    });
    

});