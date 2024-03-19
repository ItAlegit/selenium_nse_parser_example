# SeleniumNseParserExample
Automation example using Selenium and BeautifulSoup library.
Algorithm:
1) go to the website nseindia.com;
2) pointing to "MARKET DATA";
3) click on "Pre-Open Market";
4) parsing the "SYMBOL" and "FINAL" fields from the table;
5) go to the main page of the site;
6) scroll to “MOST ACTIVE” and click on the element;
7) scroll to “View All” and click on the element;
8) select “NIFTY MIDCAP 50” in the selector;
9) scroll to the end of the table.
If the error "err_http2_protocol_error" appears, you need to uncomment all "#browser.delete_all_cookies()".


Пример автоматизации с помощью библиотеки Selenium и BeautifulSoup.
Алгоритм работы:
1) переход на сайт nseindia.com;
2) наведение на "MARKET DATA";
3) клик по "Pre-Open Market";
4) парсинг полей "SYMBOL" и "FINAL" из таблицы;
5) переход на главную страницу сайта;
6) скролл до "MOST ACTIVE" и клик по элементу;
7) скролл до "View All" и клик по элементу;
8) в селекторе выбрать "NIFTY MIDCAP 50";
9) пролистать до конца таблицы.
Если появляется ошибка "err_http2_protocol_error" - нужно раскоментить все "#browser.delete_all_cookies()".