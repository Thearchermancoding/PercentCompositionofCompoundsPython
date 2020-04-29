import json
import molecule

table_raw = [x for x in json.load(open('table.json', 'r'))["elements"]]
table = dict(zip([x["symbol"] for x in table_raw], table_raw))
def empirical_from_composition(elements, compositions):
    out = {}
    masses = [table[x]["atomic_mass"] for x in elements]
    moles = ([c/e for e, c in zip(masses, compositions)])
    for element, mole in zip(elements, moles):
        out[element] = round(mole/min(moles))
    return [a for a in out], [out[b] for b in [a for a in out]]
def compositions_from_empirical(elements, amounts):
    total_molar_masses = [table[a]["atomic_mass"]*b for a,b in zip(elements, amounts)]
    return elements, ([round(x/sum(total_molar_masses)*100, 1) for x in total_molar_masses])
e,n = (empirical_from_composition(["C", "H", "N"], [74, 8.7, 17.3]))
nicotine = molecule.Molecule(e, n)
print(nicotine)
print(compositions_from_empirical(e, n))