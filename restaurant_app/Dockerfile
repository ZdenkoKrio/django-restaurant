FROM python:3.8

# pracovný adresár v kontajneri
WORKDIR /app

# Skopírujte obsah aktuálneho adresára (vrátane requirements.txt) do pracovného adresára v kontajneri
COPY . /app

# Inštalujte závislosti uvedené v súbore requirements.txt
RUN pip install django

EXPOSE 3000
# Spustite príkaz alebo aplikáciu
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]
