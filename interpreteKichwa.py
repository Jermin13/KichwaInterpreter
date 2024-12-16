class KichwaInterpreter:
    def __init__(self):
        self.variables = {}
        self.commands = {
            'LLULLANA': self.cmd_asignar,  # Asignar
            'YAPANA': lambda args: self.cmd_calcular(args, op="+"),  # Suma
            'ANCHUCHINA': lambda args: self.cmd_calcular(args, op="-"),  # Resta
            'RIKUNA': self.cmd_print  # Imprimir
        }

    def get_valor(self, token):
        """Obtiene el valor de un token (número o variable)."""
        if token.isdigit():
            return int(token)
        return self.variables.get(token, 0)

    def cmd_asignar(self, args):
        """LLULLANA - Asigna un valor a una variable."""
        if len(args) < 2:
            print("Error: LLULLANA necesita una variable y un valor.")
            return
        self.variables[args[0]] = self.get_valor(args[1])

    def cmd_calcular(self, args, op):
        """Realiza operaciones matemáticas (suma/resta)."""
        if len(args) < 3:
            print(f"Error: La operación {op} necesita dos valores y una variable de resultado.")
            return
        val1 = self.get_valor(args[0])
        val2 = self.get_valor(args[1])
        self.variables[args[2]] = val1 + val2 if op == "+" else val1 - val2

    def cmd_print(self, args):
        """RIKUNA - Imprime el valor de una variable."""
        if not args:
            print("Error: RIKUNA necesita un argumento.")
            return
        result = self.get_valor(args[0])
        
        # En Kichwa
        if args[0] == 'SUMA':
            print(f"Rikchana kawsaykuna: {result}")  # "Resultado de la suma"
        elif args[0] == 'RESTA':
            print(f"Rikchana chinkana: {result}")  # "Resultado de la resta"
        else:
            print(f"Ñukaka {args[0]}: {result}")  # "Valor de (nombre de la variable)"

    def execute(self, program):
        """Ejecuta el programa línea por línea."""
        for line in program.strip().split('\n'):
            tokens = line.split()
            if not tokens:
                continue
            command, args = tokens[0], tokens[1:]
            action = self.commands.get(command)
            if action:
                action(args)
            else:
                print(f"Comando mana riksina: {command}")  # "Comando no reconocido"


# Ejemplo de uso
if __name__ == "__main__":
    interpreter = KichwaInterpreter()
    program = """
    LLULLANA A 10
    LLULLANA B 5
    YAPANA A B SUMA
    RIKUNA SUMA
    ANCHUCHINA A B RESTA
    RIKUNA RESTA
    """
    interpreter.execute(program)


if __name__ == "__main__":
    interpreter == KichwaInterpreter()
    program = """
    LLULLANA C 20
    LLULLANA D 3
    YAPANA C D SUMA
    RIKUNA SUMA
    ANCHUCHINA C D RESTA
    RIKUNA RESTA
    """
    interpreter.execute(program)