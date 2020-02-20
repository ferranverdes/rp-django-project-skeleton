import React from "react";
import useResourceList from "../hooks/useResourceList";
import { POSTS_URL } from "../constants/"

const PostList = () => {
  const posts = useResourceList(POSTS_URL);

  return (
    <ul>
      {posts.map(post => (
        <li key={post.id}>{post.title}</li>
      ))}
    </ul>
  );
};

export default PostList;
