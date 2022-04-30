// var input = require('fs').readFileSync('/dev/stdin', 'utf8');
// var lines = input.split('\n');

var lines =[10 ,18];
x = parseInt(lines.shift())
y = parseInt(lines.shift())

if(x>y){
    while(y<x){
        if(y%5==2 || y%5 ==3){
            console.log(y);
        }   
        y++;
    }
}else{
    while(x<y){
        if(x%5==2 || x%5 ==3){
            console.log(x);  
           
            }
    x++;            
        }
}




