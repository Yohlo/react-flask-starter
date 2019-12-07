import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import Authorization from "./components/Authorization";
import { Success } from "./components/OAuth";
import UserInfo from "./components/UserInfo";
import Metrics from "./components/Metrics";
import Home from "./components/Home";
import "./App.css";

const App = () => <div className="App">
  <div className="App-header">
    <UserInfo />
    <Router>
      <Switch>
        <Route exact path="/">
          <Authorization Component={Home} />
        </Route>
        <Route exact path="/OAuth/Success">
          <Success />
        </Route>
      </Switch>
    </Router>
    <Metrics />
  </div>
</div>

export default App;
