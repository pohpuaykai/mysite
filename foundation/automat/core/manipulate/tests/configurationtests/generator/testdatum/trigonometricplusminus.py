TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (sin (+ x z)))',
                      'input': '(= y (+ (* (sin x) (cos z)) (* (cos x) (sin z))))'},#(+ (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ('vor', '0'): {'expected': '(= y (+ (* (sin x) (cos z)) (* (cos x) (sin z))))', 'input': '(= y (sin (+ x z)))'},#(sin (+ $0 $1))


    ('hin', '1'): {   'expected': '(= y (sin (- x z)))',
                      'input': '(= y (- (* (sin x) (cos z)) (* (cos x) (sin z))))'},#(- (* (sin $0) (cos $1)) (* (cos $0) (sin $1)))
    ('vor', '1'): {'expected': '(= y (- (* (sin x) (cos z)) (* (cos x) (sin z))))', 'input': '(= y (sin (- x z)))'},#(sin (- $0 $1))


    ('hin', '2'): {   'expected': '(= y (cos (+ x z)))',
                      'input': '(= y (- (* (cos x) (cos z)) (* (sin x) (sin z))))'},#(- (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ('vor', '2'): {'expected': '(= y (- (* (cos x) (cos z)) (* (sin x) (sin z))))', 'input': '(= y (cos (+ x z)))'},#(cos (+ $0 $1))


    ('hin', '3'): {   'expected': '(= y (cos (- x z)))',
                      'input': '(= y (+ (* (cos x) (cos z)) (* (sin x) (sin z))))'},#(+ (* (cos $0) (cos $1)) (* (sin $0) (sin $1)))
    ('vor', '3'): {'expected': '(= y (+ (* (cos x) (cos z)) (* (sin x) (sin z))))', 'input': '(= y (cos (- x z)))'},#(cos (- $0 $1))


    ('hin', '4'): {   'expected': '(= y (tan (+ x z)))',
                      'input': '(= y (/ (+ (tan x) (tan z)) (- "1" (* (tan x) (tan z)))))'},#(/ (+ (tan $0) (tan $1)) (- "1" (* (tan $0) (tan $1))))
    ('vor', '4'): {'expected': '(= y (/ (+ (tan x) (tan z)) (- "1" (* (tan x) (tan z)))))', 'input': '(= y (tan (+ x z)))'},#(tan (+ $0 $1))


    ('hin', '5'): {   'expected': '(= y (tan (- x z)))',
                      'input': '(= y (/ (- (tan x) (tan z)) (+ "1" (* (tan x) (tan z)))))'},#(/ (- (tan $0) (tan z)) (+ "1" (* (tan $0) (tan z))))
    ('vor', '5'): {'expected': '(= y (/ (- (tan x) (tan z)) (+ "1" (* (tan x) (tan z)))))', 'input': '(= y (tan (- x z)))'},#


    ('hin', '6'): {   'expected': '(= y (cosec (+ x z)))',
                      'input': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))'},#(/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ('vor', '6'): {'expected': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))', 'input': '(= y (cosec (+ x z)))'},#(cosec (+ $0 $1))


    ('hin', '7'): {   'expected': '(= y (cosec (- x z)))',
                      'input': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))'},#(/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ('vor', '7'): {'expected': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))', 'input': '(= y (cosec (- x z)))'},#(cosec (- $0 $1))


    ('hin', '8'): {   'expected': '(= y (cosec (+ x z)))',
                      'input': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))'},#(/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (- (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ('vor', '8'): {'expected': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (- (* (sec x) (cosec z)) (* (cosec x) (sec z)))))', 'input': '(= y (cosec (+ x z)))'},#(cosec (+ $0 $1))


    ('hin', '9'): {   'expected': '(= y (cosec (- x z)))',
                      'input': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))'},#(/ (* (* (* (sec $0) (sec $1)) (cosec $0)) (cosec $1)) (+ (* (sec $0) (cosec $1)) (* (cosec $0) (sec $1))))
    ('vor', '9'): {'expected': '(= y (/ (* (* (* (sec x) (sec z)) (cosec x)) (cosec z)) (+ (* (sec x) (cosec z)) (* (cosec x) (sec z)))))', 'input': '(= y (cosec (- x z)))'},#(cosec (- $0 $1))


    ('hin', '10'): {   'expected': '(= y (cot (+ x z)))',
                       'input': '(= y (/ (- (* (cot x) (cot z)) "1") (+ (cot z) (cot x))))'},#(/ (- (* (cot $0) (cot $1)) "1") (+ (cot $1) (cot $0)))
    ('vor', '10'): {'expected': '(= y (/ (- (* (cot x) (cot z)) "1") (+ (cot z) (cot x))))', 'input': '(= y (cot (+ x z)))'},#(cot (+ $0 $1))


    ('hin', '11'): {   'expected': '(= y (cot (- x z)))',
                       'input': '(= y (/ (+ (* (cot x) (cot z)) "1") (- (cot z) (cot x))))'},#(/ (+ (* (cot $0) (cot $1)) "1") (- (cot $1) (cot $0)))
    ('vor', '11'): {'expected': '(= y (/ (+ (* (cot x) (cot z)) "1") (- (cot z) (cot x))))', 'input': '(= y (cot (- x z)))'},#(cot (- $0 $1))


    ('hin', '12'): {   'expected': '(= y (+ (arcsin x) (arcsin z)))',
                       'input': '(= y (arcsin (+ (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))'},#(arcsin (+ (* $0 (nroot "2" (- "1" (^ $1 "2")))) (* $1 (nroot "2" (- "1" (^ $0 "2"))))))
    ('vor', '12'): {'expected': '(= y (arcsin (+ (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))', 'input': '(= y (+ (arcsin x) (arcsin z)))'},#(+ (arcsin $0) (arcsin $1))


    ('hin', '13'): {   'expected': '(= y (- (arcsin x) (arcsin z)))',
                       'input': '(= y (arcsin (- (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))'},#(arcsin (- (* $0 (nroot "2" (- "1" (^ $1 "2")))) (* $1 (nroot "2" (- "1" (^ $0 "2"))))))
    ('vor', '13'): {'expected': '(= y (arcsin (- (* x (nroot "2" (- "1" (^ z "2")))) (* z (nroot "2" (- "1" (^ x "2")))))))', 'input': '(= y (- (arcsin x) (arcsin z)))'},#(- (arcsin $0) (arcsin $1))


    ('hin', '14'): {   'expected': '(= y (+ (arccos x) (arccos z)))',
                       'input': '(= y (arccos (- (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))'},#(arccos (- (* $0 $1) (nroot "2" (* (- "1" (^ $0 "2")) (- "1" (^ $1 "2"))))))
    ('vor', '14'): {'expected': '(= y (arccos (- (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))', 'input': '(= y (+ (arccos x) (arccos z)))'},#(+ (arccos $0) (arccos $1))


    ('hin', '15'): {   'expected': '(= y (- (arccos x) (arccos z)))',
                       'input': '(= y (arccos (+ (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))'},#(arccos (+ (* $0 $1) (nroot "2" (* (- "1" (^ $0 "2")) (- "1" (^ $1 "2"))))))
    ('vor', '15'): {'expected': '(= y (arccos (+ (* x z) (nroot "2" (* (- "1" (^ x "2")) (- "1" (^ z "2")))))))', 'input': '(= y (- (arccos x) (arccos z)))'},#(- (arccos $0) (arccos $1))


    ('hin', '16'): {   'expected': '(= y (+ (arctan x) (arctan z)))',
                       'input': '(= y (arctan (/ (+ x z) (- "1" (* x z)))))'},#(arctan (/ (+ $0 $1) (- "1" (* $0 $1))))
    ('vor', '16'): {'expected': '(= y (arctan (/ (+ x z) (- "1" (* x z)))))', 'input': '(= y (+ (arctan x) (arctan z)))'},#(+ (arctan $0) (arctan $1))


    ('hin', '17'): {   'expected': '(= y (- (arctan x) (arctan z)))',
                       'input': '(= y (arctan (/ (- x z) (+ "1" (* x z)))))'},#(arctan (/ (- $0 $1) (+ "1" (* $0 $1))))
    ('vor', '17'): {'expected': '(= y (arctan (/ (- x z) (+ "1" (* x z)))))', 'input': '(= y (- (arctan x) (arctan z)))'},#(- (arctan $0) (arctan $1))


    ('hin', '18'): {   'expected': '(= y (+ (arccot x) (arccot z)))',
                       'input': '(= y (arccot (/ (- (* x z) "1") (+ z x))))'},#(arccot (/ (- (* $0 $1) "1") (+ $1 $0)))
    ('vor', '18'): {'expected': '(= y (arccot (/ (- (* x z) "1") (+ z x))))', 'input': '(= y (+ (arccot x) (arccot z)))'},#(+ (arccot $0) (arccot $1))


    ('hin', '19'): {   'expected': '(= y (- (arccot x) (arccot z)))',
                       'input': '(= y (arccot (/ (+ (* x z) "1") (- z x))))'},#(arccot (/ (+ (* $0 $1) "1") (- $1 $0)))
    ('vor', '19'): {'expected': '(= y (arccot (/ (+ (* x z) "1") (- z x))))', 'input': '(= y (- (arccot x) (arccot z)))'}#(- (arccot $0) (arccot $1))

}