from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem, Draw

m1 = Chem.MolFromSmiles('CC(C)NCC(O)COC1=CC=CC2=CC=CC=C12')
m2 = Chem.MolFromSmiles('CC(C)NS(=O)(=O)CCOC1=CC=CC2=CC=CC=C12')

Rads = [1,2,3,4]
Bits = [512,1024,2048,4096]

for Rad in Rads:
    for Bit in Bits:
        fp1 = AllChem.GetMorganFingerprintAsBitVect(m1, Rad, nBits=Bit)
        fp2 = AllChem.GetMorganFingerprintAsBitVect(m2, Rad, nBits=Bit)
        MolSim = DataStructs.TanimotoSimilarity(fp1, fp2)
        print("Radius of ", Rad, ", ", Bit, " bits: ", MolSim,sep="")