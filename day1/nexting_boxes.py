def nesting_boxes(tags: str) -> bool:
    def nesting_boxes(tags: str) -> bool:
    # Een stack om de geopende doos-vormen bij te houden
    stack = []
    
    # Een dictionary om snel te zien welk sluitteken bij welk openteken hoort
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in tags:
        # Als het een openingsdoos is, zetten we hem op de stapel
        if char in "([{":
            stack.append(char)
        # Als het een sluitingsdoos is, controleren we de volgorde
        elif char in ")]}":
            # Als de stapel leeg is OF de bovenste doos matcht niet met de sluitvorm
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            # Als het wel klopt, halen we de geopende doos van de stapel
            stack.pop()
            
        # Alle andere letters (de stempels van de winkel) worden genegeerd
        
    # Als de stapel helemaal leeg is, nestelt alles perfect!
    return len(stack) == 0
