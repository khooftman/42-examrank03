def merge_harvest_rows(crate_a: list[int], crate_b: list[int]) -> list[int]:
    # Maak een lege lijst voor het eindresultaat
    merged_crate = []
    
    # Gebruik twee pointers om door beide kratten te navigeren
    pointer_a = 0
    pointer_b = 0
    
    length_a = len(crate_a)
    length_b = len(crate_b)
    
    # Loop zolang beide kratten nog appels bevatten om te vergelijken
    while pointer_a < length_a and pointer_b < length_b:
        # Vergelijk het gewicht van de huidige appels in beide kratten
        if crate_a[pointer_a] <= crate_b[pointer_b]:
            merged_crate.append(crate_a[pointer_a])
            pointer_a += 1
        else:
            merged_crate.append(crate_b[pointer_b])
            pointer_b += 1
            
    # Voeg de resterende appels van krat A toe (als die er nog zijn)
    while pointer_a < length_a:
        merged_crate.append(crate_a[pointer_a])
        pointer_a += 1
        
    # Voeg de resterende appels van krat B toe (als die er nog zijn)
    while pointer_b < length_b:
        merged_crate.append(crate_b[pointer_b])
        pointer_b += 1
        
    return merged_crate
