const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const regex = /<div class="platform-section fade-up">([\s\S]*?)<\/div>\s*<\/section>/;

const newHTML = `
                <div class="accordion-container fade-up">
                    <!-- Android -->
                    <div class="accordion-item active">
                        <div class="accordion-header">
                            <div class="accordion-title">
                                <span class="platform-emoji">🤖</span> Android
                            </div>
                            <div class="accordion-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                        </div>
                        <div class="accordion-content">
                            <div class="grid downloads-grid">
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper">
                                        <img src="assets/logo.png" alt="PARSCLOUD" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; padding: 5px;">
                                    </div>
                                    <h4>PARSCLOUD</h4>
                                    <p>برنامه اختصاصی پارس‌کلود</p>
                                    <a href="assets/parscloud.apk" class="btn btn-download">دانلود مستقیم</a>
                                </div>
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/v2rayng.png" alt="V2RayNG" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>V2RayNG</h4>
                                    <p>پیشنهادی برای اندروید</p>
                                    <a href="assets/v2rayng.apk" class="btn btn-download">دانلود مستقیم</a>
                                </div>
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/hiddify.png" alt="Hiddify" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>Hiddify</h4>
                                    <p>رابط کاربری ساده و سریع</p>
                                    <a href="assets/hiddify.apk" class="btn btn-download">دانلود مستقیم</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- iOS -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-title">
                                <span class="platform-emoji">🍎</span> iOS
                            </div>
                            <div class="accordion-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                        </div>
                        <div class="accordion-content">
                            <div class="grid downloads-grid center-grid">
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/streisand.png" alt="Streisand" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>Streisand</h4>
                                    <p>محبوب‌ترین کلاینت آی‌اواس</p>
                                    <a href="assets/streisand.ipa" class="btn btn-download">دانلود از App Store</a>
                                </div>
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/hiddify.png" alt="Hiddify" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>Hiddify</h4>
                                    <p>پشتیبانی کامل از جدیدترین پروتکل‌ها</p>
                                    <a href="assets/hiddify.ipa" class="btn btn-download">دانلود از App Store</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Windows -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-title">
                                <span class="platform-emoji">🪟</span> Windows
                            </div>
                            <div class="accordion-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                        </div>
                        <div class="accordion-content">
                            <div class="grid downloads-grid center-grid">
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/v2rayn.png" alt="V2RayN" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>V2RayN</h4>
                                    <p>کلاینت قدرتمند ویندوز</p>
                                    <a href="assets/v2rayn.zip" class="btn btn-download">دانلود فایل ZIP</a>
                                </div>
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/hiddify.png" alt="Hiddify" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>Hiddify</h4>
                                    <p>نسخه دسکتاپ هیدیفای</p>
                                    <a href="assets/hiddify.exe" class="btn btn-download">دانلود فایل EXE</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- macOS -->
                    <div class="accordion-item">
                        <div class="accordion-header">
                            <div class="accordion-title">
                                <span class="platform-emoji">🍏</span> macOS
                            </div>
                            <div class="accordion-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                            </div>
                        </div>
                        <div class="accordion-content">
                            <div class="grid downloads-grid center-grid">
                                <div class="glass-card download-card">
                                    <div class="app-icon-wrapper" style="overflow: hidden; padding: 0;">
                                        <img src="assets/hiddify.png" alt="Hiddify" class="app-icon" style="width: 100%; height: 100%; object-fit: contain; border-radius: 12px;">
                                    </div>
                                    <h4>Hiddify</h4>
                                    <p>کلاینت قدرتمند مک</p>
                                    <a href="assets/hiddify.dmg" class="btn btn-download">دانلود فایل DMG</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>`;

content = content.replace(/<div class="platform-section fade-up">[\s\S]*?<\/div>\s*<\/section>/, newHTML);
fs.writeFileSync('index.html', content);
