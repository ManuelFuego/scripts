# Работа с файлами
## FIND
постраничное листание c командой less 
```
find /var/log | less 
```
поиск по имени файла (все файлы с расширением pdf)
```
find . -name "*.pdf" 
find . -name "f*.pdf"
```
поиск по глубине 
```
find . -maxdepth 1 -name "*.json"
```
поиск файлов , директорий
```
find . -type f -name "file_name"
find . -type d -name "directory_name"
```
исключение из поиска (-prune)
```
find . -type d -path ./dir -prune -o -name "*py" -print
```
использование ИЛИ  в поиске (-o)
```
find . -type f -name "cars*.json" -o type f -name "*.txt"
```
поиск без учета регистра (-iname) 
```
find . -iname "caRs.txt"
```
поиск по дате изменения (-atime X время последнего доступа) (-mtime X время изменения файла) 
```
find . -type f -atime 1
```

поиск по размеру файла (-a and поиск в диапазоне)
```
find . -type f -size 25M  | head -3
find . -type f -size -25M | tail -2
find . -tipe f -size 400k
find . -type f -size +25k
find . -type f -size -25k -a -type f -size 100k
```
поиск файла в каталогах 
```
find ./ -name "file_name"
```
## GREP 
поиск в файле
```
grep "hi dude" file.txt
```
нерегистрозависимый поиск c указанием номера строки 
```
grep -in "hi dude" file.txt
```

поиск по в директории 
```
grep -iwn 'hi dude' ./ 
```
поиск в директории и вложенным директориям
```
grep -iwnr 'hi dude' ./ 
```
grep в качестве фильтра (поиск по регуляркам )
```
ls -la | grep "file.*"
grep - P "\d{3}-d{2}-\d{2}" filename
```
