import './App.css';
import Board from './components/Board';
function App() {
  const stages = ['To Do', 'In Progress', 'Done']

  const tasks = [{ name: 'Task 1', stage: 'To Do' },
  { name: 'Task 2', stage: 'To Do' },
  {name: 'Task 3', stage: 'In Progress'}]

  return (
    <div className="app">
      <Board stages={stages} tasks={tasks}/>
    </div>
  );
}

export default App;
