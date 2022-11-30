MESSAGE = f"""Bajgle, logiczna gra na dedukcję. Mam na myśli pewien ciąg znaków składający się z trzech cyfr (od 1 do 9)
na początku i trzech liter (od a do f) na końcu. W ciągu tym znaki i cyfry nie powtarzają się. Spróbuj odgadnąć ten 
ciąg. Oto wskazówki:
Gdy mówię:\tOznacza to:
\tPiko\tJedna cyfra lub znak jest poprawny, ale jest na złej pozycji.
\tFermi\tJedna cyfra lub znak jest poprawny i znajduje się na odpowiedniej pozycji.
\tBajgle\tŻadna cyfra ani znak nie jest poprawny.\n
Na przykład, jeśli tajny ciąg to 248abc, a Ty podasz ciąg 843dbe, wskazówka będzie brzmieć:
Fermi Piko Fermi."""

NUM_DIGITS = 3
NUM_LETTERS = 3
MAX_GUESSES = 10

WIN_MESSAGE = 'Udało się! Brawo :)'
FERMI_MESSAGE = 'Fermi'
PIKO_MESSAGE = 'Piko'
BAJGLE_MESSAGE = 'Bajgle'
