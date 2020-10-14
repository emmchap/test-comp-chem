from rdkit import Chem

suppl = Chem.SDMolSupplier('data/824_ideal.sdf')
for mol in suppl:
    print(Chem.MolToSmiles(mol),file=open("data/824_smiles.txt","w"))