# Вернуть кортеж (минимум, максимум). Если список пуст — ValueError
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список пуст")

    minimum = min(nums)
    maximum = max(nums)
    return (minimum, maximum)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums)
    return sorted_nums

def flatten(mat: list[list | tuple]) -> list:
    result_list = []
    for element in mat:
        if type(element) == list or type(element) == tuple:
            for sub_element in element:
                result_list.append(sub_element)
        elif type(element) == str:
            return TypeError("строка не строка строк матрицы")

        else:
            result_list.append(element)

    return result_list