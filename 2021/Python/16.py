import fileinput
from typing import Optional


hex_to_bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def main(input_path: Optional[str] = None):
    """
    >>> from _pytest.monkeypatch import MonkeyPatch
    >>> with MonkeyPatch.context() as monkeypatch:
    ...     monkeypatch.setattr(fileinput, "input", lambda x: iter(["8A004A801A8002F478"]))
    ...     main()
    16
    >>> main('../16.in')
    """
    transmission = next(fileinput.input(input_path)).strip()
    transmission_bits = "".join(hex_to_bits[x] for x in transmission)
    decode

def decode(bits: str):
    version = int(bits[:3], base=2)
    type_id = int(bits[3:6], base=2)
    rest = bits[6:]
    if type_id == 4: # literal value
        number_bits = ''
        i = 0
        while True:
            is_last = rest[i] == '0'
            number_bits += rest[i+1:i+5]
            i += 5
            if is_last:
                break
        number = int(number_bits, base=2)
        return {
            'version': version,
            'type': 'literal',
            'number': number
        }
    else: # operator packet
        length_type_id = rest[0]
        if length_type_id == '0':
            length_of_subpackets_in_bits = int(rest[1:16], base=2)
        else:
            number_of_subpackets_contained = int(rest[1:12], base=2)



