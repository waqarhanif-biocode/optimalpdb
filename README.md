# OptimalPDB

This script retrives 3D structures by taking UniProt ID(s) as input, figures out the currently available PDB structures that are experimentally validated, and chooses the best structure based on lowest resolution (A value). Then it extracts PDB ID(s) that should be retrieved and stores it in a CSV file. 

What it extracts:
Resolution
PBD ID
Length of the structure (PDB)

# Installation
To install the package simply use pip: 
pip install optimalpdb

# To retrieve structure from a single UniProt accession (protein accession):
optimalpdb.run_optimalpdb("accession", "output_folder")

#Example: Q8NBP7
optimalpdb.run_optimalpdb("Q8NBP7", "myPDB")

You can also run it in a loop by providing multiple accession IDs in a txt file. Example is given in the files section. 
optimalpdb.run_optimalpdb("uniprot_ids.txt", "myPDBs")
