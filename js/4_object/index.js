let code = {
    name : '코드잇',
    bornYear : 2017,
    isVeryNice : true,
    'a a a': null,
    bestCourse:{
        title: '자바스크립',
        lan: 'javascript'
    }
}

console.log(code['a a a']);

console.log(code.name);
code.ceo = 'kim';
console.log(code)

//delete code.bestCourse;

//method
let greetings = {
    sayHello : function(){
        console.log('Hello')
    },
    sayHi : function(){
        console.log('Hi')
    }
}

greetings.sayHello();
greetings['sayHi']();

for(let key in code){
    console.log(key)
}

//Date
let myDate =new Date();
console.log(myDate)