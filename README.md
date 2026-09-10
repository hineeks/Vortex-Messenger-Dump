# Vortex Messenger

> 🌀 Мощный инструмент для управления и анализа данных мессенджера Vortex

Vortex Messenger Dump — это открытый проект, который помогает пользователям экспортировать, анализировать и визуализировать данные из мессенджера Vortex. Идеален для архивирования переписки, анализа статистики и сохранения важных разговоров.

## ✨ Особенности

- 📥 **Экспорт данных** — сохраняйте переписку в различные форматы (JSON, CSV, HTML)
- 📊 **Анализ статистики** — получайте подробные отчеты о активности и статистике
- 🎨 **Визуализация** — красивые графики и диаграммы
- 💾 **Резервное копирование** — безопасное сохранение всех данных
- ⚡ **Быстрая работа** — оптимизированный код для работы с большими объемами данных
- 🔒 **Приватность** — вся обработка данных происходит локально

## 🚀 Быстрый старт

### Требования
- Python 3.8+
- pip

### Установка

```bash
git clone https://github.com/hineeks/Vortex-Messenger-Dump-Sbork-.git
cd Vortex-Messenger-Dump-Sbork-
pip install -r requirements.txt
```

### Использование

```python
from vortex_dump import VortexDump

# Инициализация
dump = VortexDump(token="your_token_here")

# Экспорт всех сообщений
dump.export_all(format="json", output_dir="./exports")

# Получение статистики
stats = dump.get_statistics()
print(f"Всего сообщений: {stats['total_messages']}")
print(f"Уникальных пользователей: {stats['unique_users']}")
```

## 📚 Документация

### API Примеры

#### Экспорт сообщений
```python
dump.export_messages(
    chat_id="123456",
    start_date="2024-01-01",
    end_date="2024-12-31",
    format="html"
)
```

#### Анализ активности
```python
activity = dump.analyze_activity(chat_id="123456")
print(f"Пиковое время активности: {activity['peak_hour']}")
print(f"Самый активный пользователь: {activity['top_user']}")
```

#### Поиск по сообщениям
```python
results = dump.search(
    query="важное",
    chat_id="123456",
    limit=100
)
```

## 🎯 Примеры использования

### Создание HTML отчета
```bash
python export.py --chat-id 123456 --format html --output report.html
```

### Экспорт в CSV
```bash
python export.py --chat-id 123456 --format csv --output data.csv
```

### Анализ статистики
```bash
python analyze.py --chat-id 123456 --generate-graphs
```

## 🔧 Структура проекта

```
.
├── vortex_dump/
│   ├── __init__.py
│   ├── core.py           # Основной класс VortexDump
│   ├── exporters.py      # Экспортеры (JSON, CSV, HTML)
│   ├── analyzers.py      # Анализаторы данных
│   └── utils.py          # Вспомогательные функции
├── examples/
│   ├── basic_export.py
│   ├── analyze_stats.py
│   └── search_messages.py
├── tests/
│   ├── test_export.py
│   ├── test_analysis.py
│   └── test_utils.py
├── requirements.txt
├── setup.py
└── README.md
```

## 📈 Возможности анализа

- 📅 Анализ активности по времени
- 👥 Статистика по пользователям
- 💬 Анализ частоты использования слов
- 📌 Выделение ключевых тем
- 🔗 Анализ связей между пользователями
- 📊 Генерация подробных отчетов

## 🌐 Форматы экспорта

- **JSON** — полная информация с метаданными
- **CSV** — табличный формат для анализа в Excel/Google Sheets
- **HTML** — красивый отчет для просмотра в браузере
- **PDF** — готовый документ для печати

## 🤝 Вклад в проект

Мы приветствуем контрибьюции! 

1. Fork репозиторий
2. Создайте ветку для вашей фичи (`git checkout -b feature/AmazingFeature`)
3. Commit ваши изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📝 Лицензия

Проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 🙋 Поддержка

Если у вас есть вопросы или проблемы:
- 📖 Посмотрите [документацию](docs/)
- 💬 Создайте [issue](https://github.com/hineeks/Vortex-Messenger-Dump-Sbork-/issues)
- 📧 Свяжитесь с нами через GitHub Discussions

## 🎓 Примеры использования

Смотрите папку [examples/](examples/) для полных рабочих примеров.

---

**⭐ Если проект вам помогает, поставьте звездочку! Это помогает нам развивать проект.**

Сделано с ❤️ для сообщества




Об авторе:
GitHub: [Профиль GitHub](https://github.com/hineeks)
