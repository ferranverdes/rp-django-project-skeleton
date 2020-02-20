import React from "react";
import useResourceList from "../hooks/useResourceList";
import { USERS_URL } from "../constants/"

const UserList = () => {
  const users = useResourceList(USERS_URL);

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};

export default UserList;
