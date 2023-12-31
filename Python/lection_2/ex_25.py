import math  #матемтические функции, константы
import decimal #высокая точность вычисления
import fractions #работа с дробями

print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')
print(dir(math))
print(help(math.gcd))

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

decimal.getcontext().prec = 120 #задали точность, кол-во знаков
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)