# plf-walker

Claude Code skill для запуска онлайн-продуктов по методу Джеффа Уокера – **Product Launch Formula (PLF)**. Скилл превращает обычное «открытие продаж» в управляемое событие с pre-launch контентом, sideways sales letter и crescendo в финале.

## Что это

PLF Walker – универсальный методологический скилл, не привязанный к конкретному запуску. Его можно применять к запуску онлайн-курса, инфопродукта, коучинг-программы, SaaS с лимитированным доступом и любому другому продукту, где есть «событие открытия продаж».

Скилл даёт:
- Полную методологию 4 фаз PLF (Pre-Pre-Launch / Pre-Launch / Open Cart / Post-Launch)
- Структуру трёх PLC видео (Opportunity / Transformation / Ownership)
- Концепт Sideways Sales Letter
- 7 ментальных триггеров Уокера и карту их применения по фазам
- Day-by-day сценарий Open Cart 5-7 дней
- Готовые шаблоны постов и писем для каждой фазы
- 4 адаптации (Telegram, email-internal, seed, JV)
- Скрипт `plf-plan.sh` для генерации launch-таймлайна от даты Open Cart

## Структура скилла

```
plf-walker/
├── SKILL.md                          # main skill descriptor + workflow
├── README.md                         # этот файл
├── LICENSE                           # MIT
├── reference/
│   ├── PLF_OVERVIEW.md               # 4 фазы запуска
│   ├── PLC_VIDEOS.md                 # PLC1 / PLC2 / PLC3
│   ├── SIDEWAYS_SALES_LETTER.md      # концепт SSL
│   ├── MENTAL_TRIGGERS.md            # 7 триггеров + карта применения
│   ├── OPEN_CART.md                  # day-by-day Open Cart
│   └── BENCHMARKS.md                 # ожидаемые конверсии
├── templates/
│   ├── plc1-opportunity.md           # шаблон PLC1
│   ├── plc2-transformation.md        # шаблон PLC2
│   ├── plc3-ownership.md             # шаблон PLC3
│   ├── cart-open-sequence.md         # дни 0-6
│   ├── cart-close-crescendo.md       # финальные 24 часа
│   └── post-launch-onboarding.md     # после закрытия
├── adaptations/
│   ├── telegram-channel.md           # PLF в Telegram
│   ├── seed-launch.md                # маленькая аудитория / валидация
│   ├── internal-launch.md            # классика на свой лист
│   └── jv-launch.md                  # партнёрский запуск
└── scripts/
    └── plf-plan.sh                   # генератор launch-таймлайна
```

## Установка

### Как Claude Code skill

Склонировать в `~/.claude/skills/` или в `<project>/.claude/skills/`:

```bash
git clone https://github.com/qwwiwi/plf-walker.git ~/.claude/skills/plf-walker
```

Скилл триггерится автоматически на запросы про запуски, PLF, Walker, open cart и т.п.

### Как референс / документация

Можно использовать просто как knowledge base – читать reference/ и templates/ напрямую без Claude Code.

## Использование скрипта `plf-plan.sh`

```bash
# Internal launch с Open Cart 6 мая 2026, 7 дней Cart
./scripts/plf-plan.sh 2026-05-06

# Seed launch (компактный сценарий)
./scripts/plf-plan.sh 2026-05-06 --type seed

# JV launch (расширенный)
./scripts/plf-plan.sh 2026-05-06 --type jv --cart-days 10
```

Печатает все ключевые даты от Pre-Pre-Launch до Post-Launch.

## Workflow для использования через Claude Code

1. Открой Claude Code в проекте, где установлен скилл
2. Скажи: «Помоги спланировать запуск курса с Open Cart 6 мая»
3. Claude автоматически активирует plf-walker, спросит контекст (тип запуска, канал, лимит мест) и сгенерирует контент-план

Триггерные фразы:
- «запуск», «launch», «PLF», «Walker»
- «open cart», «pre-launch»
- «как разогревать перед запуском»
- «контент-план запуска»

## Принципы скилла

- **Универсальный** – не привязан к конкретному запуску, продукту, нише
- **Без дат** – все даты считаются от пользовательской даты Open Cart
- **Применимый** – не теория, а готовые шаблоны постов и писем
- **Адаптивный** – 4 варианта запуска под разные размеры аудитории и цели
- **Честный** – не учит фейковой срочности и манипуляциям

## Источники

- Jeff Walker, *Launch* (2014, обновлённое издание 2021)
- Jeff Walker, Product Launch Formula trainings (jeffwalker.com)
- Public reviews и разборы практиков

## Лицензия

MIT. См. LICENSE.

## Автор

Создан в ходе работы над запуском [Edge Lab](https://edgelab.su/) – образовательной платформы по AI-агентам.

Контрибьюции и pull-requests приветствуются.
