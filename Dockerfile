# Resmi ve hafif Python imajını kullanıyoruz
FROM python:3.13-slim

# Python'ın çıktıları direkt terminale basması ve .pyc dosyaları oluşturmaması için
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Çalışma dizinini ayarlıyoruz
WORKDIR /srv/app

# Gerekli sistem paketlerini kuruyoruz (Veritabanı sürücüleri vb. için gerekebilir)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Önce sadece requirements.txt'yi kopyalayıp kütüphaneleri kuruyoruz (Önbellek avantajı için)
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Kodlarımızı konteyner içine kopyalıyoruz
COPY . .

# 8000 portunu dışarı açıyoruz
EXPOSE 8000

# Sunucuyu başlatıyoruz
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]