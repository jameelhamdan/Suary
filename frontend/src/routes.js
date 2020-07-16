import React from "react";

// Layout Types
import { DefaultLayout } from "layouts";

// Route Views

// Auth
import Login from "views/auth/Login";
import Logout from "views/auth/Logout";
import Register from "views/auth/Register";

// Home
import Home from "views/home/Home";
import Search from "views/home/Search";

//Users
import UserDetail from "views/user/Detail";
import UserProfileRedirect from "views/user/ProfileRedirect";

// Posts
import PostDetail from "views/posts/Detail";

/*
  TODO: for now all views are logged in only,
  later specify permissions for each view and permission for actions and such
*/

export default [
  {
    path: "/",
    logged_in_only: true,
    exact: true,
    strict: false,
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
    strict: false,
    layout: DefaultLayout,
    component: Register
  },
  {
    path: "/logout",
    logged_in_only: true,
    exact: true,
    strict: false,
    layout: DefaultLayout,
    component: Logout
  },
  {
    path: "/profile",
    logged_in_only: true,
    exact: true,
    strict: false,
    layout: DefaultLayout,
    component: UserProfileRedirect
  },
  {
    path: "/profile/:username?",
    logged_in_only: true,
    exact: false,
    strict: false,
    layout: DefaultLayout,
    component: UserDetail
  },
  {
    path: "/post/:id",
    logged_in_only: true,
    exact: false,
    strict: false,
    layout: DefaultLayout,
    component: PostDetail
  },
];
