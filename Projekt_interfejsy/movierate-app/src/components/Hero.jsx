import React from 'react'
import { Search } from 'lucide-react'

const Hero = () => {
  return (
    <section className="hero">
      <div className="container">
        <div className="hero-content">
          <h1 className="hero-title">
            Discover & Rate Your Favorite Movies
          </h1>
          
          <div className="search-container">
            <input 
              type="text" 
              placeholder="Search for movies or series..." 
              className="search-input"
            />
            <Search className="search-icon" size={20} />
          </div>
          
          <div className="hero-size">
            1920 × 600
          </div>
        </div>
      </div>
    </section>
  )
}

export default Hero