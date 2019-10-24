
const CountAllPositive = arr => arr.filter(m => m > 0).length;
const FindMaxElem = arr => Math.max(...arr);


function main(){
    let test = [6,0,-4,5,-1];
    console.log(CountAllPositive(test));
    console.log(FindMaxElem(test));
}

main();
