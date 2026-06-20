document.addEventListener('DOMContentLoaded', () => {
    const categoryBtns = document.querySelectorAll('.category-btn');
    const sections = document.querySelectorAll('.category-section');

    // Kategori butonlarına tıklama ile kaydırma
    categoryBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetId = btn.getAttribute('data-target');
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                // Smooth scroll to the section
                targetSection.scrollIntoView({ behavior: 'smooth' });
                
                // Update active button immediately for better UX
                categoryBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
            }
        });
    });

    // Intersection Observer ile scroll yaparken aktif kategoriyi belirleme
    const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -70% 0px', // Adjust these values to change trigger area
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                
                // Remove active class from all
                categoryBtns.forEach(btn => btn.classList.remove('active'));
                
                // Add active class to intersecting one
                const activeBtn = document.querySelector(`.category-btn[data-target="${id}"]`);
                if (activeBtn) {
                    activeBtn.classList.add('active');
                    // Scroll the category nav horizontally to show active button
                    activeBtn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
});
