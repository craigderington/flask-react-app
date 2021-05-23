import logo from './logo.svg';
import './App.css';
import React, {useEffect, useState} from 'react';

function App() {
  const [currentTime, setCurrentTime] = useState(0);
  useEffect(() => {
      fetch("/api/getdate").then(res => res.json()).then(data => {
        setCurrentTime(data.timestamp);
      });
  }, []);
  
  return (
    <div className="App">
      <p>The current date and time is {currentTime}.</p>
    </div>
  );
}

export default App;
