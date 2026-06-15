function LinearSearch(l,v){
    
    for(let i = 0; i<l.length; i++){
        if(v == l[i]){
            return i
        }

    }
    return -1
}

list1 = [6,5,4,3,7,2]
val = 7;
console.log(LinearSearch(list1,val))