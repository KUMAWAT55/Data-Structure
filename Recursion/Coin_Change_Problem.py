#Knon results going to be greater than [0]*target+1 #initialization
def coin_change(target,coins,known_results):
    min_change=target
    if target in coins :
        known_results[target]=1
        return 1
    elif known_results[target]>0:
        return known_results[target]

    else:
        for coin in [c for c in coins if c<=target] :

            no_coins=1+coin_change(target-coin,coins,known_results)

            if no_coins<min_change:
                min_change=no_coins
                known_results[target]=min_change
    return min_change


if __name__=='__main__':
    print (coin_change(50,[1,2,5],[0]*(50+1)))