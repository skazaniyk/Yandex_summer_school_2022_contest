def check_min_position(position):
    with open('input.txt', 'r') as f:
        min_id = -1
        idx = 0
        while idx != position:
            symbol = f.read(1)
            if symbol == ')':
                if min_id == -1:
                    min_id = idx
            if symbol == '(':
                min_id = -1

            idx += 1

        if min_id == -1:
            return position
        return min_id + 1


def find_index_to_delete():
    len_stack = 0
    element_of_stack = -1
    index_of_the_item_being_deleted = -1

    with open('input.txt', 'r') as f:
        idx = 1
        symbol = f.read(1)
        while symbol:
            if symbol == '(':
                if len_stack == 0:
                    element_of_stack = idx
                len_stack += 1

            if symbol == ')':
                if len_stack > 0:
                    len_stack -= 1
                else:
                    ## если уже удалили элемент, но нужно удалить ещё, то -1
                    if index_of_the_item_being_deleted != -1:
                        return -1

                    index_of_the_item_being_deleted = idx
            idx += 1
            symbol = f.read(1)

    ## если в стеке осталось больше одной открывающей скобки, то -1
    if len_stack > 1:
        return -1

    ## если в стеке один элемент
    if len_stack > 0:
        if index_of_the_item_being_deleted != -1:
            return -1
        else:
            return check_min_position(element_of_stack)

    if index_of_the_item_being_deleted != -1:
        return check_min_position(index_of_the_item_being_deleted)
    else:
        return -1

print(find_index_to_delete())
