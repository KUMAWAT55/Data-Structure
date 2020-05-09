#Complexity O(n)
def pair_sum(array,num):
    if len(array)<2:
        return "No pairs"

    seen=set()
    output=set()
    for element in array :
        target=num-element
        print(element)
        print(target)
        if target not in seen:
            seen.add(element)
            print("seen:",seen)
        else:
            output.add((min(element,target),max(element,target)))
            print(output)
    return output

if __name__ == "__main__":
    print(pair_sum([1,3,2,2],4))