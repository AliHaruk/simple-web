import requests
import json

def send_discord_webhook(webhook_url, message):
    data = {
        "content": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    if response.status_code == 204:
        print("Message sent to Discord webhook successfully.")
    else:
        print(f"Failed to send message to Discord webhook. Status code: {response.status_code}")

# Replace the webhook URL with your actual Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1083128480801234985/9jnFLFs_noPNlVs41Hv2FmDyGj2Cu8CkVVHULRBcmt0DhcfsYna4UHPrpYd6pd7ehJ7Y"
message = "Hello, Discord!"

send_discord_webhook(webhook_url, message)
