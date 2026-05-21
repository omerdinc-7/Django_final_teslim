#!/bin/bash

    # Veritabanı tablolarını oluştur
    echo "Veritabanı migrasyonları yapılıyor..."
    python manage.py migrate

    # Dockerfile'daki CMD komutunu (runserver) çalıştır
    exec "$@"
    ```



    Terminalde bu dosyanın olduğu dizine gidip dosyaya çalıştırılabilme izni ver:
    ```bash
    chmod +x entrypoint.sh
    ```



    Yukarıda verdiğim temiz `Dockerfile`'ın en sonuna, `CMD` satırından hemen **önce** şu satırı ekle:
    ```dockerfile
    ENTRYPOINT ["/srv/app/entrypoint.sh"]
    ```