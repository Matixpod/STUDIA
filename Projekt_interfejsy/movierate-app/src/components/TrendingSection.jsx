import React from 'react'
import { Star } from 'lucide-react'
import useMoviesData from '../hooks/useMoviesData'

const TrendingSection = () => {
  const { movies, loading } = useMoviesData()

  if (loading) {
    return (
      <section className="trending-section">
        <h2 className="section-title">Trending Now</h2>
        <div style={{ textAlign: 'center', padding: '50px' }}>
          Ładowanie...
        </div>
      </section>
    )
  }

  // Wybierz 3 najlepiej oceniane filmy
  const trendingMovies = movies
    .sort((a, b) => b.rating - a.rating)
    .slice(0, 3)

  return (
    <section className="trending-section">
      <h2 className="section-title">Trending Now</h2>
      
      <div className="trending-grid">
        {trendingMovies.map(movie => (
          <div key={movie.id} className="trending-card">
            <div className="movie-placeholder">
              <img 
                src={movie.image} 
                alt={movie.title}
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                onError={(e) => {
                  e.target.style.display = 'none'
                  e.target.parentElement.innerHTML = '400 × 600'
                }}
              />
            </div>
            <h3 className="movie-title">{movie.title}</h3>
            <div className="movie-info">
              <div className="rating">
                <Star size={16} fill="#ffd700" color="#ffd700" />
                <span>{movie.rating.toFixed(1)}</span>
              </div>
              <span className="category">{movie.genre.split(',')[0]}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default TrendingSection