let millionaire = 1000000000;

let mynum = 1e9;
//10의 9승을 곱함
console.log(millionaire)
console.log(mynum)

//다양한 진수 표현
let hex1 = 0xff;
let cotal = 0o377;
let bin = 0b111;

let myNum = 0.3591;
console.log(typeof myNum.toFixed(9))
console.log(+myNum.toFixed(9))

//toString(2) 2진수로 바꾸기
//정수형으로 쓰고싶으면 255..toString 이렇게 써야함

let x = 0.1+0.2
//cosonle.log(x) // 0.30000000000000000004
console.log(x.toFixed(1))

 //참조형 복사하기
 let array1= [1,2,3]
 let array2 = array1
 let array3 = array1.slice()

 let course1 = {
     title: 'python course',
     lan: 'python'
 };

 let course2 = course1
 let course3 = Object.assign({}, course1)
 //이 방법 외에도 for..in 문으로 표현 가능

//  for (let key in course1){
//      course4[key] = course1
//  }
function cloneObject(object){
    let temp = {}

    for(let key in object){
        temp[key] = object[key]
    }
    
    return temp
}

course4 = cloneObject(course1)

//근데 객체안에 또 참조형변수인 배열이 들어가면 이렇게 해봤자 주소값이 복사됨
//인지할 것

console.log(70000/30000)