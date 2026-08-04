with open("script.js", "r") as f:
    content = f.read()

target = """                        // Smooth scroll to top of the item, accounting for sticky header
                        setTimeout(() => {
                            const headerOffset = 100; // Approximate header height + some padding
                            const elementPosition = item.getBoundingClientRect().top;
                            const offsetPosition = elementPosition + window.scrollY - headerOffset;
                            
                            window.scrollTo({
                                top: offsetPosition,
                                behavior: "smooth"
                            });
                        }, 300); // Wait for transition to start/finish"""

replacement = """                        // Smooth scroll to top of the item, accounting for sticky header
                        setTimeout(() => {
                            const headerOffset = 100; // Approximate header height + some padding
                            const elementPosition = item.getBoundingClientRect().top;
                            const offsetPosition = elementPosition + window.scrollY - headerOffset;
                            
                            window.scrollTo({
                                top: offsetPosition,
                                behavior: "smooth"
                            });
                        }, 410); // Wait for transition to finish so position is accurate"""

if target in content:
    content = content.replace(target, replacement)
    with open("script.js", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
