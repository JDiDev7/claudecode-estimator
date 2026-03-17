import json
import requests # Ahora sí funcionará porque lo instalamos en el workflow
from datetime import datetime

def update_prices():
    # En el futuro, aquí usaremos 'requests' para leer la web de Anthropic.
    # Por ahora, mantenemos la lista maestra actualizada manualmente aquí:
    
    new_data = {
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "models": [
            {"id": "claude-4-6-sonnet", "name": "Claude 4.6 Sonnet (Latest)", "price": 2.50},
            {"id": "claude-4-0-opus", "name": "Claude 4.0 Opus", "price": 15.00},
            {"id": "claude-3-7-sonnet", "name": "Claude 3.7 Sonnet", "price": 3.00},
            {"id": "claude-3-5-sonnet", "name": "Claude 3.5 Sonnet", "price": 3.00},
            {"id": "claude-3-5-haiku", "name": "Claude 3.5 Haiku", "price": 0.25}
        ]
    }
    
    # Escribimos el archivo JSON que lee la web
    with open('prices.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=2, ensure_ascii=False)
    
    print("✅ JSON generado con éxito con los modelos más recientes.")

if __name__ == "__main__":
    update_prices()
