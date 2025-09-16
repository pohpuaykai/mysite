TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arcsin x) v_{0}))'},#(arcsin $0)
    ('vor', '0'): {   'expected': '(= y (+ (arcsin x) v_{0}))',
                      'input': '(= y (int (* (/ "1" (nroot "2" (- "1" (* x x)))) (D x x)) x))'},#(int (* (/ "1" (nroot "2" (- "1" (* $0 $0)))) (D $0 $1)) $1)


    ('hin', '1'): {'expected': '(= y (int (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccos x) v_{0}))'},#(arccos $0)
    ('vor', '1'): {   'expected': '(= y (+ (arccos x) v_{0}))',
                      'input': '(= y (int (* (- "0" (/ "1" (nroot "2" (- "1" (* x x))))) (D x x)) x))'},#(int (* (- "0" (/ "1" (nroot "2" (- "1" (* $0 $0))))) (D $0 $1)) $1)


    ('hin', '2'): {'expected': '(= y (int (* (/ "1" (+ "1" (* x x))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arctan x) v_{0}))'},#(arctan $0)
    ('vor', '2'): {   'expected': '(= y (+ (arctan x) v_{0}))',
                      'input': '(= y (int (* (/ "1" (+ "1" (* x x))) (D x x)) x))'},#(int (* (/ "1" (+ "1" (* $0 $0))) (D $0 $1)) $1)


    ('hin', '3'): {'expected': '(= y (int (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arcsec x) v_{0}))'},#(arcsec $0)
    ('vor', '3'): {   'expected': '(= y (+ (arcsec x) v_{0}))',
                      'input': '(= y (int (* (/ "1" (* x (nroot "2" (- (* x x) "1")))) (D x x)) x))'},#(int (* (/ "1" (* $0 (nroot "2" (- (* $0 $0) "1")))) (D $0 $1)) $1)


    ('hin', '4'): {'expected': '(= y (int (* (nroot "2" (- (* x x) "1")) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccosec x) v_{0}))'},#(arccosec $0)
    ('vor', '4'): {   'expected': '(= y (+ (arccosec x) v_{0}))',
                      'input': '(= y (int (* (nroot "2" (- (* x x) "1")) (D x x)) x))'},#(int (* (nroot "2" (- (* $0 $0) "1")) (D $1 $0)) $1)


    ('hin', '5'): {'expected': '(= y (int (* (- "0" (/ "1" (+ "1" (* x x)))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccot x) v_{0}))'},#(arccot $0)
    ('vor', '5'): {   'expected': '(= y (+ (arccot x) v_{0}))',
                      'input': '(= y (int (* (- "0" (/ "1" (+ "1" (* x x)))) (D x x)) x))'}#(int (* (- "0" (/ "1" (+ "1" (* $0 $0)))) (D $0 $1)) $1)

}