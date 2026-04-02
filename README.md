# WhatsApp AI Agent 

An AI agent that automatically replies to WhatsApp messages using Groq (Llama 3) and Twilio.

## Features
- Auto replies to WhatsApp messages
- Mimics a custom personality using system prompts
- Built with Python, Flask, Groq API, and Twilio

## Tech Stack
- Python
- Flask
- Groq API (Llama 3)
- Twilio WhatsApp API
- ngrok

## How it works
1. A message is received on WhatsApp via Twilio
2. Flask webhook receives the message
3. Groq AI generates a reply based on a custom personality
4. The reply is sent back via Twilio
```
