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
