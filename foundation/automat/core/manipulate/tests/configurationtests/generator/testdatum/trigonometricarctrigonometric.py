TEST_DATUM = {
    ('hin', '0'): {'expected': '(= (sin (arcsin y)) (sin (arcsin x)))', 'input': '(= y x)'},#$0
    ('vor', '0'): {'expected': '(= y x)', 'input': '(= y (sin (arcsin x)))'},#(sin (arcsin $0))


    ('hin', '1'): {'expected': '(= y (sin (arccos x)))', 'input': '(= y (nroot "2" (- "1" (^ x "2"))))'},#(nroot "2" (- "1" (^ $0 "2")))
    ('vor', '1'): {'expected': '(= y (nroot "2" (- "1" (^ x "2"))))', 'input': '(= y (sin (arccos x)))'},#(sin (arccos $0))


    ('hin', '2'): {   'expected': '(= y (sin (arctan x)))',
                      'input': '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))'},#(/ $0 (nroot "2" (+ "1" (^ $0 "2"))))
    ('vor', '2'): {'expected': '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))', 'input': '(= y (sin (arctan x)))'},#(sin (arctan $0))


    ('hin', '3'): {'expected': '(= y (sin (arccosec x)))', 'input': '(= y (/ "1" x))'},#(/ "1" $0)
    ('vor', '3'): {'expected': '(= y (/ "1" x))', 'input': '(= y (sin (arccosec x)))'},#(sin (arccosec $0))


    ('hin', '4'): {   'expected': '(= y (sin (arcsec x)))',
                      'input': '(= y (/ (nroot "2" (- (^ x "2") "1")) x))'},#(/ (nroot "2" (- (^ $0 "2") "1")) $0)
    ('vor', '4'): {'expected': '(= y (/ (nroot "2" (- (^ x "2") "1")) x))', 'input': '(= y (sin (arcsec x)))'},#(sin (arcsec $0))


    ('hin', '5'): {   'expected': '(= y (sin (arccot x)))',
                      'input': '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))'},#(/ "1" (nroot "2" (+ "1" (^ $0 "2"))))
    ('vor', '5'): {'expected': '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))', 'input': '(= y (sin (arccot x)))'},#(sin (arccot $0))


    ('hin', '6'): {'expected': '(= y (cos (arcsin x)))', 'input': '(= y (nroot "2" (- "1" (^ x "2"))))'},#(nroot "2" (- "1" (^ $0 "2")))
    ('vor', '6'): {'expected': '(= y (nroot "2" (- "1" (^ x "2"))))', 'input': '(= y (cos (arcsin x)))'},#(cos (arcsin $0))


    ('hin', '7'): {'expected': '(= (cos (arccos y)) (cos (arccos x)))', 'input': '(= y x)'},#$0
    ('vor', '7'): {'expected': '(= y x)', 'input': '(= y (cos (arccos x)))'},#(cos (arccos $0))


    ('hin', '8'): {   'expected': '(= y (cos (arctan x)))',
                      'input': '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))'},#(/ "1" (nroot "2" (+ "1" (^ $0 "2"))))
    ('vor', '8'): {'expected': '(= y (/ "1" (nroot "2" (+ "1" (^ x "2")))))', 'input': '(= y (cos (arctan x)))'},#(cos (arctan $0))


    ('hin', '9'): {   'expected': '(= y (cos (arccosec x)))',
                      'input': '(= y (/ (nroot "2" (- (^ x "2") "1")) x))'},#(/ (nroot "2" (- (^ $0 "2") "1")) $0)
    ('vor', '9'): {'expected': '(= y (/ (nroot "2" (- (^ x "2") "1")) x))', 'input': '(= y (cos (arccosec x)))'},#(cos (arccosec $0))


    ('hin', '10'): {'expected': '(= y (cos (arcsec x)))', 'input': '(= y (/ "1" x))'},#(/ "1" $0)
    ('vor', '10'): {'expected': '(= y (/ "1" x))', 'input': '(= y (cos (arcsec x)))'},#(cos (arcsec $0))


    ('hin', '11'): {   'expected': '(= y (cos (arccot x)))',
                       'input': '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))'},#(/ $0 (nroot "2" (+ "1" (^ $0 "2"))))
    ('vor', '11'): {'expected': '(= y (/ x (nroot "2" (+ "1" (^ x "2")))))', 'input': '(= y (cos (arccot x)))'},#(cos (arccot $0))


    ('hin', '12'): {   'expected': '(= y (tan (arcsin x)))',
                       'input': '(= y (/ x (nroot "2" (- "1" (^ x "2")))))'},#(/ $0 (nroot "2" (- "1" (^ $0 "2"))))
    ('vor', '12'): {'expected': '(= y (/ x (nroot "2" (- "1" (^ x "2")))))', 'input': '(= y (tan (arcsin x)))'},#(tan (arcsin $0))


    ('hin', '13'): {   'expected': '(= y (tan (arccos x)))',
                       'input': '(= y (/ (nroot "2" (- "1" (^ x "2"))) x))'},#(/ (nroot "2" (- "1" (^ $0 "2"))) $0)
    ('vor', '13'): {'expected': '(= y (/ (nroot "2" (- "1" (^ x "2"))) x))', 'input': '(= y (tan (arccos x)))'},#(tan (arccos $0))


    ('hin', '14'): {'expected': '(= (tan (arctan y)) (tan (arctan x)))', 'input': '(= y x)'},#$0
    ('vor', '14'): {'expected': '(= y x)', 'input': '(= y (tan (arctan x)))'},#(tan (arctan $0))


    ('hin', '15'): {   'expected': '(= y (tan (arccosec x)))',
                       'input': '(= y (/ "1" (nroot "2" (- (^ x "2") "1"))))'},#(/ "1" (nroot "2" (- (^ $0 "2") "1")))
    ('vor', '15'): {'expected': '(= y (/ "1" (nroot "2" (- (^ x "2") "1"))))', 'input': '(= y (tan (arccosec x)))'},#(tan (arccosec $0))


    ('hin', '16'): {   'expected': '(= y (tan (arcsec x)))',
                       'input': '(= y (nroot "2" (- (^ x "2") "1")))'},#(nroot "2" (- (^ $0 "2") "1"))
    ('vor', '16'): {'expected': '(= y (nroot "2" (- (^ x "2") "1")))', 'input': '(= y (tan (arcsec x)))'},#(tan (arcsec $0))


    ('hin', '17'): {'expected': '(= y (tan (arccot $0)))', 'input': '(= y (/ "1" $0))'},#(/ "1" $0)
    ('vor', '17'): {'expected': '(= y (/ "1" $0))', 'input': '(= y (tan (arccot $0)))'}#(tan (arccot $0))

}