import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';

function App() {
  return (
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <Link className="navbar-brand d-flex align-items-center" to="/">
            <img src="/octofitapp-small.png" alt="Octofit Logo" className="me-2" style={{height: '40px'}} />
            Octofit Tracker
          </Link>
          <div className="navbar-nav">
            <Link className="nav-link" to="/activities">Activities</Link>
            <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
            <Link className="nav-link" to="/teams">Teams</Link>
            <Link className="nav-link" to="/users">Users</Link>
            <Link className="nav-link" to="/workouts">Workouts</Link>
          </div>
        </div>
      </nav>
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={
            <div className="container">
              <div className="card mt-5 shadow">
                <div className="card-body text-center">
                  <h1 className="display-4">Welcome to Octofit Tracker</h1>
                  <p className="lead">Track your fitness activities, manage teams, and compete on the leaderboard!</p>
                  <div className="row">
                    <div className="col-md-4">
                      <div className="card shadow">
                        <div className="card-body">
                          <h5 className="card-title">Activities</h5>
                          <p className="card-text">Log and track your fitness activities.</p>
                          <Link className="btn btn-primary" to="/activities">View Activities</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-4">
                      <div className="card shadow">
                        <div className="card-body">
                          <h5 className="card-title">Leaderboard</h5>
                          <p className="card-text">See how you rank against others.</p>
                          <Link className="btn btn-primary" to="/leaderboard">View Leaderboard</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-4">
                      <div className="card shadow">
                        <div className="card-body">
                          <h5 className="card-title">Teams</h5>
                          <p className="card-text">Create and manage your teams.</p>
                          <Link className="btn btn-primary" to="/teams">View Teams</Link>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div className="row mt-3">
                    <div className="col-md-6">
                      <div className="card shadow">
                        <div className="card-body">
                          <h5 className="card-title">Users</h5>
                          <p className="card-text">Manage user profiles.</p>
                          <Link className="btn btn-primary" to="/users">View Users</Link>
                        </div>
                      </div>
                    </div>
                    <div className="col-md-6">
                      <div className="card shadow">
                        <div className="card-body">
                          <h5 className="card-title">Workouts</h5>
                          <p className="card-text">Plan and track your workouts.</p>
                          <Link className="btn btn-primary" to="/workouts">View Workouts</Link>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          } />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
