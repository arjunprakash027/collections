import react from 'react';

const UserList = ({ users }) => {
    return (
        <div>
            <h2> registered users </h2>
            <ul>
                {users.map((user,index) => (
                    <li key={index}>{user.data}</li>
                ))}
            </ul>
        </div>
    );
};

export default UserList;