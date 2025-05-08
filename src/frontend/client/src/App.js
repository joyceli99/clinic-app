import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react'; // Import useState and useEffect

function App() {
  const [message, setMessage] = useState(""); // State to store the message

  // useEffect to fetch data when the component mounts
  useEffect(() => {
    fetch("http://localhost:8000/api/hello") // Assuming FastAPI runs on port 8000
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error("Error fetching data: ", error));
  }, []); // Empty dependency array means this effect runs once on mount

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {/* Display the message from the backend */}
        <p>Message from Backend: {message}</p>
      </header>
    </div>
  );
}

export default App;
