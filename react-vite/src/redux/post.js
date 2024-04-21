const GET_POSTS = 'post/GET_POSTS';

const getPosts = (posts) => ({
  type: GET_POSTS,
  payload: posts
});

export const thunkGetPosts = () => async (dispatch) => {
  const response = await fetch("/api/posts/");

  if (response.ok) {
    const posts = await response.json();
    dispatch(getPosts(posts));
  }
}

const initialState = { posts: null };

function postreducer(state = initialState, action) {
  switch (action.type) {
    case GET_POSTS:
      return { ...state, posts: action.payload };
    default:
      return state;
  }
}

export default postreducer;
