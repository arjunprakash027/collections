import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';
import UserList from './UserList';

const App = () => {
  const [users, setUsers] = useState([]);
  const [username, setUsername] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    if (socket) {
      socket.on('user_registered', (username) => {
        setUsers((prevUsers) => [...prevUsers, username]);
      });

      return () => {
        socket.disconnect();
      };
    }
  }, [socket]);

  const handleConnect = () => {
    const newSocket = io('http://localhost:5000'); // Replace with your backend URL
    setSocket(newSocket);
    setIsConnected(true);

    newSocket.on('connect', () => {
      console.log('Connected to backend');
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (socket) {
      socket.emit('register', username);
      setUsername('');
    }
  };

  return (
    <div>
      <h1>React Socket.IO User Registration</h1>
      {isConnected && socket ? (
        <div>
          <UserList users={users} />
          <form onSubmit={handleSubmit}>
            <input
              type="text"
              placeholder="Enter username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
            <button type="submit">Register</button>
          </form>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect to Backend</button>
      )}
    </div>
  );
};

export default App;