import argparse

class Machine:
    def __init__(self, states, current):
        self.states = states
        self.current = current
        self.tape = ["#"]
        self.index = 0
        self.null = "#"

    def __str__(self):
        temp = ""
        for i in self.states:
            temp += "{}".format(self.states[i])
        return temp

    def run(self, input_string):
        self.tape = list(input_string)
        print("".join(self.tape))
        print(" " * self.index + "^")
        while True:
            char = self.tape[self.index]
            trans = self.current.transit(char)
            print(trans)
            # Switch state
            self.current = trans.switch
            # Write content
            if self.index in range(0, len(self.tape)):
                self.tape[self.index] = trans.write
            # Move on tape
            if trans.move == ">":
                self.index += 1
            elif trans.move == "<":
                self.index -= 1
            else:
                raise Exception
            if self.index >= len(self.tape):
                self.tape.append(self.null)
            elif self.index < 0:
                self.tape = [self.null] + self.tape
            print("".join(self.tape))
            print(" " * self.index + "^")
            if self.current.accepting:
                print("ACCEPTED")
                return

                
class State:
    def __init__(self, name, accepting):
        self.name = name
        self.transitions = {}
        self.accepting = accepting

    def add_transition(self, character, transition):
        self.transitions[character] = transition

    def transit(self, character):
        return self.transitions[character]

    def __str__(self):
        temp = ""
        for i in self.transitions:
            temp += "|{}: {}|".format(i, self.transitions[i])
        if self.accepting:
            return "_{}\n   {}\n".format(self.name, temp)
        else:
            return " {}\n   {}\n".format(self.name, temp)

class Transition:
    def __init__(self, switch, write, move):
        self.switch = switch
        self.write = write
        self.move = move

    def __str__(self):
        return "{} {} {}".format(self.switch.name, self.write, self.move)

def get_parser():
    parser = argparse.ArgumentParser("Turing's machine emulator")
    parser.add_argument("input_file")
    parser.add_argument("input")

    return parser

def get_machine(filename):
     with open(filename, "r") as mach_file:
        start_state = mach_file.readline().strip().split()[0]
        accepting_states = mach_file.readline().strip().split()
        mach_file.readline()

        transitions = {}
        states = {}
        for line in mach_file.readlines():
            data = line.strip().split()
            state_name = data[0]
            character = data[1]
            dest_state_name = data[3]
            write = data[4]
            move = data[5]

            if state_name not in states.keys():
                state = State(state_name, state_name in accepting_states)
                states[state_name] = state

            if dest_state_name not in states.keys():
                dest_state = State(dest_state_name, dest_state_name in accepting_states)
                states[dest_state_name] = dest_state

            transition = Transition(states[dest_state_name], write, move)
            states[state_name].add_transition(character, transition)

        machine = Machine(states, states[start_state])
        return machine

def main():
    parser = get_parser()

    args = parser.parse_args()

    machine = get_machine(args.input_file)

    print(machine)
    
    machine.run(args.input)
    
if __name__ == "__main__":
    main()
