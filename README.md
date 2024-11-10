# Игра Тетрис

## * Правила игры:

* Используйте стрелки на клавиатуре для управления фигурами:
* Влево: стрелка влево
* Вправо: стрелка вправо
* Вниз: стрелка вниз
* Поворот: стрелка вверх
* Ваша задача — манипулировать фигурами, чтобы они заполнили горизонтальные линии. Полная линия исчезнет, и вы получаете очки. Игра заканчивается, когда фигуры достигают вершины игрового поля.


###   Краткое описание кода

#### Константы:
* Определяют основные параметры игры, такие как ширина, высота и размер блока.
* Цвета и фигуры: Содержат предопределенные значения и формы для тетрис-фигур.

#### Классы:

* Block: Описывает отдельную фигуру со свойствами и методами для ее поворота.
* Board: Управляет игровым полем, проверкой валидности позиции и очисткой линий.
* TetrisGame: Управляет всей логикой игры, включая обработку событий и отрисовку.
Методmove_block : обрабатывает перемещение блока влево или вправо.

#### Методы:

* Методdrop_block : Возникает падение текущего блока вниз. Если блок не может двигаться ниже, он вставляется на игровое поле, затем очищаются заполненные линии.
* Методrotate_block : поворачивает текущий блок, и если поворот приводит к столкновению, он отменяется.
* Методdraw : отрисовывает игровое поле и настоящий падающий блок.