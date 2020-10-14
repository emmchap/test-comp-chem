from rdkit import Chem
from rdkit.Chem import rdMolDescriptors

suppl = Chem.SDMolSupplier('data/824_ideal.sdf')
for mol in suppl:
    print("Number of rotatable bonds:", rdMolDescriptors.CalcNumRotatableBonds(mol))
    print("Number of rings:", rdMolDescriptors.CalcNumRings(mol))
    print("Number of acceptor atoms:", rdMolDescriptors.CalcNumHBA(mol))
    print("Number of donor atoms:", rdMolDescriptors.CalcNumHBD(mol))
    print("Wildman-Crippen LogP:", rdMolDescriptors.CalcCrippenDescriptors(mol)[0])