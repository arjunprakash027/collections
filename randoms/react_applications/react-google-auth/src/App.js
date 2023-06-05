import logo from './logo.svg';
import './App.css';
import React from 'react';
import { useState, useEffect } from 'react';
import { googleLogout,useGoogleLogin } from '@react-oauth/google';
import axios from 'axios';

function App() {


  const [user, setUser] = useState(null);
  const [ profile, setProfile] = useState(null);

  const login = useGoogleLogin({
    onSuccess: (codeResponse) => setUser(codeResponse),
    onError: (error) => console.log('login failed:',error)
  });

  if (user){
  console.log(user['access_token']);
  }
  
  useEffect(() => {
    if (user) {
      axios.get('https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token='+user['access_token'], {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer '+user['access_token']
          }
        })
        .then((response) => {
          setProfile(response['data']);
        }, (error) => {
          console.log(error);
        });
    }
  }, [user]);

  const logout = () => {
    googleLogout();
    setProfile(null);
  };

  if (profile){
    console.log(profile);
  }

  
  return (
    <div>
      <h2> Google login </h2>
      <br />
      <br />
      {profile ? (
        <div>
          <img src={profile['picture']} alt={profile['name']} />
          <h2>Welcome {profile['name']}!</h2>
          <h3>Mail ID : {profile['email']}</h3>
          <br />
          <br />
          <button onClick={()=>logout()}>Logout</button>
        </div>
      ) : (
        <button onClick={()=>login()}>Sign in with google </button>
      )}
    </div>
  );
}

export default App;
