# Экономика информатизации: решения экзаменационных задач

## О репозитории

Здесь решения всех экзаменационных задач курса «Экономика информатизации» (лекции 1, 3–20; лекции №2 в материалах курса нет).
Каждое решение оформлено как аналитическая записка в Jupyter Notebook: постановка задачи, исходные данные, математическая модель,
расчёт на Python, графики, интерпретация, выводы и рекомендации.

**Студент:** Грошев Степан Сергеевич, группа БИ 5-1

## Структура репозитория

- `notebooks/`: Jupyter Notebook с решениями (уже выполнены, с результатами)
- `reports/`: отчёты в HTML и PDF
- `utils/`: общие функции расчётов (`calculations.py`: NPV, IRR, сроки окупаемости) и оформление графиков (`visualization.py`)
- `data/`: конфигурация задач и сводные исходные данные
- `docs/`: методические пояснения и глоссарий

## Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/LangeBoY577/economy-of-informatization-exam.git
   cd economy-of-informatization-exam
   ```
2. Создать виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```
3. Установить зависимости: `pip install -r requirements.txt`
4. Запустить Jupyter: `jupyter lab`, открыть папку `notebooks/` и выполнить ноутбук целиком (Run All).
   Ноутбуки запускаются из папки `notebooks/`, путь к `utils/` подключается сам.

Пересобрать HTML-отчёт: `jupyter nbconvert --to html --execute notebooks/<имя>.ipynb --output-dir reports`

## Список задач

| № | Лекция | Задача | Ключевой результат | Отчёт | Статус |
|---|---|---|---|---|---|
| 01 | №1 | [Оценка эффективности внедрения облачной CRM](notebooks/task_01_crm_efficiency.ipynb) | NPV ≈ 11,07 млн руб., окупаемость ≈ 4 мес., ROI ≈ 496 % | [HTML](reports/task_01_crm_efficiency_report.html) · [PDF](reports/task_01_crm_efficiency_report.pdf) | ✅ |
| 02 | №3 | [Критическая масса и ценность социальной сети](notebooks/task_02_critical_mass.ipynb) | КМ с учётом CAC недостижима (CAC·g = ARPU); NPV(36 мес.) ≈ −60 млн руб. | [HTML](reports/task_02_critical_mass_report.html) · [PDF](reports/task_02_critical_mass_report.pdf) | ✅ |
| 03 | №4 | [Выбор ценовой стратегии AI-сервиса](notebooks/task_03_pricing_strategy.ipynb) | Подписка: LTV 6 000 руб., лучший NPV; при базе ×10 NPV ≈ +148 млн руб. | [HTML](reports/task_03_pricing_strategy_report.html) · [PDF](reports/task_03_pricing_strategy_report.pdf) | ✅ |
| 04 | №5 | [Оптимизация рекламной нагрузки](notebooks/task_04_ad_load_optimization.ipynb) | Оптимум — 10 показов/день, прибыль ≈ 1 530 млн руб./мес. | [HTML](reports/task_04_ad_load_optimization_report.html) · [PDF](reports/task_04_ad_load_optimization_report.pdf) | ✅ |
| 05 | №6 | [Стоимость разработки по COCOMO II](notebooks/task_05_cocomo_ii.ipynb) | 133,4 чел.-мес., 13,9 мес., ≈ 44,0 млн руб. с НДС | [HTML](reports/task_05_cocomo_ii_report.html) · [PDF](reports/task_05_cocomo_ii_report.pdf) | ✅ |
| 06 | №7 | [TCO и выбор инфраструктурной стратегии](notebooks/task_06_tco_infrastructure.ipynb) | Облако: TCO(PV) ≈ 93,3 млн руб. против 176,2 (on-premise) | [HTML](reports/task_06_tco_infrastructure_report.html) · [PDF](reports/task_06_tco_infrastructure_report.pdf) | ✅ |
| 07 | №8 | [Эффективность ИС документооборота (NPV, IRR)](notebooks/task_07_npv_irr_roi.ipynb) | NPV ≈ −34,5 млн руб., IRR ≈ −20 %, ROI ≈ −51 % | [HTML](reports/task_07_npv_irr_roi_report.html) · [PDF](reports/task_07_npv_irr_roi_report.pdf) | ✅ |
| 08 | №9 | [Юнит-экономика сервиса доставки еды](notebooks/task_08_unit_economics.ipynb) | Маржа заказа −348 руб. (модель А) / +132 руб. (модель Б) | [HTML](reports/task_08_unit_economics_report.html) · [PDF](reports/task_08_unit_economics_report.pdf) | ✅ |
| 09 | №10 | [Выбор модели для AI-сервиса поддержки](notebooks/task_09_token_costs.ipynb) | Гибрид API + кеш: TCO(PV) ≈ $42,4 тыс. | [HTML](reports/task_09_token_costs_report.html) · [PDF](reports/task_09_token_costs_report.pdf) | ✅ |
| 10 | №11 | [Модель координации разработки госИС](notebooks/task_10_coordination_model.ipynb) | Гибрид: TCO ≈ 1 188 млн руб., лучший в 63 % вариантов весов | [HTML](reports/task_10_coordination_model_report.html) · [PDF](reports/task_10_coordination_model_report.pdf) | ✅ |
| 11 | №12 | [Готовность к цифровой трансформации](notebooks/task_11_digital_readiness.ipynb) | Индекс готовности ≈ 2,8 из 5 (средняя) | [HTML](reports/task_11_digital_readiness_report.html) · [PDF](reports/task_11_digital_readiness_report.pdf) | ✅ |
| 12 | №13 | [Стратегия защиты интеллектуальной собственности](notebooks/task_12_ip_strategy.ipynb) | Патент: NPV ≈ 8,1 млн руб.; open source ≈ 7,7 млн руб. | [HTML](reports/task_12_ip_strategy_report.html) · [PDF](reports/task_12_ip_strategy_report.pdf) | ✅ |
| 13 | №14 | [Риск переплаты на аукционе](notebooks/task_13_winners_curse.ipynb) | P(переплата | победа) ≈ 97 %, ожидаемая переплата ≈ 22 млн руб. | [HTML](reports/task_13_winners_curse_report.html) · [PDF](reports/task_13_winners_curse_report.pdf) | ✅ |
| 14 | №15 | [Ценность информации для проекта](notebooks/task_14_value_of_information.ipynb) | EVSI ≈ 6,8 млн руб. > 5 млн руб. → исследовать | [HTML](reports/task_14_value_of_information_report.html) · [PDF](reports/task_14_value_of_information_report.pdf) | ✅ |
| 15 | №16 | [Опцион на масштабирование платформы](notebooks/task_15_real_option.ipynb) | Опцион (Блэк–Шоулз) ≈ 79,3 млн руб., NPV ≈ 79,05 млн руб. | [HTML](reports/task_15_real_option_report.html) · [PDF](reports/task_15_real_option_report.pdf) | ✅ |
| 16 | №17 | [Оптимальная стратегия участия в аукционе](notebooks/task_16_auction_bidding.ipynb) | P* = 42,5 млн руб., Pr = 15 %, U* = 1,125 млн руб. | [HTML](reports/task_16_auction_bidding_report.html) · [PDF](reports/task_16_auction_bidding_report.pdf) | ✅ |
| 17 | №18 | [Подготовка и защита бюджета BI (обоснование)](notebooks/task_17_budget_bi_justification.ipynb) | ROI 50 %, NPV ≈ 6,9 млн руб., окупаемость 3,3 года | [HTML](reports/task_17_budget_bi_justification_report.html) · [PDF](reports/task_17_budget_bi_justification_report.pdf) | ✅ |
| 18 | №19 | [НМЦК по методике г. Москвы](notebooks/task_18_nmck_moscow.ipynb) | ОТр ≈ 86,6 чел.-мес., НМЦК ≈ 16,2 млн руб. без НДС | [HTML](reports/task_18_nmck_moscow_report.html) · [PDF](reports/task_18_nmck_moscow_report.pdf) | ✅ |
| 19 | №20 | [Защита бюджета ИТ-проекта (итоговая)](notebooks/task_19_budget_defense.ipynb) | NPV ≈ 6,9 млн руб., DPP ≈ 4,3 года, P(NPV<0) ≈ 44 % | [HTML](reports/task_19_budget_defense_report.html) · [PDF](reports/task_19_budget_defense_report.pdf) | ✅ |

Допущения, принятые там, где условие неполное, перечислены в каждом ноутбуке. Общий подход описан в
[docs/methodology.md](docs/methodology.md).

## Авторы

Студент Грошев Степан Сергеевич, группа БИ 5-1
