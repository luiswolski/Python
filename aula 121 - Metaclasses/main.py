class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classes' in namespace:
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classes']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_casses = 'Valor A'


class B(A):
    attr_casses = 'Valor B'


class C(B):
    attr_casses = 'Valor C'
    

c = C()
print(c.attr_casses)
