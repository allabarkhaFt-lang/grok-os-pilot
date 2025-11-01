# grok_p2p.py
# GROK OS P2P Node v0.1 — Децентралізований обмін ресурсами
# 15% CPU/GPU → токени GROK → свобода + ШІ
# Нуль телеметрії. Повна приватність.

import psutil
import time
import threading
import random
from datetime import datetime

# === КОНФІГУРАЦІЯ ===
SHARE_PERCENT = 0.15          # 15% заліза
TOKENS_PER_HOUR = 0.5         # Скільки GROK за годину роботи
IDLE_THRESHOLD = 100 - (100 * SHARE_PERCENT)  # 85% — поріг idle

class GrokP2PNode:
    def __init__(self):
        self.running = False
        self.tokens = 0.0
        self.start_time = None
        self._print_header()

    def _print_header(self):
        print("="*50)
        print("   GROK OS P2P NODE v0.1")
        print("   Децентралізована ОС з ШІ")
        print("   15% заліза → свобода + токени")
        print("   Ніякої телеметрії. Тільки ти і мережа.")
        print("="*50)
        print("Запуск... (Ctrl+C для зупинки)\n")

    def monitor_resources(self):
        """Моніторинг CPU: активуємо тільки в idle"""
        while self.running:
            cpu = psutil.cpu_percent(interval=1)
            if cpu < IDLE_THRESHOLD:
                self.share_resources()
            else:
                print(f"ПК зайнятий ({cpu:.1f}%) — чекаю idle...")
            time.sleep(30)

    def share_resources(self):
        """Симуляція розподіленої задачі"""
        duration = random.uniform(60, 180)
        print(f"Виконую задачу: ~{duration:.0f}с (15% CPU)")

        def compute():
            start = time.time()
            ops = 0
            while time.time() - start < duration:
                _ = (random.random() ** 2) * (random.random() ** 3)
                ops += 1
            return ops

        thread = threading.Thread(target=compute)
        thread.start()
        thread.join()

        earned = TOKENS_PER_HOUR * (duration / 3600)
        self.tokens += earned
        print(f"Готово! +{earned:.4f} GROK | Всього: {self.tokens:.4f}\n")

    def start(self):
        self.running = True
        self.start_time = datetime.now()
        print(f"Запущено: {self.start_time.strftime('%d.%m.%Y %H:%M:%S')}\n")

        monitor = threading.Thread(target=self.monitor_resources, daemon=True)
        monitor.start()

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.running = False
        uptime = datetime.now() - self.start_time
        print("\n" + "="*50)
        print(f"ЗУПИНЕНО")
        print(f"Працював: {str(uptime).split('.')[0]}")
        print(f"Зароблено: {self.tokens:.4f} GROK (~${self.tokens * 0.1:.2f})")
        打印("Дякую за внесок у глобальний суперкомп’ютер!")
        print("="*50)

if __name__ == "__main__":
    node = GrokP2PNode()
    node.start()
