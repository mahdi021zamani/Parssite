with open("index.html", "r") as f:
    content = f.read()

install_target = """                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing Section -->"""

install_replacement = """                        </ul>
                    </div>

                    <div class="glass-card install-card fade-up" style="transition-delay: 300ms">
                        <div class="install-header">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"></path><path d="M10 2c1 .5 2 2 2 5"></path></svg>
                            <h3>macOS</h3>
                        </div>
                        <ul class="timeline">
                            <li>
                                <div class="timeline-step">۱</div>
                                <div class="timeline-content">دانلود برنامه FlClash یا SingBox</div>
                            </li>
                            <li>
                                <div class="timeline-step">۲</div>
                                <div class="timeline-content">نصب و اجرای برنامه در مک</div>
                            </li>
                            <li>
                                <div class="timeline-step">۳</div>
                                <div class="timeline-content">کپی کردن لینک اشتراک</div>
                            </li>
                            <li>
                                <div class="timeline-step">۴</div>
                                <div class="timeline-content">ورود به بخش Profiles و افزودن لینک</div>
                            </li>
                            <li>
                                <div class="timeline-step">۵</div>
                                <div class="timeline-content">بروزرسانی (Update) و سپس اتصال به سرور</div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Pricing Section -->"""

faq_target = """                    <div class="faq-item">
                        <button class="faq-question">
                            <span>چگونه سرویس خود را تمدید کنم؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>برای تمدید سرویس کافیست قبل از اتمام حجم یا زمان اشتراک، از طریق بات تلگرام یا تماس با پشتیبانی واتساپ اقدام به تمدید همان لینک قبلی نمایید تا نیاز به وارد کردن مجدد اطلاعات نداشته باشید.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

faq_replacement = """                    <div class="faq-item">
                        <button class="faq-question">
                            <span>نحوه خرید و تمدید اشتراک چگونه است؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>برای خرید یا تمدید اشتراک می‌توانید به سادگی از طریق تلگرام یا واتساپ با تیم پشتیبانی در ارتباط باشید. توجه داشته باشید در صورت تمدید، نیازی به وارد کردن لینک جدید نیست و همان لینک قبلی مجدداً شارژ خواهد شد.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>"""

if install_target in content:
    content = content.replace(install_target, install_replacement)
    print("Install section updated.")
else:
    print("Install target not found")

# Remove the old faq item about renewal to replace it with the new broader one
if faq_target in content:
    content = content.replace(faq_target, faq_replacement)
    print("FAQ section updated.")
else:
    print("FAQ target not found")
    
with open("index.html", "w") as f:
    f.write(content)

