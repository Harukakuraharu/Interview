from model import Stack

def get_balance(value: str) -> str:
    dict_elements = dict([('()'), ('[]'), ('{}')])
    stack = Stack()
    if len(value) % 2 != 0:
        return 'Несбалансированно'
    else:
        for el in value:
            if el in dict_elements:
                stack.push(el)
            elif stack.size() != 0 and dict_elements.get(stack.peek()) == el:
                stack.pop()
        if stack.is_empty():
            return 'Сбалансированно'
        else:
            return 'Несбалансированно'

if __name__ == "__main__":
    assert get_balance('(((([{}]))))') == 'Сбалансированно'
    assert get_balance('[([])((([[[]]])))]{()}') == 'Сбалансированно'
    assert get_balance('{{[()]}}') == 'Сбалансированно'
    assert get_balance('}{}') == 'Несбалансированно'
    assert get_balance('{{[(])]}}') == 'Несбалансированно'
    assert get_balance('[[{())}]') == 'Несбалансированно'
  
 


    
