with open("script.js", "r") as f:
    content = f.read()

replacement = """
    // 6. Downloads Accordion
    const downloadItems = document.querySelectorAll('.accordion-item');
    
    function initDownloadAccordion() {
        downloadItems.forEach(item => {
            const header = item.querySelector('.accordion-header');
            const content = item.querySelector('.accordion-content');
            
            if (header && content) {
                header.addEventListener('click', () => {
                    const isActive = item.classList.contains('active');
                    
                    // Close all others
                    downloadItems.forEach(otherItem => {
                        otherItem.classList.remove('active');
                        otherItem.querySelector('.accordion-content').style.maxHeight = null;
                    });
                    
                    // Toggle current
                    if (!isActive) {
                        item.classList.add('active');
                        content.style.maxHeight = content.scrollHeight + 'px';
                    }
                });
            }
        });
    }

    // Initialize accordion clicks
    initDownloadAccordion();

    // Set initial active heights after images load so scrollHeight is accurate
    window.addEventListener('load', () => {
        downloadItems.forEach(item => {
            if (item.classList.contains('active')) {
                const content = item.querySelector('.accordion-content');
                if (content) {
                    content.style.maxHeight = content.scrollHeight + 'px';
                }
            }
        });
    });

    // Recalculate heights on window resize
    window.addEventListener('resize', () => {
        downloadItems.forEach(item => {
            if (item.classList.contains('active')) {
                const content = item.querySelector('.accordion-content');
                if (content) {
                    content.style.maxHeight = content.scrollHeight + 'px';
                }
            }
        });
    });
});
"""

if content.endswith("});\n") or content.endswith("});"):
    content = content.rsplit("});", 1)[0] + replacement
    with open("script.js", "w") as f:
        f.write(content)
    print("Success JS update")
