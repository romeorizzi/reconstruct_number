def che_mai_saralo_sto_numer:
    n = 0
    while not se_mia_zero_ah():
       if not se_mia_pari_cio():
           caveghe_zo_uno()
           n += 1
           continue
       dividi_par_do()
       n *= 2
    return n
