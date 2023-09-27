def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))
print(tpl_sort([23, 43, 43, 32, 43, 55, 39, 12, 88, 32.23]))
print(tpl_sort([23, 43, 43, 32, 43, 55, 39, 12, 88, 32]))