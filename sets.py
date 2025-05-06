set1={1,3,2,6,5,7,8}
set2={2,3,5,3,9,0,4}
set1.add(13)
print(set1)

set2.remove(3)
print(set2)

union_set=set1.union(set2)
print(f' union: {union_set}')

intersection_sets=set1.intersection(set2)
print(f'intersection is: {intersection_sets}')