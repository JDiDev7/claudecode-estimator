import requests
import json
from datetime import datetime

def update_prices():
    # URL de la documentación de Anthropic (donde suelen poner los precios)
    # Nota: Si Anthropic cambia la estructura, ajustamos el selector.
    url = "https://api.anthropic.com/v1/models" # O su página de pricing
    
    # Por ahora, simulamos la extracción para asegurar que el flujo funciona
    # En un caso real, usaríamos BeautifulSoup para scrapear el HTML
    
    new_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "models": [
            {"id": "claude-4-6-sonnet", "name": "Claude 4.6 Sonnet", "price": 2.50},
            {"id": "claude-4-0-opus", "name": "Claude 4.0 Opus", "price": 15.00},
            {"id": "claude-3-7-sonnet", "name": "Claude 3.7 Sonnet", "price": 3.00},
            {"id": "claude-3-5-haiku", "name": "Claude 3.5 Haiku", "price": 0.25}
        ]
    }
    
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    print("✅ prices.json actualizado correctamente.")

if __name__ == "__main__":
    update_prices()
