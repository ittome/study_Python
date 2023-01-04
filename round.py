import decimal;
import math;

context = decimal.getcontext();
context.rounding = decimal.ROUND_HALF_EVEN

print(round(decimal.Decimal(0.5),0));
print(round(decimal.Decimal(1.5),0));
print(round(decimal.Decimal(2.5),0));

print(round(0.5));
print(round(1.5));
print(round(2.5));


print(math.floor(0.5))     #0
print(math.floor(-0.5))    #-1
print(math.trunc(-0.5))   #0
print(math.floor(-0.5))   #-1

print(math.ceil(0.5))     #1