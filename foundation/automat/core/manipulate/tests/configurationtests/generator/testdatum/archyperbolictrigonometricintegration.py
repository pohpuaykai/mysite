TEST_DATUM = {   
    ('hin', '0'): {'expected': '(= y (int (* (sech (arcsinh x)) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arcsinh x) v_{0}))'},#(arcsinh $0)
    ('vor', '0'): {   'expected': '(= y (+ (arcsinh x) v_{0}))',
                      'input': '(= y (int (* (sech (arcsinh x)) (D x x)) x))'},#(int (* (sech (arcsinh $0)) (D $0 $1)) $1)


    ('hin', '1'): {'expected': '(= y (int (* (cosech (arccosh x)) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccosh x) v_{0}))'},#(arccosh $0)
    ('vor', '1'): {   'expected': '(= y (+ (arccosh x) v_{0}))',
                      'input': '(= y (int (* (cosech (arccosh x)) (D x x)) x))'},#(int (* (cosech (arccosh $0)) (D $0 $1)) $1)


    ('hin', '2'): {'expected': '(= y (int (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x v_{0})) v_{0}))', 'input': '(= y (+ (arctanh x) v_{0}))'},#(arctanh $0)
    ('vor', '2'): {   'expected': '(= y (+ (arctanh x) v_{0}))',
                      'input': '(= y (int (* (/ (+ "1" (cosh (* "2" (arctanh x)))) "2") (D x x)) x))'},#(int (* (/ (+ "1" (cosh (* "2" (arctanh $0)))) "2") (D $0 $1)) $1)


    ('hin', '3'): {'expected': '(= y (int (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arcsech x) v_{0}))'},#(arcsech $0)
    ('vor', '3'): {   'expected': '(= y (+ (arcsech x) v_{0}))',
                      'input': '(= y (int (* (* (- "0" (cosh (arcsech x))) (coth (arcsech x))) (D x x)) x))'},#(int (* (* (- "0" (cosh (arcsech $0))) (coth (arcsech $0))) (D $0 $1)) $1)


    ('hin', '4'): {'expected': '(= y (int (* (* (- "0" (sinh (arccosech x)))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccosech x) v_{0}))'},#(arccosech $0)
    ('vor', '4'): {   'expected': '(= y (+ (arccosech x) v_{0}))',
                      'input': '(= y (int (* (* (- "0" (sinh (arccosech x)))) (D x x)) x))'},#(int (* (* (- "0" (sinh (arccosech $0)))) (D $0 $1)) $1)


    ('hin', '5'): {'expected': '(= y (int (* (/ (- "1" (sinh (arccoth x))) "2") (D x v_{0})) v_{0}))', 'input': '(= y (+ (arccoth x) v_{0}))'},#(arccoth $0)
    ('vor', '5'): {   'expected': '(= y (+ (arccoth x) v_{0}))',
                      'input': '(= y (int (* (/ (- "1" (sinh (arccoth x))) "2") (D x x)) x))'}#(int (* (/ (- "1" (sinh (arccoth $0))) "2") (D $0 $1)) $1)
}