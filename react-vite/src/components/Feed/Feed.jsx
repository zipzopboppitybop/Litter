import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch, useSelector } from "react-redux";
import { Navigate, useNavigate } from "react-router-dom";

function Feed() {
  return (
    <>
      <h1>Feed</h1>
    </>
  );
}

export default Feed;