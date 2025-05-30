import React from 'react'
import { Link } from 'react-router-dom'
import { Star } from 'lucide-react'
import useMoviesData from '../hooks/useMoviesData'

const MoviesGrid = () => {
  const { movies, loading } = useMoviesData()

  if (loading) {
    return (
      <div className="movies-container">
        <div style={{ textAlign: 'center', padding: '50px' }}>
          Ładowanie filmów...
        </div>
      </div>
    )
  }

  return (
    <div className="movies-container">
      <div className="movies-grid">
        {movies.slice(0, 12).map(movie => ( // Pokazuje pierwsze 12 filmów
          <div key={movie.id} className="movie-card">
            <div className="movie-image">
              <img 
                src={movie.image} 
                alt={movie.title}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/250x350/d0d0d0/666?text=No+Image'
                }}
              />
              <button className="movie-play">▶</button>
            </div>
            <div className="movie-card-info">
              <h3 className="movie-card-title">{movie.title}</h3>
              <p className="movie-card-subtitle">{movie.subtitle}</p>
              <div className="movie-card-rating">
                <div className="stars">
                  {[...Array(5)].map((_, i) => (
                    <Star 
                      key={i} 
                      size={14} 
                      fill={i < Math.floor(movie.rating) ? "#ffd700" : "#ddd"} 
                      color={i < Math.floor(movie.rating) ? "#ffd700" : "#ddd"}
                    />
                  ))}
                </div>
                <span className="reviews-count">{movie.reviews}</span>
              </div>
              <div className="movie-genre">{movie.genre.split(',')[0]}</div>
            </div>
          </div>
        ))}
      </div>
      
      {/* Footer */}
      <footer className="movies-footer">
        <Link to="/" className="footer-logo">MovieRate</Link>
      </footer>
    </div>
  )
}

export default MoviesGrid