document.addEventListener("DOMContentLoaded", function () {
    AOS.init(); // لتشغيل تأثيرات التمرير إذا كنتِ تستخدمين AOS.js
});

// تأثير عند التمرير لإضافة كلاس "نشط" على العناصر
window.addEventListener("scroll", function () {
    let header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 50);
});
document.querySelector(".lang-btn").addEventListener("click", function () {
    if (this.innerText.includes("EN")) {
        this.innerText = "🇸🇦 AR"; // تحويل للعربية
        document.documentElement.lang = "en"; // تغيير لغة الموقع
    } else {
        this.innerText = "🇬🇧 EN"; // تحويل للإنجليزية
        document.documentElement.lang = "ar";
    }
});

<script>
  const text = "Hi, I'm Aryam Aseiri ";
  const typingElement = document.getElementById("typing-text");
  let index = 0;

  function type() {
      if (index < text.length) {
          typingElement.textContent += text.charAt(index);
          index++;
          setTimeout(type, 100);
      }
  }
  type();
</script>

<script>
  let lastScrollTop = 0;
  const header = document.getElementById("mainHeader");

  window.addEventListener("scroll", function () {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
      // المستخدم نازل لتحت
      header.classList.add("hide-header");
    } else {
      // المستخدم طالع لفوق
      header.classList.remove("hide-header");
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // لحماية من scroll سلبي
  });
</script>

<script>
  window.addEventListener('scroll', function () {
    const hrElement = document.getElementById('dynamic-text');

    // قيمة التمرير العمودية (scroll)
    const scrollY = window.scrollY;

    // حساب سمك الفاصل: من 1px إلى 10px
    let borderWidth = 1 + scrollY / 50;

    // تحديد الحد الأعلى للسمك
    if (borderWidth > 10) borderWidth = 10;
    // تحديد الحد الأدنى للسمك
    if (borderWidth < 1) borderWidth = 1;

    // تطبيق التغيير على سمك الفاصل
    hrElement.style.borderWidth = borderWidth + 'px';
  });
</script>

