import React from "react";
import { useState } from "react";

export function ShortUrl () {
    const [Value, setValue] = useState("")
    const [Response, setResponse] = useState("")
  
    const handleChange = (event) => {
      setValue(event.target.value);
    }
  
    const handleSubmit = async (event) => {
        event.preventDefault();
        const data = {"link": Value}
        const result = await fetch("http://localhost:8000/new", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        if (result.ok)
        {
            const resultJSON = await result.json()
            setResponse("http://localhost:8000/" + resultJSON.hash)
            return
        }
        const resultJSON = await result.json()
        setResponse(resultJSON.detail[0].msg)
    }

    return (
    <div>
        <h1>ShortURL</h1>
        <p>Create your shorter url right now !</p>
        <form onSubmit={handleSubmit}>
            <input type="text" value={Value} onChange={handleChange} />
        <input type="submit" value="Create" />
        <h2>{Response}</h2>
        </form>
    </div>
    );
  }

