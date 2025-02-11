# Завдання 4. Візуалізація піраміди

У цьому прикладі представлено візуалізацію бінарної купи з обов'язковими атрибутами кожного вузла. Код написаний на Python та використовує бібліотеки `networkx` та `matplotlib` для створення та відображення графів.

## Клас Node

Клас `Node` визначає вузол бінарного дерева з наступними обов'язковими атрибутами:
- `left`: лівий нащадок вузла;
- `right`: правий нащадок вузла;
- `val`: значення вузла;
- `color`: колір вузла (за замовчуванням - 'skyblue');
- `id`: унікальний ідентифікатор вузла;
- `parent`: батьківський вузол.

## Функція add_edges

Функція `add_edges` додає ребра та вузли до графа `networkx` на основі бінарного дерева.

## Функція draw_heap

Функція `draw_heap` візуалізує бінарну купу за допомогою `networkx` та `matplotlib`. Кожен вузол представлений кольоровим прямокутником з відповідним значенням.

## Функція heap_insert

Функція `heap_insert` вставляє новий елемент у бінарну купу та перебудовує купу.

## Функція heapify_up

Функція `heapify_up` перебудовує купу вгору після вставки нового елемента.

## Використання

Для використання коду створюється бінарне дерево та відображується його графічне представлення.

## Використання

1. Запустіть програму `Task4.py`.
2. За допомогою функції `heap_insert()` вставте елементи у бінарну купу.
3. Функція `draw_heap()` автоматично візуалізує створену купу.

## Залежності

- `networkx`
- `matplotlib`

Перед використанням переконайтеся, що ви маєте встановлені відповідні бібліотеки. Їх можна встановити, використовуючи `pip`:

