;;; Lab08: Scheme

(define (over-or-under a b)
  (cond
    ((> a b) 1)
    ((= a b) 0)
    (else ((lambda (x) -1) 1))
  )
)


(define (make-adder n)
  (define (adder x)
    (+ x n)
  )
  adder
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define (remainder a b)
  (- a (* b (quotient a b))))

(define (gcd a b)
  (cond
    ((= b 0) a)
    (else (gcd b (modulo a b)))
  )
)


(define lst
  ((lambda (x) '((1) 2 (3 4) 5)) 1)
)


(define (ordered s)
  (cond
    ((null? (cdr s)) #t)
    ((>= (car (cdr s)) (car s)) (ordered (cdr s)))
    (else ((lambda (x) #f) 1))
  )
)
