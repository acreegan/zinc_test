from opencmiss.zinc.context import Context
from opencmiss.zinc.status import OK as ZINC_OK

# Surface mesh fitted to human torso
files_to_load = ["Torso_fitted.exnode", "Torso_fitted.exelem"]

context = Context("Example")
region = context.getDefaultRegion()
for file in files_to_load:
    region.readFile(file)
fieldmodule = region.getFieldmodule()
field = fieldmodule.findFieldByName("coordinates")
cache = fieldmodule.createFieldcache()
xi = [0.5, 0.5]  # Center of a 2 dimensional element
mesh = fieldmodule.findMeshByDimension(2)  # Surface mesh has 2 dimensional elements
el_iter = mesh.createElementiterator()
element = el_iter.next()
outputs = []

# Display coordinates of each element
while element.isValid():
    cache.setMeshLocation(element, xi)
    result, outValues = field.evaluateReal(cache, 3)
    # Check result for errors, Use outValues
    if result == ZINC_OK:
        print(f"Element no.: {element.getIdentifier()}, coordinates:{outValues}")
        outputs.append(outValues)
    else:
        break
    element = el_iter.next()

# TODO: Convert to STL/OBJ/PLY and export
