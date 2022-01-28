;;; HW08: Scheme

;;; Required Problems

(define (square x) (* x x))

(define (pow base exp)
  (cond
    ((= exp 0) 1)
    ((= exp 1) base)
    ((even? exp) (square (pow base (/ exp 2))))
    ((odd? exp) (* base (square (pow base (/ (- exp 1) 2)))))
  )
)


(define (filter-lst fn lst)
  (
    define (lst-up lst-old lst-new)
    (
      cond
      ((null? lst-old) lst-new)
      ((fn (car lst-old)) (lst-up (cdr lst-old) (append lst-new (cons (car lst-old) nil))))
      (else (lst-up (cdr lst-old) lst-new))
    )
  )
  (lst-up lst '())
)


(define (no-repeats s)
  (define (in-it value n)
    (cond 
      ((null? n) #f)
      ((= value (car n)) #t)
      (else (in-it value (cdr n)))
    )
  )
  (define (nr s n)
    (cond
      ((null? s) n)
      ((in-it (car s) n) (nr (cdr s) n))
      (else (nr (cdr s) (append n (cons (car s) nil))))
    )
  )
  (nr s '())
)


(define (substitute s old new)
  (define (sbsttt s n)
    (cond 
      ((null? s) n)
      ((pair? (car s)) (sbsttt (cdr s) (append n (cons (substitute (car s) old new) nil))))
      (else (if (eq? (car s) old) 
              (sbsttt (cdr s) (append n (cons new nil)))  
              (sbsttt (cdr s) (append n (cons (car s) nil))))
    ))
  )
  (sbsttt s '())
)


(define (sub-all s olds news)
    (if (null? olds)
      s
      (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
    )
)


(define (tree label branches)
  (cons label branches)
)

(define (label t)
  (car t)
)

(define (branches t)
  (cdr t)
)

(define (is-leaf t)
  (if (eq? (branches t) '())
    #t
    #f
  )
)

; A tree for test

(define t1 (tree 1
  (list
    (tree 2
      (list
        (tree 5 nil)
          (tree 6 (list
            (tree 8 nil)))))
    (tree 3 nil)
    (tree 4
      (list
        (tree 7 nil))))))


(define (label-sum t)
  (define (ls lst)
    (if (null? lst)
      0
      (+ (label-sum (car lst)) (ls (cdr lst)))
    )
  )
  (+ (label t) (ls (branches t)))
)


;;; Just for fun Problems

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (first-operand s) (cadr s))
(define (second-operand s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
; You can access the operands from the expressions with
; first-operand and second-operand
(define (first-operand p) (cadr p))
(define (second-operand p) (caddr p))

(define (derive-sum expr var)
  'YOUR-CODE-HERE
)

(define (derive-product expr var)
  'YOUR-CODE-HERE
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  'YOUR-CODE-HERE
)

(define (exp? exp)
  'YOUR-CODE-HERE
)

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  'YOUR-CODE-HERE
)
