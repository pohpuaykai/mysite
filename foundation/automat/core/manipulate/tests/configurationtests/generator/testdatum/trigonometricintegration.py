TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (int (* (cos x) (D x v_{0})) v_{0}))', 'input': '(= y (+ (sin x) v_{0}))'},#(sin $0)
    ('vor', '0'): {   'expected': '(= y (+ (sin x) v_{0}))',
                      'input': '(= y (int (* (cos x) (D x x)) x))'},#(int (* (cos $0) (D $0 $1)) $1)


    ('hin', '1'): {'expected': '(= y (int (* (- "0" (sin x)) (D x v_{0})) v_{0}))', 'input': '(= y (+ (cos x) v_{0}))'},#(cos $0)
    ('vor', '1'): {   'expected': '(= y (+ (cos x) v_{0}))',
                      'input': '(= y (int (* (- "0" (sin x)) (D x x)) x))'},#(int (* (- "0" (sin $0)) (D $0 $1)) $1)


    ('hin', '2'): {'expected': '(= y (int (* (^ (sec x) "2") (D x v_{0})) v_{0}))', 'input': '(= y (+ (tan x) v_{0}))'},#(tan $0)
    ('vor', '2'): {   'expected': '(= y (+ (tan x) v_{0}))',
                      'input': '(= y (int (* (^ (sec x) "2") (D x x)) x))'},#(int (* (^ (sec $0) "2") (D $0 $1)) $1)


    ('hin', '3'): {'expected': '(= y (int (* (* (sec x) (tan x)) (D x v_{0})) v_{0}))', 'input': '(= y (+ (sec x) v_{0}))'},#(sec $0)
    ('vor', '3'): {   'expected': '(= y (+ (sec x) v_{0}))',
                      'input': '(= y (int (* (* (sec x) (tan x)) (D x x)) x))'},#(int (* (* (sec $0) (tan $0)) (D $0 $1)) $1)


    ('hin', '4'): {'expected': '(= y (int (* (- "0" (* (cosec x) (cot x))) (D x v_{0})) v_{0}))', 'input': '(= y (+ (cosec x) v_{0}))'},#(cosec $0)
    ('vor', '4'): {   'expected': '(= y (+ (cosec x) v_{0}))',
                      'input': '(= y (int (* (- "0" (* (cosec x) (cot x))) (D x x)) x))'},#(int (* (- "0" (* (cosec $0) (cot $0))) (D $0 $1)) $1)


    ('hin', '5'): {'expected': '(= y (int (* (- "0" (^ cosec x) "2") (D x v_{0})) v_{0}))', 'input': '(= y (+ (cot x) v_{0}))'},#(cot $0)
    ('vor', '5'): {   'expected': '(= y (+ (cot x) v_{0}))',
                      'input': '(= y (int (* (- "0" (^ cosec x) "2") (D x x)) x))'}#(int (* (- "0" (^ cosec $0) "2") (D $0 $1)) $1)

}