# hi = hora inicia | hf = hora final
# mi = minuto inicial | mf = minuto final
hi, mi, hf, mf = [int(x) for x in input().split()]
inc = 0

if mi > mf:
    m = 60 - mi + mf
elif mi < mf:
    m = mf - mi
elif mi == mf:
    m = 0

if mi > mf:
    inc = 1

if hi > hf:
    h = 24 - hi + hf - inc
elif hi < hf:
    h = hf - hi - inc
elif hi == hf:
    if mi > mf or mi == mf:
        h = 24 - inc
    elif mi < mf:
        h = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(h, m))
