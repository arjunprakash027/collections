import React, { useState, useEffect } from "react";

function Greet() {
    const [message, setMessage] = useState([])
  
    useEffect(() => {
      fetch("http://127.0.0.1:5000/greetings")
      .then(response => response.json())
      .then(data => {setMessage(data);
      console.log(data);})
    }, []);
  
    return (
        <div>
          <h1>{message.message}</h1>
        </div>
    );
  };

export default Greet;
