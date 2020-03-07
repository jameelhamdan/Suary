import React from "react";
import { Redirect } from "react-router-dom";

// Layout Types
import { DefaultLayout } from "./layouts";

// Route Views
import BlogOverview from "./views/BlogOverview";
import UserProfileLite from "./views/UserProfileLite";
import AddNewPost from "./views/AddNewPost";
import Errors from "./views/Errors";
import ComponentsOverview from "./views/ComponentsOverview";
import Tables from "./views/Tables";
import BlogPosts from "./views/BlogPosts";

export default [
  {
    path: "/",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: () => <Redirect to="/blog-overview" />
  },
  {
    path: "/blog-overview",
      exact: true,
    strict: true,
    layout: DefaultLayout,
    component: BlogOverview
  },
  {
    path: "/user-profile-lite",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: UserProfileLite
  },
  {
    path: "/add-new-post",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: AddNewPost
  },
  {
    path: "/errors",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Errors
  },
  {
    path: "/components-overview",
    layout: DefaultLayout,
    component: ComponentsOverview
  },
  {
    path: "/tables",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: Tables
  },
  {
    path: "/blog-posts",
    exact: true,
    strict: true,
    layout: DefaultLayout,
    component: BlogPosts
  }
];
