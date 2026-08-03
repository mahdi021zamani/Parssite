with open("index.html", "r") as f:
    content = f.read()

target = """                <div class="faq-container fade-up">
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>Subscription Link (لینک اشتراک) چیست؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>لینک اشتراک یک آدرس اختصاصی است که شامل تمام سرورهای خریداری شده شماست. با وارد کردن این لینک در برنامه‌های کلاینت، سرورها به صورت خودکار به گوشی یا سیستم شما اضافه می‌شوند و با هر بار آپدیت، لیست سرورها بروزرسانی می‌گردد.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>چگونه اشتراک را وارد کنم؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>بسته به سیستم‌عامل شما روش‌ها کمی متفاوت است، اما در تمامی برنامه‌ها گزینه‌ای با عنوان Add Subscription، Import from Clipboard یا Update Subscription وجود دارد. مراحل دقیق در بخش «آموزش نصب» توضیح داده شده است.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>اگر وصل نشد چه کنم؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>ابتدا از وصل بودن اینترنت اصلی خود مطمئن شوید. سپس در داخل برنامه گزینه Update Subscription را بزنید تا سرورهای جدید جایگزین شوند. اگر مشکل پابرجا بود، با پشتیبانی ما در تماس باشید.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>نحوه خرید و تمدید اشتراک چگونه است؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>برای خرید یا تمدید اشتراک می‌توانید به سادگی از طریق تلگرام یا واتساپ با تیم پشتیبانی در ارتباط باشید. توجه داشته باشید در صورت تمدید، نیازی به وارد کردن لینک جدید نیست و همان لینک قبلی مجدداً شارژ خواهد شد.</p>
                        </div>
                    </div>
                </div>"""

replacement = """                <div class="faq-container fade-up">
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>نحوه خرید و تمدید اشتراک چگونه است؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>برای خرید یا تمدید اشتراک می‌توانید به سادگی از طریق تلگرام یا واتساپ با تیم پشتیبانی در ارتباط باشید. توجه داشته باشید در صورت تمدید، نیازی به وارد کردن لینک جدید نیست و همان لینک قبلی مجدداً شارژ خواهد شد.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>Subscription Link (لینک اشتراک) چیست؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>لینک اشتراک یک آدرس اختصاصی است که شامل تمام سرورهای خریداری شده شماست. با وارد کردن این لینک در برنامه‌های کلاینت، سرورها به صورت خودکار به گوشی یا سیستم شما اضافه می‌شوند و با هر بار آپدیت، لیست سرورها بروزرسانی می‌گردد.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>چگونه اشتراک را وارد کنم؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>بسته به سیستم‌عامل شما روش‌ها کمی متفاوت است، اما در تمامی برنامه‌ها گزینه‌ای با عنوان Add Subscription، Import from Clipboard یا Update Subscription وجود دارد. مراحل دقیق در بخش «آموزش نصب» توضیح داده شده است.</p>
                        </div>
                    </div>
                    <div class="faq-item">
                        <button class="faq-question">
                            <span>اگر وصل نشد چه کنم؟</span>
                            <div class="faq-icon"></div>
                        </button>
                        <div class="faq-answer">
                            <p>ابتدا از وصل بودن اینترنت اصلی خود مطمئن شوید. سپس در داخل برنامه گزینه Update Subscription را بزنید تا سرورهای جدید جایگزین شوند. اگر مشکل پابرجا بود، با پشتیبانی ما در تماس باشید.</p>
                        </div>
                    </div>
                </div>"""

if target in content:
    content = content.replace(target, replacement)
    print("FAQ section updated.")
else:
    print("FAQ target not found")
    
with open("index.html", "w") as f:
    f.write(content)

