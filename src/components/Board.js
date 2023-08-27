import React from "react";
import Stage from "./Stage";

function Board ({stages, tasks}) {

    return (
        <div className="Board">
            {stages.map((stage, index) => {
                return <Stage key={index} stage={stage} tasks={tasks}/>
            })}
        </div>
    )
}

export default Board