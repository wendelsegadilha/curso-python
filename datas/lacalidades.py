import calendar
import locale

#locale padrão do sistema operacional
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
print(calendar.calendar(2023))