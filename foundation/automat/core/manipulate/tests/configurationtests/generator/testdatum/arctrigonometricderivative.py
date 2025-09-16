TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (D (arcsin x) x))',
                      'input': '(= y (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x x)))'},#(* (/ "1" (nroot "2" (- "1" (* $0 $0)))) (D $0 $1))
    ('vor', '0'): {'expected': '(= y (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x x)))', 'input': '(= y (D (arcsin x) x))'},#(D (arcsin $0) $1)


    ('hin', '1'): {   'expected': '(= y (D (arccos x) x))',
                      'input': '(= y (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x x)))'},#(* (- "0" (/ "1" (nroot "2" (- "1" (* $0 $0))))) (D $0 $1))
    ('vor', '1'): {'expected': '(= y (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x x)))', 'input': '(= y (D (arccos x) x))'},#(D (arccos $0) $1)


    ('hin', '2'): {   'expected': '(= y (D (arctan x) x))',
                      'input': '(= y (* (/ "1" (+ "1" (* x x))) (D x x)))'},#(* (/ "1" (+ "1" (* $0 $0))) (D $0 $1))
    ('vor', '2'): {'expected': '(= y (* (/ "1" (+ "1" (* x x))) (D x x)))', 'input': '(= y (D (arctan x) x))'},#(D (arctan $0) $1)


    ('hin', '3'): {   'expected': '(= y (D (arcsec x) x))',
                      'input': '(= y (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x x)))'},#(* (/ "1" (* $0 (nroot "2" (- (* $0 $0) "1")))) (D $0 $1))
    ('vor', '3'): {'expected': '(= y (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x x)))', 'input': '(= y (D (arcsec x) x))'},#(D (arcsec $0) $1)


    ('hin', '4'): {   'expected': '(= y (D (arccosec x) x))',
                      'input': '(= y (* (nroot "2" (- (* x x) "1")) (D x x)))'},#(* (nroot "2" (- (* $0 $0) "1")) (D $1 $0))
    ('vor', '4'): {'expected': '(= y (* (nroot "2" (- (* x x) "1")) (D x x)))', 'input': '(= y (D (arccosec x) x))'},#(D (arccosec $0) $1)


    ('hin', '5'): {   'expected': '(= y (D (arccot x) x))',
                      'input': '(= y (* (- "0" (/ "1" (+ "1" (* x x)))) (D x x)))'},#(* (- "0" (/ "1" (+ "1" (* $0 $0)))) (D $0 $1))
    ('vor', '5'): {'expected': '(= y (* (- "0" (/ "1" (+ "1" (* x x)))) (D x x)))', 'input': '(= y (D (arccot x) x))'}#(D (arccot $0) $1)

  }