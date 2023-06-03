import React from 'react';
import './App.css';
import { useState } from 'react';

function MyButton(){
  // react state
  const [count, setCount] = useState(0);

  function HandleClick(){
    //alert("Clicked");
    setCount(count + 1);
  }

  return(
    <div>
    <button onClick = {HandleClick} >Clicked {count} Times</button>
    </div>
  );
}

function Button2({count,onClick}){

  return(
    <div>
      <button onClick = {onClick}>Clicked {count} Times</button>
    </div>
  )

}

const SfNav = ({ showProfile, profilePicture }) => {
  if (!showProfile) {
    return null;
  }

  return (
    <div>
      <img className='Profile-pic' src={profilePicture} alt="Profile picture" style = {{width: 90, height: 90}} />
    </div>
  );
};

function Navbari(){
  return(
      <div>
              <SfNav showProfile={true} profilePicture='https://i.pinimg.com/736x/7f/79/6d/7f796d57218d9cd81a92d9e6e8e51ce4--free-avatars-online-profile.jpg' />
      </div>
  );
}


const user = {
  name:"Arjun",
  profilePicUrl:"https://avatars.githubusercontent.com/u/59870744?v=4"
}

function Profile(){
  return(
    <div>
      <h1>Hi {user.name}</h1>
      <img 
        className = "profile-pic"
        src = {user.profilePicUrl}
        alt = {user.name}
        style = {{width: 90, height: 90}}
      />
    </div>
  );
}

//conditional rendering
function Profile2(){
  return(
    <div>
      <h1>Hi {user.name}</h1>
        <img
          className = "profile-pic"
          src = {user.profilePicUrl}
          alt = {user.name}
          style = {{width: 90, height: 90}}
        /> 
    </div>
  );
}

let content;
let display = false;
if(display){
  content = <Profile2 />;
}
else{
  content = <p>Not displaying</p>;
}


//rendering lists
const posts = [
  { id: 1, title: "Hello World",isPytohn:false, content: "Welcome to learning React!" },
  { id: 2, title: "Installation",isPython:false, content: "You can install React from npm." },
  { id: 3, title: "Flask",isPython:true, content: "Learn flask from me" },
  { id: 4, title: "Installation",isPython:true, content: "Pip install flask" },
];

function Blog(){
  const blogs = posts.map(post => 
    <div>
      <h3
      style = {{
        color: post.isPython ? "green" : "blue"
      }}>
        {post.title}
      </h3>

      <p>{post.content}</p>

    </div>
    );

    return(
      <div>
        <h1>Welcome to my blog</h1>
        {blogs}
      </div>
    );
}

//post component
const twitter_post = [
  {id:1,post:"What in the world is react??",comments:["I dont know","I dont care","I dont want to know","I dont want to care","I dont want to know or care","I dont want to care or know"]},
  {id:2,post:"What in the world is flask??",comments:["I dont know","I dont care","I dont want to know","I dont want to care","I dont want to know or care","I dont want to care or know"]},
]


function Post(){
  const posts = twitter_post.map(post =>
    <div>
      <h3>{post.post}</h3>
      <ul>
        {post.comments.map((comment) =>
          <li>{comment}</li> 
          )}
      </ul>
    </div>
    );
    

    return(
      <div>
        {posts}
      </div>
    )
}


export default function App(){

  const [count2, setCount2] = useState(0);

  function handleclick2(){
    setCount2(count2 + 1);
  }

  return(
    <div>
      <Navbari />
      <h1>My App</h1>
      <MyButton />
      <MyButton />
      <Button2 count = {count2} onClick = {handleclick2} />
      <Button2 count = {count2} onClick = {handleclick2} />
      <Profile />
      <Blog />
      <Post />
      {content}
    </div>
  );
}

