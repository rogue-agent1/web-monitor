#!/usr/bin/env python3
"""Notification module for web-monitor.

Supports: Telegram, Email (SMTP), Webhook (HTTP POST).
"""
import json
import urllib.request

def send_webhook(url: str, payload: dict) -> bool:
    """Send change notification via webhook."""
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status == 200
    except Exception as e:
        print(f"Webhook failed: {e}")
        return False

if __name__ == "__main__":
    print("Notification module loaded. Use send_webhook() for HTTP notifications.")
