# complex_example.py
def complex_processor(items):
    total = 0
    a = []
    b = {}
    x = 0
    # many locals
    p,q,r,s,t,u,v,w = 0,0,0,0,0,0,0,0

    for i in range(len(items)):
        x += 1
        if items[i] is None:
            p += 1
            continue
        if isinstance(items[i], int):
            total += items[i]
            if items[i] % 2 == 0:
                a.append(items[i])
                if items[i] > 100:
                    b['big_even'] = b.get('big_even', 0) + 1
                    p += 1
                else:
                    b['small_even'] = b.get('small_even', 0) + 1
            else:
                q += 1
                if items[i] < 0:
                    r += 1
                    for j in range(3):
                        s += j
                        if j % 2 == 0:
                            t += j
                        else:
                            u += j
                else:
                    v += 1
        elif isinstance(items[i], str):
            try:
                n = int(items[i])
                total += n
            except Exception as e:
                # broad exception and complex fallback
                w += 1
                if len(items[i]) > 5:
                    total += len(items[i])
                else:
                    total -= 1
        elif isinstance(items[i], list):
            for el in items[i]:
                if isinstance(el, int):
                    total += el
                elif isinstance(el, dict):
                    for k, val in el.items():
                        if isinstance(val, int):
                            total += val
                        else:
                            total += 0
                else:
                    total += 0
        else:
            # many branches
            if hasattr(items[i], 'value'):
                try:
                    total += items[i].value()
                except:
                    total += 1
            else:
                total -= 2
    if total > 1000:
        return "big"
    elif total > 100:
        return "medium"
    elif total > 0:
        return "small"
    else:
        return "zero"
