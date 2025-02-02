from commands import *
c=''
p=Patient()
d=Doctor()
a=Appointment()
m=MedicalRecord()
t=Test()
l=Laboratory()
# создание списка из объектов для возможности их изменения
# (меняться будут элементы списка) в функции,
# так как list - мутабельный класс
objects=[p,d,a,m,t,l]
# создание переменных, проверяющих инициализацию объектов перед
# использованием других методов
pa=da=aa=ma=ta=la=False
access=[pa,da,aa,ma,ta,la]
while c!='e':# вызывать функцию, запрашивающую команды, пока не введена команда завершения программы
    c=commands(objects, access)
