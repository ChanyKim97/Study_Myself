console.log(2 ** 3)

console.log(3.14)

console.log('\'\'\'')

console.log(2>1)

console.log(1 == 1)
console.log(1 != 1)
console.log(3 !== 3)

console.log(typeof 101)
console.log(typeof true)
console.log(typeof 'true')
console.log(typeof typeof 101)

//자바스크립트 자동 형변환
console.log('4' - true)
//더하기 제외한 산술연산자 모두 자동
//관계 비교연산 (<, <=, >, >=)

//같음 비교 연산(===, !==, ==, !=)
//일치 -> 자동형변환 없음
console.log(1 === '1') //false
//동등 -> 자동 형변환 일어남
console.log(1 == '1') //true

//template String
let year = 2021;
console.log(`생년 ${year}년`)

//null, undefined
//null - 값이 없다 의도적인 없음
//undefined - 값이 없는 것을 확인하다 차음부터 아무것도 없음
let code
console.log(code) // undefined
code = null
console.log(code) // null

console.log(null == undefined) //true
console.log(null === undefined) //false
