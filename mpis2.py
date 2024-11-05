import random

# Определяем состояния и действия
states = ['open', 'close']
actions = ['включение сигнализации', 'выключение сигнализации', 'автозапуск двигателя']

# Таблица вероятностей
transition_table = {
    ('open', 'включение сигнализации'): ['open', 'close'],
    ('open', 'выключение сигнализации'): ['open', 'close'],
    ('open', 'автозапуск двигателя'): ['open', 'close'],
    ('close', 'включение сигнализации'): ['close', 'open'],
    ('close', 'выключение сигнализации'): ['close', 'open'],
    ('close', 'автозапуск двигателя'): ['close', 'open'],
}

# Вероятности перехода
probabilities = {
    ('open', 'включение сигнализации'): [0.9, 0.1],
    ('open', 'выключение сигнализации'): [0.8, 0.2],
    ('open', 'автозапуск двигателя'): [0.8, 0.2],
    ('close', 'включение сигнализации'): [0.8, 0.2],
    ('close', 'выключение сигнализации'): [0.5, 0.5],
    ('close', 'автозапуск двигателя'): [0.1, 0.9],
}

# Функция для выполнения перехода
def transition(current_state, action):
    if (current_state, action) in transition_table:
        next_states = transition_table[(current_state, action)]
        probs = probabilities[(current_state, action)]
        # Выбор следующего состояния с учетом вероятностей
        next_state = random.choices(next_states, weights=probs)[0]
        probability_of_transition = probs[next_states.index(next_state)]
        return next_state, probability_of_transition
    else:
        return current_state, 1.0  # если действие не определено, остаемся в текущем состоянии


# Основная функция
def main():
    print("Доступные состояния:")
    print("1. машина открыта (open)")
    print("2. машина закрыта (close)")

    state_input = input("Введите номер начального состояния (1 или 2): ").strip()

    if state_input not in ['1', '2']:
        print("Некорректное состояние! Используйте '1' для открытой или '2' для закрытой машины.")
        return

    current_state = states[int(state_input) - 1]

    print("\nДоступные действия:")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action}")

    while True:
        print(f"\nТекущее состояние: {current_state}")
        action_input = input("Введите номер действия (1, 2 или 3): ").strip()

        if action_input not in ['1', '2', '3']:
            print("Некорректное действие! Пожалуйста, выберите одно из доступных действий.")
            continue

        action_index = int(action_input) - 1
        action = actions[action_index]

        next_state, probability = transition(current_state, action)
        print(f'Действие: {action}, Следующее состояние: {next_state}, Вероятность перехода: {probability:.2f}')

        current_state = next_state  # обновляем текущее состояние

        continue_choice = input("Хотите продолжить? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Завершение работы автомата.")
            break

if __name__ == "__main__":
    main()
