def gaseste_cnp(lista_text, sir):
    for index, text in enumerate(lista_text):
        i = 0
        n = len(text) - len(sir)
        while i <= n:
            j = 0
            sw = True
            while sw and j < len(sir):
                if text[i + j] != sir[j]:
                    sw = False
                j += 1
            if sw and j == len(sir):
                print(f"Primul CNP găsit pentru data de naștere {sir} este {text}.")
                return
                break
            i += 1
    print(f"Nu s-a găsit niciun CNP pentru data de naștere {sir}.")  # If substring is not found in any string

