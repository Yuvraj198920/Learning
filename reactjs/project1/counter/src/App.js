import './App.css';
import { useState } from 'react';
// https://randomuser.me/api
function App() {
  const [counter, setCounter] = useState(0);

  return (
    <div className="App">
      <h1>Counter App</h1>
      <p>{counter}</p>
      <button onClick={() => {
        setCounter(counter+1)
      }}>Increment</button>
      <button onClick={() => {
        setCounter(counter-1)
      }}>Decrement</button>
    </div>
  );
}

export default App;
