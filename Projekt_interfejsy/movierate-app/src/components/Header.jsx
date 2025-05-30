import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Search } from 'lucide-react'
import Settings from './Settings'

const Header = () => {
  const location = useLocation()
  
  return (
    <header className="header">
      <div className="header-container">
        <div className="logo">
          <span className="desktop-text">Desktop</span>
          <Link to="/" className="logo-text">MovieRate</Link>
        </div>
        
        <nav className="nav-menu">
          <Link 
            to="/tv-shows" 
            className={`nav-link ${location.pathname === '/tv-shows' ? 'active' : ''}`}
          >
            TV Shows
          </Link>
          <Link 
            to="/movies" 
            className={`nav-link ${location.pathname === '/movies' ? 'active' : ''}`}
          >
            Movies
          </Link>
          <a href="#" className="nav-link">Leave Review</a>
          <a href="#" className="nav-link">Order Review</a>
        </nav>
        
        <div className="header-actions">
          <Settings />
          <button className="btn-signin">Sign In</button>
          <button className="btn-start">Start Free</button>
        </div>
      </div>
    </header>
  )
}

export default Header