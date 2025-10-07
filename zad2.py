def matrix_multiply(A, B):
    # Проверяем совместимость матриц
    if len(A[0]) != len(B):
        raise ValueError("Количество столбцов матрицы A должно равняться количеству строк матрицы B")

    # Создаем результирующую матрицу с нулями
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Вычисляем произведение матриц
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


# Пример использования
if __name__ == "__main__":
    # Матрица A 2x3
    A = [
        [10, 2, 3],
        [4, 5, 6]
    ]

    # Матрица B 3x2
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    try:
        result = matrix_multiply(A, B)
        print("Результат умножения:")
        for row in result:
            print(row)
    except ValueError as e:
        print(f"Ошибка: {e}")