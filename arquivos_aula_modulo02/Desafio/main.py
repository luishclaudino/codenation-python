import abc


# Classe do Departamento
class Department:
    # Instanciador da classe Departamento
    def __init__(self, name, code):
        self.name = name
        self.code = code


# Classe de Empregado
# ABCMeta para sinalizar que é uma classe abstrata
class Employee(metaclass=abc.ABCMeta):

    # Inicializa o Empregado
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.work_hours = 8

    # "Sinalizador" que é um método abstrato e deve ser implementada
    # por subclasses.
    # Com isso ele já não deixa instanciar essa classe diretamente
    @abc.abstractmethod
    def calc_bonus(self):
        pass

    @abc.abstractmethod
    def get_hours(self):
        pass


# Classe de Gerente
class Manager(Employee):

    # Inicializa o Gerente
    def __init__(self, code, name,
                 salary, department=Department('managers', 1)):
        super().__init__(code, name, salary)
        self.__department = department

    # Calcula o bônus baseado no salário
    def calc_bonus(self):
        return self.salary * 0.15

    # Implementa o método de retornar horas trabalhadas
    def get_hours(self):
        return self.work_hours

    # Pega o nome do departamento
    def get_departament(self):
        return self.__department.name

    # Modifica o nome do departamento
    def set_departament(self, name):
        self.__department.name = name


# Classe do Vendedores
class Seller(Manager):

    # Inicializa o Vendedor
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    # Retorna o número de vendas
    def get_sales(self):
        return self.__sales

    # Adiciona um certo número de vendas do vendedor
    def put_sales(self, sales):
        self.__sales += sales

    # Calcula o bônus do vendedor de acordo com o número de vendas
    def calc_bonus(self):
        return self.__sales * 0.15
