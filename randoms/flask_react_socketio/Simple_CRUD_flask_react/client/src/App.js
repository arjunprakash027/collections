import Greet from './pages/greeting';
import About from './pages/about';
import Navbar from './components';

import { BrowserRouter as Router, Routes, Route } 
        from 'react-router-dom';

import React from 'react';
import './App.css';

function App() {

  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Greet />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Router>
  );
};

export default App;
