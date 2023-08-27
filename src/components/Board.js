import React from "react";
import Column from "./Column";

const Board = ({stages, tasks}) => {
    return (
        <div>
            {stages.map((stage, index) => {
                <Column key={index} stage={stage} tasks={tasks}/>
            })}
        </div>
    )
}

export default Board