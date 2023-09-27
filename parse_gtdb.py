import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script.py input_file.txt")
    sys.exit(1)

input_file_path = sys.argv[1]

# Open the input and output files
with open(input_file_path, 'r') as input_file, open('output_gtdb.txt', 'w') as output_file:
    # Write the header to the output file
    output_file.write("user_genome\tdomain\tphylum\tclass\torder\tfamily\tgenus\tspecies\tclosest_placement_reference\n")

    # Skip the header line in the input file
    next(input_file)

    # Process each line in the input file
    for line in input_file:
        # Split the line into fields
        fields = line.strip().split('\t')

        # Extract relevant fields
        user_genome = fields[0]
        classification = fields[1]
        taxonomy = classification.split(';')
        closest_placement_reference = fields[7]
        #closest_placement_taxonomy = taxonomy[-1]

        # Extract domain, phylum, class, order, family, genus, species
        domain = taxonomy[0][3:]
        phylum = taxonomy[1][3:]
        class_ = taxonomy[2][3:]
        order = taxonomy[3][3:]
        family = taxonomy[4][3:]
        genus = taxonomy[5][3:]
        species = taxonomy[6][3:]

        # Write the extracted fields to the output file
        output_file.write(f"{user_genome}\t{domain}\t{phylum}\t{class_}\t{order}\t{family}\t{genus}\t{species}\t{closest_placement_reference}\n")

print(f"New file created: output_gtdb.txt")
