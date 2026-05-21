document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("contactForm");
    if (!form) return;

    // Django'nun id_for_label çıktısına göre ID'ler "id_" ile başlar
    const nameInput = document.getElementById("id_name");
    const lastNameInput = document.getElementById("id_last_name");
    const emailInput = document.getElementById("id_email");
    const subjectInput = document.getElementById("id_subject");
    const messageInput = document.getElementById("id_message");

    const submitBtn = document.getElementById("contactSubmit");
    const submitText = document.getElementById("submitText");
    const submitSpinner = document.getElementById("submitSpinner");

    const formMessage = document.getElementById("formMessage");

    // =========================
    // VALIDATION KURALLARI
    // =========================
    const validators = {
        name(value) {
            if (value.trim() === "") return "Ad alanı zorunludur.";
            if (value.trim().length < 2) return "Ad en az 2 karakter olmalıdır.";
            return "";
        },
        last_name(value) {
            if (value.trim() === "") return "Soyad alanı zorunludur.";
            if (value.trim().length < 2) return "Soyad en az 2 karakter olmalıdır.";
            return "";
        },
        email(value) {
            if (value.trim() === "") return "Email adresi zorunludur.";
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value.trim())) return "Geçerli bir email adresi giriniz.";
            return "";
        },
        subject(value) {
            if (value.trim() === "") return "Konu alanı boş bırakılamaz.";
            if (value.trim().length < 3) return "Konu çok kısa görünüyor.";
            return "";
        },
        message(value) {
            if (value.trim() === "") return "Mesaj alanı boş bırakılamaz.";
            if (value.trim().length < 10) return "Mesaj en az 10 karakter olmalıdır.";
            return "";
        }
    };

    // =========================
    // UI YARDIMCILARI (Kırmızı/Yeşil çerçeve ve hata metni ekleme)
    // =========================
    function setError(input, message) {
        if (!input) return;
        input.classList.remove("is-valid");
        input.classList.add("is-invalid");

        let feedback = input.parentElement.querySelector(".invalid-feedback");
        if (!feedback) {
            feedback = document.createElement("div");
            feedback.className = "invalid-feedback";
            input.parentElement.appendChild(feedback);
        }
        feedback.textContent = message;
    }

    function setSuccess(input) {
        if (!input) return;
        input.classList.remove("is-invalid");
        input.classList.add("is-valid");
    }

    function clearValidation(input) {
        if (!input) return;
        input.classList.remove("is-invalid");
        input.classList.remove("is-valid");
    }

    function validateField(input, validator) {
        if (!input) return false;
        const error = validator(input.value);
        if (error) {
            setError(input, error);
            return false;
        } else {
            setSuccess(input);
            return true;
        }
    }

    // =========================
    // GERÇEK ZAMANLI KONTROL (Kullanıcı yazarken)
    // =========================
    if (nameInput) nameInput.addEventListener("input", () => validateField(nameInput, validators.name));
    if (lastNameInput) lastNameInput.addEventListener("input", () => validateField(lastNameInput, validators.last_name));
    if (emailInput) emailInput.addEventListener("input", () => validateField(emailInput, validators.email));
    if (subjectInput) subjectInput.addEventListener("input", () => validateField(subjectInput, validators.subject));
    if (messageInput) messageInput.addEventListener("input", () => validateField(messageInput, validators.message));

    function validateForm() {
        let valid = true;
        if (!validateField(nameInput, validators.name)) valid = false;
        if (!validateField(lastNameInput, validators.last_name)) valid = false;
        if (!validateField(emailInput, validators.email)) valid = false;
        if (!validateField(subjectInput, validators.subject)) valid = false;
        if (!validateField(messageInput, validators.message)) valid = false;
        return valid;
    }

    // =========================
    // FORM GÖNDERME (AJAX / Fetch API)
    // =========================
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        if (formMessage) formMessage.innerHTML = "";

        if (!validateForm()) {
            if (formMessage) {
                formMessage.innerHTML = `<div class="alert alert-danger">Lütfen formdaki hataları düzeltin.</div>`;
            }
            return;
        }

        // Yükleniyor durumu aktif
        if (submitBtn) submitBtn.disabled = true;
        if (submitText) submitText.textContent = "Gönderiliyor...";
        if (submitSpinner) submitSpinner.classList.remove("d-none");

        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: "POST",
                body: formData,
                headers: {
                    "X-Requested-With": "XMLHttpRequest"
                }
            });

            const data = await response.json();

            if (response.ok && data.success) {
                // Başarılı senaryosu
                if (formMessage) {
                    formMessage.innerHTML = `<div class="alert alert-success">${data.message || 'Mesajınız başarıyla gönderildi.'}</div>`;
                }
                form.reset();
                document.querySelectorAll(".form-control").forEach(input => clearValidation(input));
            } else {
                // Backend'den gelen hata (Örn: Veritabanı veya E-posta sunucu hatası)
                if (formMessage) {
                    formMessage.innerHTML = `<div class="alert alert-danger">${data.message || 'Mesaj gönderilemedi. Lütfen eksikleri kontrol edin.'}</div>`;
                }
            }

        } catch (error) {
            console.error("Fetch Error:", error);
            if (formMessage) {
                formMessage.innerHTML = `<div class="alert alert-danger">Sunucu bağlantısında bir hata oluştu. Lütfen bağlantınızı kontrol edin.</div>`;
            }
        } finally {
            // Butonu tekrar normale döndür
            if (submitBtn) submitBtn.disabled = false;
            if (submitText) submitText.textContent = "Gönder";
            if (submitSpinner) submitSpinner.classList.add("d-none");
        }
    });

});