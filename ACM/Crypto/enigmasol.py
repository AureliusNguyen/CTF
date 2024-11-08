from enigma.machine import EnigmaMachine
from itertools import product, permutations

# Enigma KeyBrute - Full Brute Force
print("Enigma KeyBrute - Full Brute Force")

# Get user input for ciphertext and crib
ciphertext_user = input("[*] Enter cipher text:\n").strip().upper()
crib = input("[*] Enter crib (The longer the crib, the better the results):\n").upper()

# Define rotors and reflector options
print("[*] Starting brute force...")
available_rotors = ["I", "II", "III", "IV", "V"]  # Available rotors
reflectors = ["B", "C"]  # Standard reflectors in Enigma machines

# Set the specific plugboard settings as provided
plugboard_settings = "AS DT UQ EW GJ OF XZ BN PY VK"

# Track unique matches to avoid redundancy
unique_matches = set()

# Iterate through all possible rotor combinations, reflectors, and starting positions
for rotor_perm in permutations(
    available_rotors, 3
):  # Choose 3 rotors in a specific order
    for reflector in reflectors:
        for ring_settings in product(
            range(0, 26), repeat=3
        ):  # Ring settings from 0 to 25
            # Initialize the Enigma machine with the current configuration
            machine = EnigmaMachine.from_key_sheet(
                rotors=" ".join(rotor_perm),
                reflector=reflector,
                ring_settings=list(ring_settings),
                plugboard_settings=plugboard_settings,
            )

            # Try all starting rotor positions
            for starting_position in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=3):
                machine.set_display("".join(starting_position))

                # Attempt to decrypt the ciphertext
                plaintext = machine.process_text(ciphertext_user)

                # Check if the crib appears at the start of the decrypted text
                if plaintext.startswith(crib):
                    config = (
                        rotor_perm,
                        reflector,
                        ring_settings,
                        starting_position,
                        plaintext[: len(crib)],
                    )
                    # Only add and display if the configuration is unique
                    if config not in unique_matches:
                        unique_matches.add(config)
                        print("[*] MATCH FOUND:")
                        print(f"Rotor order: {' '.join(rotor_perm)}")
                        print(f"Reflector: {reflector}")
                        print(f"Ring settings: {ring_settings}")
                        print(f"Starting position: {''.join(starting_position)}")
                        print(f"Plugboard settings: {plugboard_settings}")
                        print(f"Plaintext: {plaintext}")
                        print("-" * 40)  # Divider for clarity between matches

if not unique_matches:
    print("No matches found.")
else:
    print(f"Total unique matches found: {len(unique_matches)}")
