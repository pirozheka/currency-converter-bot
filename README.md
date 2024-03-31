______RUS_______
# Бот для конвертации валют

Этот бот для Telegram предназначен для конвертации валют. Он позволяет пользователям легко конвертировать валюту прямо в чате. 
Доступно пять валют, дополнительные можно добавить в config.py

## Инструкции по использованию

Чтобы настроить и запустить Бота на вашем локальном компьютере, следуйте этим шагам:

### Шаг 1: Клонировать репозиторий

Клонируйте репозиторий на ваш локальный компьютер с помощью следующей команды:

```bash
git clone https://github.com/pirozheka/currency-converter-bot.git
```

### Шаг 2: Создать виртуальное окружение

Перейдите в клонированную директорию и создайте виртуальное окружение:

```bash
cd currency-converter-bot
python -m venv venv
```

### Шаг 3: Активировать виртуальное окружение

Активируйте виртуальное окружение:

Для Windows:

```bash
venv\Scripts\activate
```

Для Linux/macOS:

```bash
source venv/bin/activate
```

### Шаг 4: Установить зависимости

Установите необходимые дополнительные библиотеки с помощью pip:

```bash
pip install pytelegrambotapi requests
```

Примечание: нет необходимости устанавливать `json`, так как это встроенная библиотека в Python.

### Шаг 5: Получить API Ключ

Получите ваш API ключ для конвертации валют от [ExchangeRates API](https://exchangeratesapi.io/).

### Шаг 6: Получить токен Telegram

Получите токен бота Telegram от BotFather в Telegram, отправив команду `/newbot` и следуя инструкциям.

### Шаг 7: Обновить конфигурацию

Обновите файл `config.py` вашим полученным `API_KEY` и `TOKEN`.

### Шаг 8: Запустить Бота

Выполните файл `app.py`, чтобы запустить бота:

```bash
python app.py
```

Убедитесь, что все инструкции были выполнены последовательно для правильной настройки и запуска бота. Если требуются дополнительные конфигурации или переменные окружения, включите также эти шаги в ваш процесс настройки.



______EN_______
# Currency Converter Bot
This is a Telegram bot designed to convert currencies.

## Usage Instructions

Follow these steps to set up and run the Currency Converter Bot on your local machine:

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/pirozheka/currency-converter-bot.git
```

### Step 2: Create a Virtual Environment

Navigate to the cloned directory and create a virtual environment:

```bash
cd currency-converter-bot
python -m venv venv
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On Linux/macOS:
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Dependencies

Install the required additional libraries using `pip`:

```bash
pip install pytelegrambotapi requests
```
Note: There is no need to install `json` since it is a built-in library in Python.

### Step 5: Obtain API Key

Get your API key for currency conversion from [ExchangeRates API](https://apilayer.com/marketplace/exchangerates_data-api).

### Step 6: Obtain Telegram Token

Get the Telegram bot token from the BotFather on Telegram by sending the command `/newbot` and following the instructions.

### Step 7: Update Configuration

Update the `config.py` file with your obtained `API_KEY` and `TOKEN`.

### Step 8: Run the Bot

Execute the `app.py` file to start the bot:

```bash
python app.py
```

---
Ensure that all instructions are followed in sequence to properly set up and run the bot. If additional configuration or environmental variables are required, include those steps as well.
