TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int (* (cosh x) (D x v_{0})) v_{0}))', 'input': '(= y (+ (sinh x) v_{0}))'},#(sinh $0)
    ('vor', '0'): {   'expected': '(= y (+ (sinh x) v_{0}))',
                      'input': '(= y (int (* (cosh x) (D x x)) x))'},#(int (* (cosh $0) (D $0 $1)) $1)


    ('hin', '1'): {'expected': '(= y (int (* (sinh x) (D x v_{0})) v_{0}))', 'input': '(= y (+ (cosh x) v_{0}))'},#(cosh $0)
    ('vor', '1'): {   'expected': '(= y (+ (cosh x) v_{0}))',
                      'input': '(= y (int (* (sinh x) (D x x)) x))'},#(int (* (sinh $0) (D $0 $1)) $1)


    ('hin', '2'): {'expected': '(= y (int (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (tanh x) v_{0}))'},#(tanh $0)
    ('vor', '2'): {   'expected': '(= y (+ (tanh x) v_{0}))',
                      'input': '(= y (int (* (/ "2" (+ (cosh (* "2" x) "1"))) (D x x)) x))'},#(int (* (/ "2" (+ (cosh (* "2" $0) "1"))) (D $0 $1)) $1)


    ('hin', '3'): {'expected': '(= y (int (* (- "0" (* (tanh x) (sech x))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (sech x) v_{0}))'},#(sech $0)
    ('vor', '3'): {   'expected': '(= y (+ (sech x) v_{0}))',
                      'input': '(= y (int (* (- "0" (* (tanh x) (sech x))) (D x x)) x))'},#(int (* (- "0" (* (tanh $0) (sech $0))) (D $0 $1)) $1)


    ('hin', '4'): {'expected': '(= y (int (* (- "0" (* (coth x) (cosech x))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (cosech x) v_{0}))'},#(cosech $0)
    ('vor', '4'): {   'expected': '(= y (+ (cosech x) v_{0}))',
                      'input': '(= y (int (* (- "0" (* (coth x) (cosech x))) (D x x)) x))'},#(int (* (- "0" (* (coth $0) (cosech $0))) (D $0 $1)) $1)


    ('hin', '5'): {'expected': '(= y (int (* (/ "2" (- "1" (sinh (* "2" x)))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (coth x) v_{0}))'},#(coth $0)
    ('vor', '5'): {   'expected': '(= y (+ (coth x) v_{0}))',
                      'input': '(= y (int (* (/ "2" (- "1" (sinh (* "2" x)))) (D x x)) x))'}#(int (* (/ "2" (- "1" (sinh (* "2" $0)))) (D $0 $1)) $1)

}