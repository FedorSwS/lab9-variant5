\# Лабораторная работа №9 — Вариант 5



\## Интеграция Python + Go + Rust



\### Задания



| Тип | Задание | Описание |

|-----|---------|----------|

| Средн.1 (Go) | 5 | TCP-сервер на Go |

| Средн.2 (Go) | 2 | Горутина для фоновой обработки |

| Средн.3 (Rust) | 10 | Структура Rust как Python класс |

| Повыш.1 | 5 | Профилирование производительности |

| Повыш.2 | 3 | CI/CD для Rust-модуля |



\### Структура проекта

├── go\_tcp\_server/ # Go TCP сервер с горутинами

├── rust\_class\_lib/ # Rust библиотека с PyO3

├── python\_client/ # Python клиент и тесты

├── .github/workflows/ # CI/CD конфигурация

└── scripts/ # Скрипты сборки



\### Установка и запуск



```bash

\# 1. Сборка проекта

./scripts/build.sh



\# 2. Запуск Go сервера (в отдельном терминале)

cd go\_tcp\_server \&\& go run main.go



\# 3. Запуск Python клиента

cd python\_client \&\& python main.py



\# 4. Запуск тестов

go test ./go\_tcp\_server/...

pytest python\_client/

cargo test --manifest-path rust\_class\_lib/Cargo.toml



\# 5. Бенчмарк производительности

python python\_client/benchmark.py



Требования

Go 1.21+

Rust 1.70+

Python 3.8+

Maturin (pip install maturin)



Автор

Евстигнеев Фёдор Алексеевич, гр. 220032-11, Вариант 5

