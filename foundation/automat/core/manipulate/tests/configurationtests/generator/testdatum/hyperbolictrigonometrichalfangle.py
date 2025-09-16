TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (sinh (/ x "2")))',
                      'input': '(= y (/ (sinh x) (nroot "2" (* "2" (+ (cosh x) "1")))))'},#(/ (sinh $0) (nroot "2" (* "2" (+ (cosh $0) "1"))))
    ('vor', '0'): {'expected': '(= y (/ (sinh x) (nroot "2" (* "2" (+ (cosh x) "1")))))', 'input': '(= y (sinh (/ x "2")))'},#(sinh (/ $0 "2"))


    ('hin', '1'): {   'expected': '(= y (cosh (/ x "2")))',
                      'input': '(= y (nroot "2" (/ (+ (cosh x) "1") "2")))'},#(nroot "2" (/ (+ (cosh $0) "1") "2"))
    ('vor', '1'): {'expected': '(= y (nroot "2" (/ (+ (cosh x) "1") "2")))', 'input': '(= y (cosh (/ x "2")))'},#(cosh (/ $0 "2"))


    ('hin', '2'): {   'expected': '(= y (tanh (/ x "2")))',
                      'input': '(= y (/ (sinh x) (+ (cosh x) "1")))'},#(/ (sinh $0) (+ (cosh $0) "1"))
    ('vor', '2'): {'expected': '(= y (/ (sinh x) (+ (cosh x) "1")))', 'input': '(= y (tanh (/ x "2")))'}#(tanh (/ $0 "2"))

}