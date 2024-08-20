import itertools
import os

def read_xyz_file(file_name):
    """Reads an XYZ file and determines if data starts from line 1 or line 3."""
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # Determine if the file starts with atom positions on line 1 or line 3
        if lines[0].strip().isdigit():
            data_start_line = 2
        else:
            data_start_line = 0
        
        atoms = [line.strip() for line in lines[data_start_line:] if line.strip()]
        return atoms

def write_xyz_file(file_name, atoms, original_lines):
    """Writes a list of atoms to an XYZ file."""
    with open(file_name, 'w') as file:
        if original_lines[0].strip().isdigit():
            file.write(f"{len(atoms)}\n")
            file.write(original_lines[1])  # Copy the second line (comment) if it exists
        file.writelines(f"{atom}\n" for atom in atoms)

def main():
    file_name = input("Name of the file? (Ensure it's in XYZ format): ").strip()
    atoms = read_xyz_file(file_name)
    n = len(atoms)
    
    print(f"The total number of atoms in the file is {n}")
    
    k = int(input("How many atoms do you wish to choose from? ").strip())
    
    # Generate all combinations of k atoms out of n
    combinations = list(itertools.combinations(atoms, k))
    print(f"Total combinations possible: {len(combinations)}")
    
    concat_choice = input("Do you want to concatenate to an existing file? (yes/no): ").strip().lower()
    
    if concat_choice == 'yes':
        concat_file = input("What's the name of the file to concatenate to? ").strip()
        concat_atoms = read_xyz_file(concat_file)
        for idx, combo in enumerate(combinations):
            new_atoms = concat_atoms + list(combo)
            new_file_name = f"concatenated_{idx+1}.xyz"
            write_xyz_file(new_file_name, new_atoms, concat_atoms)
    else:
        for idx, combo in enumerate(combinations):
            new_file_name = f"combination_{idx+1}.xyz"
            write_xyz_file(new_file_name, list(combo), atoms)
    
    print("All Done!")

if __name__ == "__main__":
    main()
