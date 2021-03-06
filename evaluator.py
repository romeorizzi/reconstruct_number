from turingarena import run_algorithm, submission, evaluation

goals = dict( exponential_algorithm = True, polynomial_algorithm = True, optimum_algorithm = True )

def test_case(N):
    with run_algorithm(submission.source) as p:
        res = p.che_mai_saralo_sto_numer()
        if res != N:
            print("Il numero che avevo in mente era %d, non %d come da tè affermato." % (N,res) )
            goals[exponential_algorithm] = False
            goals[optimum_algorithm] = False
            if N <= 100:
                goals[polynomial_algorithm] = False

        operations_done = 0
        n = N
        def se_mia_zero():
            return n == 0
        def se_mia_pari():
            return n % 2 == 0
        def caveghe_zo_uno():
            nonlocal operations_done
            if n == 0:
                print("Anna era partita col numero N=%d, ma ora, a seguito delle operazion che le avevi già richiesto, si ritrovava ora con uno zero. Ed ora gli chiedi di togliere uno? Questo non ti è consentito." % N )
                goals[exponential_algorithm] = False
                goals[optimum_algorithm] = False
                if N <= 100:
                    goals[polynomial_algorithm] = False
            n -= 1
            operations_done += 1

        def dividi_par_do():
            nonlocal operations_done
            if n % 2 == 1:
                print("Anna era partita col numero N=%d, ma ora, a seguito delle operazion che le avevi già richiesto, si ritrovava ora con %n, un numero dispari. Non ti è consentito richiedere la divisione per due di un numero dispari." % (N, n) )
                goals[exponential_algorithm] = False
                goals[optimum_algorithm] = False
                if N <= 100:
                    goals[polynomial_algorithm] = False            
            n /= 2
            operations_done += 1
        
        res = p.che_mai_saralo_sto_numer(callbacks = [caveghe_zo_uno, dividi_par_do, se_mia_pari_cio, se_mia_zero_ah] )
        if res != N:
            print("Anna era partita col numero N=%d, non col numero %d come restituito dalla tua funzione che_mai_saralo_sto_numer." % (N, res) )
            goals[exponential_algorithm] = False
            goals[optimum_algorithm] = False
            if N <= 100:
                goals[polynomial_algorithm] = False            

def run_all_test_cases():
    for N in range(1,10):
        test_case(N)
    for N in [99,100, 127, 128, 742, 1000]:
        test_case(N)
        
run_all_test_cases()
        
print(goals)

