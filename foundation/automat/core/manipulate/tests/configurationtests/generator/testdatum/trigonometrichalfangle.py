TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (^ (sin (/ x "2")) "2"))', 'input': '(= y (/ (- "1" (cos x)) "2"))'},#(/ (- "1" (cos $0)) "2")
    ('vor', '0'): {'expected': '(= y (/ (- "1" (cos x)) "2"))', 'input': '(= y (^ (sin (/ x "2")) "2"))'},#(^ (sin (/ $0 "2")) "2")


    ('hin', '1'): {'expected': '(= y (^ (cos (/ x "2")) "2"))', 'input': '(= y (/ (+ "1" (cos x)) "2"))'},#(/ (+ "1" (cos $0)) "2")
    ('vor', '1'): {'expected': '(= y (/ (+ "1" (cos x)) "2"))', 'input': '(= y (^ (cos (/ x "2")) "2"))'},#(^ (cos (/ $0 "2")) "2")


    ('hin', '2'): {'expected': '(= y (tan (/ x "2")))', 'input': '(= y (- (cosec x) (cot x)))'},#(- (cosec $0) (cot $0))
    ('vor', '2'): {'expected': '(= y (- (cosec x) (cot x)))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '3'): {   'expected': '(= y (tan (/ x "2")))',
                      'input': '(= y (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x)))))'},#(nroot "2" (/ (- "1" (cos $0)) (+ "1" (cos $0))))
    ('vor', '3'): {'expected': '(= y (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x)))))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '4'): {   'expected': '(= y (tan (/ x "2")))',
                      'input': '(= y (- "0" (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x))))))'},#(- "0" (nroot "2" (/ (- "1" (cos $0)) (+ "1" (cos $0)))))
    ('vor', '4'): {'expected': '(= y (- "0" (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x))))))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '5'): {   'expected': '(= y (tan (/ x "2")))',
                      'input': '(= y (- "0" (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x))))))'},#(- "0" (nroot "2" (/ (- "1" (cos $0)) (+ "1" (cos $0)))))
    ('vor', '5'): {'expected': '(= y (- "0" (nroot "2" (/ (- "1" (cos x)) (+ "1" (cos x))))))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '6'): {'expected': '(= y (tan (/ x "2")))', 'input': '(= y (/ (sin x) (+ "1" (cos x))))'},#(/ (sin $0) (+ "1" (cos $0)))
    ('vor', '6'): {'expected': '(= y (/ (sin x) (+ "1" (cos x))))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '7'): {'expected': '(= y (tan (/ x "2")))', 'input': '(= y (/ (- "1" (cos x)) (sin x)))'},#(/ (- "1" (cos $0)) (sin $0))
    ('vor', '7'): {'expected': '(= y (/ (- "1" (cos x)) (sin x)))', 'input': '(= y (tan (/ x "2")))'},#(tan (/ $0 "2"))


    ('hin', '8'): {'expected': '(= y (cot (/ x "2")))', 'input': '(= y (+ (cosec x) (cot x)))'},#(+ (cosec $0) (cot $0))
    ('vor', '8'): {'expected': '(= y (+ (cosec x) (cot x)))', 'input': '(= y (cot (/ x "2")))'},#(cot (/ $0 "2"))


    ('hin', '9'): {   'expected': '(= y (cot (/ x "2")))',
                      'input': '(= y (nroot "2" (/ (+ "1" (cos x)) (- "1" (cos x)))))'},#(nroot "2" (/ (+ "1" (cos $0)) (- "1" (cos $0))))
    ('vor', '9'): {'expected': '(= y (nroot "2" (/ (+ "1" (cos x)) (- "1" (cos x)))))', 'input': '(= y (cot (/ x "2")))'},#(cot (/ $0 "2"))

    ('hin', '10'): {   'expected': '(= y (cot (/ x "2")))',
                       'input': '(= y (- "0" (nroot "2" (/ (+ "1" (cos x)) (- "1" (cos x))))))'},#(- "0" (nroot "2" (/ (+ "1" (cos $0)) (- "1" (cos $0)))))
    ('vor', '10'): {'expected': '(= y (- "0" (nroot "2" (/ (+ "1" (cos x)) (- "1" (cos x))))))', 'input': '(= y (cot (/ x "2")))'},#(cot (/ $0 "2"))


    ('hin', '11'): {'expected': '(= y (cot (/ x "2")))', 'input': '(= y (/ (sin x) (- "1" (cos x))))'},#(/ (sin $0) (- "1" (cos $0)))
    ('vor', '11'): {'expected': '(= y (/ (sin x) (- "1" (cos x))))', 'input': '(= y (cot (/ x "2")))'},#(cot (/ $0 "2"))


    ('hin', '12'): {'expected': '(= y (cot (/ x "2")))', 'input': '(= y (/ (+ "1" (cos x)) (sin x)))'},#(/ (+ "1" (cos $0)) (sin $0))
    ('vor', '12'): {'expected': '(= y (/ (+ "1" (cos x)) (sin x)))', 'input': '(= y (cot (/ x "2")))'},#(cot (/ $0 "2"))

    }