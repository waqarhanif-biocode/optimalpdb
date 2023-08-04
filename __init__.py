from .main import run_optimalpdb

def optimalpdb_function(uniprot_id, output_folder="pdb_files"):
    run_optimalpdb(uniprot_id, output_folder)
