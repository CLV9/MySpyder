#  MySpyder
Назначение: парсинг + поиск и ранжирование новостей по запросам на сайте [gazeta.ru](https://www.gazeta.ru/news/)

# Были использованы библиотеки:
  - Scrapy для парсинга данных с сайта
  - Elastic Search для поиска и ранжирования запросов
 
# Инструкция по запуску Elastic Search:
  - Скачать серверную часть ElasticSearch по [ссылке](https://www.elastic.co/downloads/elasticsearch) и запустить файл `elasticsearch.bat`
  - Указать путь к распаршенным данным в `app_config.py`
  - Запустить файл `elastic_search.py`
 
 ![MySpyder Launch](https://sun9-30.userapi.com/impf/ejrn5OM4pSGaEsqoi-X_JpBt9sqf-4F1SRnq4A/QcTsMIh_aWs.jpg?size=814x834&quality=96&proxy=1&sign=2d53edea4ddc35db338f1923e49431d3&type=album "Пример запуска программы")
  
# Парсинг данных с помощью Scrapy:
  - Для запуска парсера запустите скрипт `crawl_start.py`
  
# Метрика качества ранжирования NDCG:
  - В файле `NDCG.xlsx` находится расчёт метрики NDCG ([Ссылка](https://docs.google.com/spreadsheets/d/1utjAxQciItuYhGKDyZDP_PTrtemvDA-jP66mVO3fzc8/edit?usp=sharing) на Google Sheets)
