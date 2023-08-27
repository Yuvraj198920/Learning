import React from 'react';
import Task from './Task';
const Column = ({stage, tasks}) => {
    const filteredTasks = tasks.filter(task => task.stage === stage)
    return (
        <div className='column'>
            <h2>{stage}</h2>
            {filteredTasks.map((task, index) => {
                <Task key={index} task={task.name}/>
            })}
        </div>
    )
}

export default Column;