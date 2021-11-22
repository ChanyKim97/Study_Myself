let course = [
    '자바',
    'git',
    '컴퓨터'
]

console.log(course[0])

console.log(course.length)

//splice 삭제
course.splice(2) //2번 index 뒤 모두삭제
//course.splice(2, 1) //2번 index부터 1개 삭제
//course.splice(2, 1, 'Nice') 2번 index부터 1개 삭제후 추가 이거 이용해 2번째 para 0 으로 수정해서 추가만도 가능
console.log(course)

//shift()   배열 1번째 삭제
//pop()     배열 마지막 삭제
//unshift() 배열 1번째 추가
//push()    배열 마지막 추가

for (let element of course){
    console.log(element);
}

for (let index in course){
    console.log(index);
    console.log(course[index]);
}

let votes = [
    '이재식', '이재식', '이규하', '이규하', '이규하',
    '이재식', '이재식', '이규하', '이규하', '이재식',
    '이규하', '이규하', '이규하', '이규하', '이재식',
    '이재식', '이규하', '이재식', '이재식', '이재식',
    '이재식', '이재식', '이규하', '이규하', '이규하',
    '이규하', '이규하', '이재식', '이규하', '이규하',
    '이규하', '이규하', '이재식', '이규하', '이규하',
    '이규하', '이재식', '이재식', '이재식', '이규하',
  ];

  let voteCounter = {};

  for (let name of votes){
    if (name in voteCounter) {
        voteCounter[name]+= 1;
    } else {
        voteCounter[name] = 1;
    }
  }

  