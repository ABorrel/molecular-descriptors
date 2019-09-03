from Desc3D import rdkit3D
import descriptor
prout = "./../trash/"

#descriptor.getLdesc("1D2D")

SMILES = "OC(=NC1=NC2=C(N=CN2C2CC(OC(=O)C3=CC=CC=C3)C(COC(=O)C3=CC=CC=C3)O2)C(O)=N1)C1=CC=CC=C1"
#SMILES = "OO"
cDesc = descriptor.Descriptor(SMILES, prout)
cDesc.set3DChemical()
cDesc.computeAll3D()

pfilout = prout + "morse3D.csv"
filout = open(pfilout, "w")
for desc in cDesc.morse3D.keys():
    filout.write("%s\t%s\n"%(desc, cDesc.morse3D[desc]))
filout.close()
sss



pfilout = prout + "CPASE3D.csv"
filout = open(pfilout, "w")
for desc in cDesc.CPSA3D.keys():
    filout.write("%s\t%s\n"%(desc, cDesc.CPSA3D[desc]))
filout.close()

pfilout = prout + "rdf3D3D.csv"
filout = open(pfilout, "w")
for desc in cDesc.rdf3D.keys():
    filout.write("%s\t%s\n"%(desc, cDesc.rdf3D[desc]))
filout.close()

pfilout = prout + "whim3D.csv"
filout = open(pfilout, "w")
for desc in cDesc.whim3D.keys():
    filout.write("%s\t%s\n"%(desc, cDesc.whim3D[desc]))
filout.close()
ddd

# rdkit 3D
drdkit = rdkit3D.rdkit3D(cDesc.mol3D)
pfilout = prout + "descrdkit3D.csv"
filout = open(pfilout, "w")
for desc in drdkit.keys():
    filout.write("%s\t%s\n"%(desc, drdkit[desc]))
filout.close()
ddd





cDesc.computeAll2D()
print(len(list(cDesc.all2D.keys())))


pfilout = prout + "all.csv"
filout = open(pfilout, "w")
for desc in cDesc.all2D.keys():
    filout.write("%s\t%s\n"%(desc, cDesc.all2D[desc]))
filout.close()
ddd

drdkit = rdkitBase.computeDesc(cDesc.mol)
print("**")
print(drdkit["MaxEStateIndex"])

pfilout = prout + "descrdkit.csv"
filout = open(pfilout, "w")
for desc in drdkit.keys():
    filout.write("%s\t%s\n"%(desc, drdkit[desc]))
filout.close()


# writ
