import React, {useState} from "react";

function App() {
  const [text, setText] = useState('Before');

  const onSubmit = ()=>{
    alert('Submitted');
  };

  const onKeyUp = (e) => {
    //13이면 enter입력의 경우임
    if(e.keyCode === 13) {
      onSubmit();
    }
  }

  //let text = 'Before';

  const updateText = () =>{
    //text = 'After';
    setText('After');
    console.log(text); //Before임 그래서 useEffect가 필요함
  }

  return (
    <div className="App">
      <input onKeyUp={onKeyUp} />
      <button onClick = {onSubmit}>Submit</button>

      <br/><br/>

      <span>{text}</span>
      <button onClick={updateText}>Update</button>
    </div>
  );
}

export default App;
