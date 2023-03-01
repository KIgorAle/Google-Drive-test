# Google-Drive-test

Язык: Python 3

Понадобятся:
1) IDE Python 3.7 (32-bit)
2) Pip package management tool
3) Google аккаунт с включённым Google Drive

Инструкция:
1) Инсталлируем Python 3.7 (32-bit), отметив при установке пункт "Add Python 3.7 to PATH" дабы интегрировать IDE с командной строкой
2) Включаем Drive API, создаём Cloud Platform проект, загружаем клиентскую конфигурацию и сохраняем файл credentials.json в директорию, где располагается утилита
    Проще всего это сделать по ссылке: https://developers.google.com/drive/api/v3/quickstart/python , нажав кнопку "ENABLE THE DRIVE API" в 1 шаге, а затем "ENABLE THE DRIVE API"  
3) Устанавливаем Google Client Library вписав и подтвердив в командной строке следующее: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
4) Находясь в директории с утилитой вводим в командной строке требуемое, например:
testtool.py put 43223.jpg Unnamed.jpg
   - закачать файл Unnamed.jpg из текущего каталога в корневую папку Вашего Google Drive под именем 43223.jpg
или:
testtool.py get 1O3AbwakZ8SWuEkrBU6xvwgDkTyqX3YCR "C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0\8.jpg"
   - скачать файл с ID "1O3AbwakZ8SWuEkrBU6xvwgDkTyqX3YCR" в директорию "C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0\" под именем "8.jpg"

Общий вид вызова утилиты:
Загрузка:  
1) testtool.py put имя_файла_сервера имя_файла_локально
2) testtool.py put имя_файла_сервера "Абсолютный путь и имя файла_локально"
Скачивание: 
1) testtool.py get ID_файла_сервера имя_файла_локально
2) testtool.py get ID_файла_сервера "Абсолютный путь и имя файла_локально"

Примечания:
1) При первом запуске программы автоматически откроется окно подтверждения доступа, где нужно выбрать требуемый аккаунт и подтвердить полномочия. После этого в рабочей папке появится файл token.pickle и при последующих запусках подтверждение требоваться не будет.
2) Использовать можно как и просто имя файла, так и абсолютный путь к файлу.
3) Для скачивания файла требуется вписать его ID, а не имя, т.к. на Google Drive в одной и той же директории могут находиться несколько файлов с одинаковым именем, но разным ID.
3*) В процессе написания этого пояснения понял, что с папками на Google Drive дела обстоят так же как и с файлами, т.е. могут быть несколько папок с одинаковым именем, но отличающимися ID, соответственно загрузки файла в Google Drive по абсолютному пути (с папками и подпапками) реализовано не оказалось (думал само по себе будет вместе с вводом имени работать, как при скачивании на локальный диск по абсолютному пути), бегло придумать/нагуглить как это исправить не смог, отправляю как есть, если всё таки это нужно/можно как-то доработать, сообщите.
4) В конце работы программы выводится ID закаченного файла или путь к скаченному файлу.

Пример работа программы (лог командной строки):

Microsoft Windows [Version 6.3.9600]
(c) Корпорация Майкрософт (Microsoft Corporation), 2013. Все права защищены.

C:\Users\Igor>cd C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0

C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0>testtool.py put 43223.jpg Unnamed.jpg
Please visit this URL to authorize this application: https://accounts.google.com
/o/oauth2/auth?response_type=code&client_id=ДЛИИИИИИИИИИИИИИИИИННАЯ_ССЫЛКА_&access_type=offline
Upload Complete, file ID: 1wYM-xa04-Cl9a15f8YvB9aBc1-gqPjfE

C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0>testtool.py get 1O3AbwakZ8SWuEkrBU6xvwgDkTyqX3YCR "C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0\8.jpg"
Download Complete, file path: C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0\8.jpg

C:\Files\Data\Accounts\programmer\Proga\Python\MyUtilitie\7.0>
