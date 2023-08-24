import './App.css';
import { useState, useEffect } from 'react';
// https://randomuser.me/api
function App() {
  const [counter, setCounter] = useState(0);
  const [data, setData] = useState(null)

  const fetchData = () => {
    fetch("https://randomuser.me/api").then((res) => {
      return res.json()
    }).then(data => {
      // const stringFy = JSON.stringify(data)
      console.log(data)
      setData(data)
    })
  }

  // useEffect(() => {
  //   fetchData()
  // }, []);

  return (
    <div className="App">
      <h1>Counter App</h1>
      <p>{counter}</p>
      <button onClick={() => {
        setCounter(counter + 1)
      }}>Increment</button>
      <button onClick={() => {
        setCounter(counter - 1)
      }}>Decrement</button>

      <button onClick={() => {
        fetchData()
      }}>FetchData</button>

      <div>
        <ul>
        {data.map(elem => {
          <ul key={elem.cell}>{elem.first}</ul>
        })}
        </ul>

      </div>
    </div>
  );
}

export default App;
