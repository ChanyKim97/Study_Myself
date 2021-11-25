import React, {useState} from "react";

const Counter = (props) =>{
    const [count, setCount] = useState(0);

    const increment = () =>{
        setCount(count+1);
    }

    //존재하면 전 존재안하면 후
    const clickString = props.click || 'Click';

    return (
        <button onClick={increment}>
            {clickString} {count}
        </button>
    );
}

export default Counter;