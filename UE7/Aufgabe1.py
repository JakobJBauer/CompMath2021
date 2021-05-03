from typing import List


def get_filtered_string(s_in: str, s_find: str, s_replace: str) -> str:
    return ' '.join([text.replace(s_find, s_replace) for text in s_in.split(' ')])


def f(s: str, capitalize: bool = False) -> List[str]:
    return s.strip().upper().split(' ') if capitalize else s.strip().split(' ')


print(get_filtered_string('replace my name is JJ. replace I am 19', 'replace', 'Hello'))
print(f("    Put me in a list "))
print(f("    Put me in a list i said", True))
