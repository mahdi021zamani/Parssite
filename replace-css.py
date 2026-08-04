with open("style.css", "r") as f:
    content = f.read()

target = """/* Downloads */
.platform-section {
    margin-bottom: 60px;
}

.platform-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 30px;
    text-align: center;
    color: #fff;
    font-family: system-ui, -apple-system, sans-serif;
    letter-spacing: 1px;
}"""

replacement = """/* Accordion Downloads */
.accordion-container {
    max-width: 800px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.accordion-item {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 16px;
    margin-bottom: 15px;
    overflow: hidden;
    transition: var(--transition);
}
.accordion-item.active {
    border-color: rgba(96, 165, 250, 0.4);
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.1);
}
.accordion-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 25px;
    cursor: pointer;
    user-select: none;
    transition: var(--transition);
}
.accordion-header:hover {
    background: rgba(255, 255, 255, 0.03);
}
.accordion-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: system-ui, -apple-system, sans-serif;
}
.platform-emoji {
    font-size: 1.5rem;
}
.accordion-icon {
    color: var(--text-muted);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.accordion-item.active .accordion-icon {
    transform: rotate(180deg);
    color: var(--primary);
}
.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.4s ease-out;
}
.accordion-content .downloads-grid {
    padding: 0 25px 25px;
}
"""

if target in content:
    content = content.replace(target, replacement)
    with open("style.css", "w") as f:
        f.write(content)
    print("Success")
else:
    print("Target not found")
