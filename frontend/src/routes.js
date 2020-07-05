import React from "react";

// Layout Types
import { DefaultLayout } from "layouts";

// Route Views
import Login from "views/auth/Login";
import Logout from "views/auth/Logout";
import Register from "views/auth/Register";
import Home from "views/home/Home";

//Users
import UserDetail from "views/user/Detail";
import UserProfileRedirect from "views/user/ProfileRedirect";

// Posts
import PostDetail from "views/posts/Detail";


export default [
  {
    path: "/",
    logged_in_only: false,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Home
  },
  {
    path: "/login",
    logged_in_only: false,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Login
  },
  {
    path: "/register",
    logged_in_only: false,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Register
  },
  {
    path: "/logout",
    logged_in_only: true,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Logout
  },
  {
    path: "/profile",
    logged_in_only: true,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: UserProfileRedirect
  },
  {
    path: "/profile/:username?",
    logged_in_only: false,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: UserDetail
  },
  {
    path: "/post/:id",
    logged_in_only: false,
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: PostDetail
  },
];
