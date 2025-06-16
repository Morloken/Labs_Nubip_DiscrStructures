universal_set = set(range(1, 26))

 
set_A = {1, 2, 3, 4, 5, 11, 12, 17, 19, 22}
set_B = {1, 2, 3, 6, 7, 13, 14, 17, 18, 24 }
set_C = {1,2, 3, 13, 15, 16, 20, 21, 25}
 

complement_B = universal_set - set_B  # ~B
A_intersect_complement_B = set_A & complement_B  # A ∩ ~B,              & → перетин (intersection): A & B — спільні елементи множин А і В

complement_A_intersect_complement_B = universal_set - A_intersect_complement_B  # ~(A ∩ ~B)

complement_A = universal_set - set_A  # ~A
complement_A_intersect_B = complement_A & set_B  # ~A ∩ B

result_set = (complement_A_intersect_complement_B - complement_A_intersect_B) | set_C  # Основний вираз
#      | → об'єднання (union).   всі елементи з обох множин.

 
print("Потужність множини:", len(result_set))
print("Елементи множини:", result_set)