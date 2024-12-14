import tkinter as tk
import requests
from datetime import datetime

def fetch_crypto_data():
    try:
        # Add more cryptocurrencies to the API request
        response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin,litecoin&vs_currencies=usd")
        data = response.json()

        # Extract prices
        btc_price = data['bitcoin']['usd']
        eth_price = data['ethereum']['usd']
        doge_price = data['dogecoin']['usd']
        ltc_price = data['litecoin']['usd']

        # Get current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update labels
        btc_label.config(text=f"Bitcoin: ${btc_price}")
        eth_label.config(text=f"Ethereum: ${eth_price}")
        doge_label.config(text=f"Dogecoin: ${doge_price}")
        ltc_label.config(text=f"Litecoin: ${ltc_price}")
        
        # Display the time of data extraction
        time_label.config(text=f"Data last updated: {current_time}")
        
        error_label.config(text="")  # Clear error message if data is fetched
    except Exception as e:
        error_label.config(text="Error fetching data. Check connection.")
        time_label.config(text="")  # Clear the time if there's an error

# GUI Setup
root = tk.Tk()
root.title("Crypto Price Tracker")
root.geometry("350x350")
root.config(bg="#f4f4f9")  # Soft background color

# Title Label
title_label = tk.Label(root, text="Crypto Prices", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=20)

# Price Labels
btc_label = tk.Label(root, text="Bitcoin: Fetching...", font=("Arial", 14), bg="#f4f4f9", fg="#333")
btc_label.pack(pady=5)

eth_label = tk.Label(root, text="Ethereum: Fetching...", font=("Arial", 14), bg="#f4f4f9", fg="#333")
eth_label.pack(pady=5)

doge_label = tk.Label(root, text="Dogecoin: Fetching...", font=("Arial", 14), bg="#f4f4f9", fg="#333")
doge_label.pack(pady=5)

ltc_label = tk.Label(root, text="Litecoin: Fetching...", font=("Arial", 14), bg="#f4f4f9", fg="#333")
ltc_label.pack(pady=5)

# Error Label
error_label = tk.Label(root, text="", fg="red", font=("Arial", 12), bg="#f4f4f9")
error_label.pack(pady=10)

# Time Label
time_label = tk.Label(root, text="Data last updated: N/A", font=("Arial", 10), bg="#f4f4f9", fg="#666")
time_label.pack(pady=5)

# Fetch Button
fetch_button = tk.Button(root, text="Refresh Prices", command=fetch_crypto_data, font=("Arial", 12), bg="#007bff", fg="white", relief="raised", bd=2)
fetch_button.pack(pady=10, ipadx=10, ipady=5)

# Initial Fetch
fetch_crypto_data()

# Main Loop
root.mainloop()
