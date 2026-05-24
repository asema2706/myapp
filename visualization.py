import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

def collect_metrics():
    """Собирает метрики из нашего приложения (имитация мониторинга)"""
    try:
        response = requests.get('http://localhost:5000/health')
        data = response.json()
        return {'requests_served': data.get('requests_served', 0)}
    except:
        # Если приложение не запущено, используем тестовые данные
        return {'requests_served': 42}

def visualize():
    """Создаёт визуализацию метрик"""
    # Стиль графиков
    sns.set_style("whitegrid")
    
    # Данные для визуализации (имитируем нагрузку)
    endpoints = ['/', '/health', '/external']
    status_codes = [200, 200, 200]
    
    # Создаём график
    plt.figure(figsize=(10, 6))
    bars = plt.bar(endpoints, status_codes, color=['#2ecc71', '#3498db', '#e74c3c'])
    
    # Добавляем значения на столбцы
    for bar, value in zip(bars, status_codes):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                 f'Status: {value}', ha='center', fontsize=12)
    
    plt.title('API Endpoints Health Status', fontsize=16, fontweight='bold')
    plt.ylabel('HTTP Status Code', fontsize=12)
    plt.xlabel('Endpoints', fontsize=12)
    plt.ylim(0, 500)
    
    # Добавляем пояснительную линию для нормы
    plt.axhline(y=200, color='green', linestyle='--', alpha=0.7, label='OK Status (200)')
    plt.legend()
    
    # Сохраняем график
    plt.tight_layout()
    plt.savefig('requests_stats.png', dpi=150)
    plt.show()
    
    print("График сохранён как 'requests_stats.png'")

if __name__ == '__main__':
    visualize()