function SelectionSort(l){

    let start, minpos, i, temp;
    for (start = 0; start < l.length; start++){

        minpos = start
        for(i = start; i<l.length; i++){
            if(l[i] < l[minpos]){
                minpos = i
            }
        }
        temp = l[start];
        l[start] = l[minpos];
        l[minpos] = temp
    }
    return l
}

let list1 = [9,2,3,7,5,8,4,6]
console.log(SelectionSort(list1))



