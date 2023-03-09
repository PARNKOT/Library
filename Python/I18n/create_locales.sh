
# Создаем *.pot файлы из исходного кода (t - template)
xgettext -L Python -o locales/base.pot $1

# Копируем *.pot файлы в соответствующие папки по языкам (ru, ...)
cp locales/base.pot locales/ru/LC_MESSAGES/base_extra.po

# Заменяем CHARSET на UTF-8
sed -i 's/CHARSET/UTF-8/' locales/ru/LC_MESSAGES/base_extra.po

# Сливаем *.po файлы в один файл
msgcat -o locales/ru/LC_MESSAGES/base.po locales/ru/LC_MESSAGES/base.po locales/ru/LC_MESSAGES/base_extra.po

# Создаем бинарные файлы *.mo из файлов *.po
# msgfmt -o locales/ru/LC_MESSAGES/base.mo locales/ru/LC_MESSAGES/base.po
