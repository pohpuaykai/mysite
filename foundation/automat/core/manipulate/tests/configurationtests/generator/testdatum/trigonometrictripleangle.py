TEST_DATUM = {
    ('hin', '0'): {   'expected': '(= y (sin (* "3" x)))',
                      'input': '(= y (- (* "3" (sin x)) (* "4" (^ (sin x) "3"))))'},#(- (* "3" (sin x)) (* "4" (^ (sin x) "3")))
    ('vor', '0'): {'expected': '(= y (- (* "3" (sin x)) (* "4" (^ (sin x) "3"))))', 'input': '(= y (sin (* "3" x)))'},#(sin (* "3" x))


    ('hin', '1'): {   'expected': '(= y (cos (* "3" x)))',
                      'input': '(= y (- (* "4" (^ (cos x) "3")) (* "3" (cos x))))'},#(- (* "4" (^ (cos x) "3")) (* "3" (cos x)))
    ('vor', '1'): {'expected': '(= y (- (* "4" (^ (cos x) "3")) (* "3" (cos x))))', 'input': '(= y (cos (* "3" x)))'},#(cos (* "3" x))


    ('hin', '2'): {   'expected': '(= y (tan (* "3" x)))',
                      'input': '(= y (/ (- (* "3" (tan x)) (^ (tan x) "3")) (- "1" (* "3" (^ (tan x) "2")))))'},#(/ (- (* "3" (tan x)) (^ (tan x) "3")) (- "1" (* "3" (^ (tan x) "2"))))
    ('vor', '2'): {'expected': '(= y (/ (- (* "3" (tan x)) (^ (tan x) "3")) (- "1" (* "3" (^ (tan x) "2")))))', 'input': '(= y (tan (* "3" x)))'},#(tan (* "3" x))


    ('hin', '3'): {   'expected': '(= y (cot (* "3" x)))',
                      'input': '(= y (/ (- (* "3" (cot x)) (^ (cot x) "3")) (- "1" (* "3" (^ (cot x) "2")))))'},#(/ (- (* "3" (cot x)) (^ (cot x) "3")) (- "1" (* "3" (^ (cot x) "2"))))
    ('vor', '3'): {'expected': '(= y (/ (- (* "3" (cot x)) (^ (cot x) "3")) (- "1" (* "3" (^ (cot x) "2")))))', 'input': '(= y (cot (* "3" x)))'},#(cot (* "3" x))


    ('hin', '4'): {   'expected': '(= y (sec (* "3" x)))',
                      'input': '(= y (/ (^ (sec x) "3") (- "4" (* "3" (^ (sec x) "2")))))'},#(/ (^ (sec x) "3") (- "4" (* "3" (^ (sec x) "2"))))
    ('vor', '4'): {'expected': '(= y (/ (^ (sec x) "3") (- "4" (* "3" (^ (sec x) "2")))))', 'input': '(= y (sec (* "3" x)))'},#(sec (* "3" x))


    ('hin', '5'): {   'expected': '(= y (cosec (* "3" x)))',
                      'input': '(= y (/ (^ (cosec x) "3") (- (* "3" (^ (cosec x) "3")) "4")))'},#(/ (^ (cosec x) "3") (- (* "3" (^ (cosec x) "3")) "4"))
    ('vor', '5'): {'expected': '(= y (/ (^ (cosec x) "3") (- (* "3" (^ (cosec x) "3")) "4")))', 'input': '(= y (cosec (* "3" x)))'}#(cosec (* "3" x))

    }