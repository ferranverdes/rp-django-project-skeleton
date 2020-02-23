import React from "react";
import useResourceList from "../hooks/useResourceList";
import { COURSES_URL } from "../constants/";

const UserList = () => {
  const courses = useResourceList(COURSES_URL);
  console.log(courses);

  return <ul>HOLA</ul>;
};

export default UserList;
