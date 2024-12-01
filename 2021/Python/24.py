import fileinput
from typing import List, Optional, Tuple, Union
from types import FunctionType


def main(input_path: Optional[str] = None):
    # """
    # >>> main('../16.in')
    # """
    instructions = [line.strip().split(" ") for line in fileinput.input(input_path)]
    func = instructions_to_func(instructions)
    number = 99999999999999
    while True:
        snumber = str(number)
        if '0' in snumber:
            number -= 1
            continue
        print(number, end = ' | ')
        ret = func(snumber)
        print(ret['z'])
        if ret['z'] == 0:
            break
        number -= 1

# do the calculations only one time for each prefix and then recurse(?)


def instructions_to_func(
    instructions: List[Union[Tuple[str, str], Tuple[str, str, str]]]
):
    python_code_lines = ["def program(vars, input_iter):"]
    for instruction in instructions:
        ins_type = instruction[0]
        if ins_type == "inp":
            python_code_lines.append(" vars['w'] = int(next(input_iter))")
            continue

        p1, p2 = instruction[1:]
        p1 = f"vars['{p1}']"
        if not p2.lstrip('-').isdigit():
            p2 = f"vars['{p2}']"

        if ins_type == "add":
            python_code_lines.append(f" {p1} += {p2}")
            continue
        if ins_type == "mul":
            python_code_lines.append(f" {p1} *= {p2}")
            continue
        if ins_type == "div":
            python_code_lines.append(f" {p1} = int({p1}/{p2})")
            continue
        if ins_type == "mod":
            python_code_lines.append(f" {p1} %= {p2}")
            continue
        if ins_type == "eql":
            python_code_lines.append(f" {p1} = int({p1}=={p2})")
            continue

    python_code = "\n".join(python_code_lines)
    compiled_code = compile(python_code, "<string>", "exec")

    def call_func(input_number: str):
        assert len(input_number) == 14
        variables = {"w": 0, "x": 0, "y": 0, "z": 0}
        program_func = FunctionType(
            compiled_code.co_consts[0], {}, compiled_code.co_names[0]
        )
        program_func(variables, iter(input_number))
        return variables

    return call_func


if __name__ == "__main__":
    main()
