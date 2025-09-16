TEST_DATUM = {
    ('hin', '0'): {'expected': '(= y (sin (* "2" x)))', 'input': '(= y (* (* "2" (sin x)) (cos x)))'},#(* (* "2" (sin $0)) (cos $0))
    ('vor', '0'): {'expected': '(= y (* (* "2" (sin x)) (cos x)))', 'input': '(= y (sin (* "2" x)))'},#(sin (* "2" $0))


    ('hin', '1'): {   'expected': '(= y (sin (* "2" x)))',
                      'input': '(= y (/ (* "2" (tan x)) (+ "1" (^ (tan x) "2"))))'},#(/ (* "2" (tan $0)) (+ "1" (^ (tan $0) "2")))
    ('vor', '1'): {'expected': '(= y (/ (* "2" (tan x)) (+ "1" (^ (tan x) "2"))))', 'input': '(= y (sin (* "2" x)))'},#(sin (* "2" $0))


    ('hin', '2'): {   'expected': '(= y (cos (* "2" x)))',
                      'input': '(= y (- (^ (cos x) "2") (^ (sin x) "2")))'},#(- (^ (cos $0) "2") (^ (sin $0) "2"))
    ('vor', '2'): {'expected': '(= y (- (^ (cos x) "2") (^ (sin x) "2")))', 'input': '(= y (cos (* "2" x)))'},#(cos (* "2" $0))


    ('hin', '3'): {   'expected': '(= y (cos (* "2" x)))',
                      'input': '(= y (- (* "2" (^ (cos x) "2")) "1"))'},#(- (* "2" (^ (cos $0) "2")) "1")
    ('vor', '3'): {'expected': '(= y (- (* "2" (^ (cos x) "2")) "1"))', 'input': '(= y (cos (* "2" x)))'},#(cos (* "2" $0))


    ('hin', '4'): {   'expected': '(= y (cos (* "2" x)))',
                      'input': '(= y (- "1" (* "2" (^ (sin x) "2"))))'},#(- "1" (* "2" (^ (sin $0) "2")))
    ('vor', '4'): {'expected': '(= y (- "1" (* "2" (^ (sin x) "2"))))', 'input': '(= y (cos (* "2" x)))'},#(cos (* "2" $0))


    ('hin', '5'): {   'expected': '(= y (cos (* "2" x)))',
                      'input': '(= y (/ (- "1" (^ (tan x) "2")) (+ "1" (^ (tan x) "2"))))'},#(/ (- "1" (^ (tan $0) "2")) (+ "1" (^ (tan $0) "2")))
    ('vor', '5'): {'expected': '(= y (/ (- "1" (^ (tan x) "2")) (+ "1" (^ (tan x) "2"))))', 'input': '(= y (cos (* "2" x)))'},#(cos (* "2" $0))


    ('hin', '6'): {   'expected': '(= y (tan (* "2" x)))',
                      'input': '(= y (/ (* "2" (tan x)) (- "1" (^ (tan x) "2"))))'},#(/ (* "2" (tan $0)) (- "1" (^ (tan $0) "2")))
    ('vor', '6'): {'expected': '(= y (/ (* "2" (tan x)) (- "1" (^ (tan x) "2"))))', 'input': '(= y (tan (* "2" x)))'},#(tan (* "2" $0))


    ('hin', '7'): {   'expected': '(= y (cot (* "2" x)))',
                      'input': '(= y (/ (- (* (^ cot "2") x) "1") (* "2" (cot x))))'},#(/ (- (* (^ cot "2") $0) "1") (* "2" (cot $0)))
    ('vor', '7'): {'expected': '(= y (/ (- (* (^ cot "2") x) "1") (* "2" (cot x))))', 'input': '(= y (cot (* "2" x)))'},#(cot (* "2" $0))


    ('hin', '8'): {   'expected': '(= y (cot (* "2" x)))',
                      'input': '(= y (/ (- "1" (* (^ tan "2") x)) (* "2" (tan x))))'},#(/ (- "1" (* (^ tan "2") $0)) (* "2" (tan $0)))
    ('vor', '8'): {'expected': '(= y (/ (- "1" (* (^ tan "2") x)) (* "2" (tan x))))', 'input': '(= y (cot (* "2" x)))'},#(cot (* "2" $0))


    ('hin', '9'): {   'expected': '(= y (sec (* "2" x)))',
                      'input': '(= y (/ (^ (sec x) "2") (- "2" (* (^ sec "2") x))))'},#(/ (^ (sec $0) "2") (- "2" (* (^ sec "2") $0)))
    ('vor', '9'): {'expected': '(= y (/ (^ (sec x) "2") (- "2" (* (^ sec "2") x))))', 'input': '(= y (sec (* "2" x)))'},#(sec (* "2" $0))


    ('hin', '10'): {   'expected': '(= y (sec (* "2" x)))',
                       'input': '(= y (/ (+ "1" (* (^ tan "2") x)) (- "1" (* (^ tan "2") x))))'},#(/ (+ "1" (* (^ tan "2") $0)) (- "1" (* (^ tan "2") $0)))
    ('vor', '10'): {'expected': '(= y (/ (+ "1" (* (^ tan "2") x)) (- "1" (* (^ tan "2") x))))', 'input': '(= y (sec (* "2" x)))'},#(sec (* "2" $0))


    ('hin', '11'): {   'expected': '(= y (cosec (* "2" x)))',
                       'input': '(= y (/ (* (sec x) (cosec x)) "2"))'},#(/ (* (sec $0) (cosec $0)) "2")
    ('vor', '11'): {'expected': '(= y (/ (* (sec x) (cosec x)) "2"))', 'input': '(= y (cosec (* "2" x)))'},#(cosec (* "2" $0))


    ('hin', '12'): {   'expected': '(= y (cosec (* "2" x)))',
                       'input': '(= y (/ (+ "1" (* (^ tan "2") x)) (* "2" (tan x))))'},#(/ (+ "1" (* (^ tan "2") $0)) (* "2" (tan $0)))
    ('vor', '12'): {'expected': '(= y (/ (+ "1" (* (^ tan "2") x)) (* "2" (tan x))))', 'input': '(= y (cosec (* "2" x)))'}#(cosec (* "2" $0))

}