# Основні структури даних

## Завдання 1

Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу сервісного центру.

### Приклад роботи

```
Request 1 added to queue.
Request 1 processed.
Request 2 added to queue.
Request 3 added to queue.
Request 2 processed.
Request 4 added to queue.
Request 3 processed.
Request 4 processed.
Queue is empty. Waiting for new requests.
Request 5 added to queue.
Request 5 processed.
Queue is empty. Waiting for new requests.
```

## Завдання 2

Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.

### Приклад роботи

```
Enter a string: Я несу гусеня
This is a palindrome!

Enter a string: Я несу цуценя
This is not a palindrome.
```