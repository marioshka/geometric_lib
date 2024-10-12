
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
>Когда программа запросит ввод, введите название фигуры

3. Enter the function: Area or Perimeter.
>Укажите функцию, которую хотите рассчитать

4. Enter figure sizes. Radius for circle, one side for square.
>Предоставьте необходимые размеры:

• Для Круга введите радиус.

• Для Квадрата введите длину стороны.
5. Get the answer!

- # Math formulas

>Математические формулы для вычисления площади и периметра различных геометрических фигур, таких как круг, квадрат и прямоугольник

## Area 

>Формулы для нахождения площади

### Circle: S = πR² 

 > Формула для нахождения площади круга с использованием радиуса R и числа pi 
  Параметры: pi-число пи и R-радиус окружности
  Пример:

 **Принимает число 2, возвращает квадрат 2 умноженное на число pi**

 ```
 area = calculatecirclearea(2);
 ```
> При таких условиях площадь будет равнна 4*pi;

### Rectangle: S = ab
> Формула для нахождения площади прямоугольника с использованием двух его сторон a и b
  Параметры: а и b -стороны прямоугольника
  Пример:

** Принимает числа 2 и 3, возвращает произведение 2*3**

```
area = calculatrectanglearea(3,2);
 ```
> При таких условиях площадь будет равнна 3*2=6;

### Square: S = a²
> Формула для нахождения площади квадрата с использованием его стороны a
 Параметры: а-сторона квадрата
 Пример:


**Принимает число 3, возвращает квадрат 3** 
 
 ```
 area = calculatesquarearea(3)
 ```
> При таких условиях площадь будет равнна 3*3=9;

### Triangle: S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter
> Формула для нахождения площади треугольника по формуле Герона с использованием его сторон a,b,c и его поупериметра p
 Параметры: а,b,c-стороны треугольника, p-полупериметр треугольника ((a+b+c)/2)
 Пример:


**Принимает числа 5,3,4,6 и возвращает площадь треугольника по формуле герона**
 ```
 area = calculatetrianglearea(5,3,4,6)
 ```
> При таких условиях площадь будет равнна sqrt(6*(6-5) * (6-3) * (6-4))=6;

## Perimeter

 >Формулы для нахождения периметра

### Circle: P = 2πR
 >Формулы для нахождения длины окружности круга с использованием его радиуса и числа pi
 Параметры: pi-число пи и R-радиус окружности
 Пример:

 **Принимает число 2, возвращает произведение 2 на 2**
 ```
 perimeter = calculatecircleperimeter(2)
 ```
 >При таких условиях площадь будет равнна 4*pi;

### Rectangle: P = 2a + 2b

> Формулы для нахождения периметра прямоугольника с использованием двух его сторон
 Параметры: а и b -стороны прямоугольника
  Пример:


 **Принимает числа 2 и 3 и возвращает произведение 2 на 3**
 ```
 perimeter = calculaterectangleperimeter(2, 3)
 ```
 >При таких условиях площадь будет равнна (3+2)*2*=10;

 ### Square: P = 4a
 >Формулы для нахождения периметра квадрата с использованием его тороны а
 Параметры: а-сторона квадрата
 Пример:


 Принимает число 3 и возвращает квадрат 3
 ```
 perimeter = calculatesquareperimeter(3)
 ```

 >При таких условиях площадь будет равнна 3*4=12;
 ### Triangle: P = a + b + c
 >Формулы для нахождения периметра треугольника с использованием его сторон а,b,c
 Параметры: а,b,c
 Пример:


 **Принимает числа 3, 4, 5 и возвращает сумму**
 '''
 ```
 perimeter = calculatetriangleperimeter(3,4,5)
 ```

 >При таких условиях периметр будет равнна 3 + 4 + 5 = 12;

 ### История коммитов и их изменений:

 1)commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

2)commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

3)commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300

4)commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (HEAD -> documentation, origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

5)commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

6)commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

    L-04: Doc updated for triangle

7)commit d080c7888b81955bad2ed78d58ad910526b5132a
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:48:39 2021 +0300


