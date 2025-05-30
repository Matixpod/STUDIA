import React, { useState, useMemo } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Star } from 'lucide-react'
import useMoviesData from '../hooks/useMoviesData'
import FilterSort from './FilterSort'

const MoviesGrid = () => {
  const { movies, loading } = useMoviesData()
  const navigate = useNavigate()
  const [selectedGenre, setSelectedGenre] = useState('all')
  const [sortBy, setSortBy] = useState('popularity')

  // Wyodrębnij unikalne gatunki
  const genres = useMemo(() => {
    const allGenres = new Set()
    movies.forEach(movie => {
      if (movie.genre) {
        movie.genre.split(',').forEach(g => {
          allGenres.add(g.trim())
        })
      }
    })
    return Array.from(allGenres).sort()
  }, [movies])

  // Filtruj i sortuj filmy
  const filteredAndSortedMovies = useMemo(() => {
    let filtered = [...movies]

    // Filtrowanie po gatunku
    if (selectedGenre !== 'all') {
      filtered = filtered.filter(movie => 
        movie.genre && movie.genre.includes(selectedGenre)
      )
    }

    // Sortowanie
    switch (sortBy) {
      case 'rating':
        filtered.sort((a, b) => b.rating - a.rating)
        break
      case 'popularity':
        filtered.sort((a, b) => parseInt(b.reviews) - parseInt(a.reviews))
        break
      case 'newest':
        filtered.sort((a, b) => {
          const yearA = parseInt(a.title.match(/$$(\d{4})$$/)?.[1] || 0)
          const yearB = parseInt(b.title.match(/$$(\d{4})$$/)?.[1] || 0)
          return yearB - yearA
        })
        break
      case 'alphabetical':
        filtered.sort((a, b) => a.title.localeCompare(b.title))
        break
      default:
        break
    }

    return filtered
  }, [movies, selectedGenre, sortBy])

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
      <FilterSort 
        genres={genres}
        selectedGenre={selectedGenre}
        onGenreChange={setSelectedGenre}
        sortBy={sortBy}
        onSortChange={setSortBy}
        type="movies"
      />
      
      <div className="results-info">
        Znaleziono {filteredAndSortedMovies.length} filmów
        {selectedGenre !== 'all' && ` w kategorii: ${selectedGenre}`}
      </div>

      <div className="movies-grid">
        {filteredAndSortedMovies.slice(0, 12).map(movie => (
          <div 
            key={movie.id} 
            className="movie-card"
            onClick={() => navigate(`/movie/${movie.id}`)}
          >
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
      
      {filteredAndSortedMovies.length > 12 && (
        <div className="load-more-container">
          <button className="load-more-btn">
            Pokaż więcej
          </button>
        </div>
      )}
      
      <footer className="movies-footer">
        <Link to="/" className="footer-logo">MovieRate</Link>
      </footer>
    </div>
  )
}

export default MoviesGrid