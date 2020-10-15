from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

m1 = Chem.MolFromSmiles('CC(C)NCC(O)COC1=CC=CC2=CC=CC=C12')
m2 = Chem.MolFromSmiles('CC(C)NS(=O)(=O)CCOC1=CC=CC2=CC=CC=C12')

fp1 = AllChem.GetMorganFingerprint(m1,2)
fp2 = AllChem.GetMorganFingerprint(m2,2)

MolSim = DataStructs.TanimotoSimilarity(fp1,fp2)
print(MolSim)