TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (+ (sin x) (sin z)))',
                      'input': '(= y (* (* "2" (sin (/ (+ x z) "2"))) (cos (/ (- x z) "2"))))'},#(* (* "2" (sin (/ (+ $0 $1) "2"))) (cos (/ (- $0 $1) "2")))
    ('vor', '0'): {'expected': '(= y (* (* "2" (sin (/ (+ x z) "2"))) (cos (/ (- x z) "2"))))', 'input': '(= y (+ (sin x) (sin z)))'},#(+ (sin $0) (sin $1))


    ('hin', '1'): {   'expected': '(= y (- (sin x) (sin z)))',
                      'input': '(= y (* (* "2" (sin (/ (- x z) "2"))) (cos (/ (+ x z) "2"))))'},#(* (* "2" (sin (/ (- $0 $1) "2"))) (cos (/ (+ $0 $1) "2")))
    ('vor', '1'): {'expected': '(= y (* (* "2" (sin (/ (- x z) "2"))) (cos (/ (+ x z) "2"))))', 'input': '(= y (- (sin x) (sin z)))'},#(- (sin $0) (sin $1))


    ('hin', '2'): {   'expected': '(= y (- (cos x) (cos z)))',
                      'input': '(= y (- "0" (* (* "2" (sin (/ (+ x z) "2"))) (sin (/ (- x z) "2")))))'},#(- "0" (* (* "2" (sin (/ (+ $0 $1) "2"))) (sin (/ (- $0 $1) "2"))))
    ('vor', '2'): {'expected': '(= y (- "0" (* (* "2" (sin (/ (+ x z) "2"))) (sin (/ (- x z) "2")))))', 'input': '(= y (- (cos x) (cos z)))'},#(- (cos $0) (cos $1))


    ('hin', '3'): {   'expected': '(= y (+ (tan x) (tan z)))',
                      'input': '(= y (/ (sin (+ x z)) (* (cos x) (cos z))))'},#(/ (sin (+ $0 $1)) (* (cos $0) (cos $1)))
    ('vor', '3'): {'expected': '(= y (/ (sin (+ x z)) (* (cos x) (cos z))))', 'input': '(= y (+ (tan x) (tan z)))'},#(+ (tan $0) (tan $1))


    ('hin', '4'): {   'expected': '(= y (- (tan x) (tan z)))',
                      'input': '(= y (/ (sin (- x z)) (* (cos x) (cos z))))'},#(/ (sin (- $0 $1)) (* (cos $0) (cos $1)))
    ('vor', '4'): {'expected': '(= y (/ (sin (- x z)) (* (cos x) (cos z))))', 'input': '(= y (- (tan x) (tan z)))'}#(- (tan $0) (tan $1))

}