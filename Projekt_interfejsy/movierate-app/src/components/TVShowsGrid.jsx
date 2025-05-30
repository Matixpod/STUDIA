import React, { useState, useMemo } from 'react'
import { useNavigate } from 'react-router-dom'
import { Star } from 'lucide-react'
import useTVShowsData from '../hooks/useTVShowsData'
import FilterSort from './FilterSort'

const TVShowsGrid = () => {
  const { tvShows, loading } = useTVShowsData()
  const navigate = useNavigate()
  const [selectedGenre, setSelectedGenre] = useState('all')
  const [sortBy, setSortBy] = useState('popularity')

  // Wyodrębnij unikalne gatunki
  const genres = useMemo(() => {
    const allGenres = new Set()
    tvShows.forEach(show => {
      if (show.genre) {
        show.genre.split(',').forEach(g => {
          allGenres.add(g.trim())
        })
      }
    })
    return Array.from(allGenres).sort()
  }, [tvShows])

  // Filtruj i sortuj seriale
  const filteredAndSortedShows = useMemo(() => {
    let filtered = [...tvShows]

    // Filtrowanie po gatunku
    if (selectedGenre !== 'all') {
      filtered = filtered.filter(show => 
        show.genre && show.genre.includes(selectedGenre)
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
        filtered.sort((a, b) => a.title.localeCompare(b.title)) // Możesz dostosować jeśli masz daty
        break
      case 'alphabetical':
        filtered.sort((a, b) => a.title.localeCompare(b.title))
        break
      default:
        break
    }

    return filtered
  }, [tvShows, selectedGenre, sortBy])

  if (loading) {
    return (
      <div className="tv-shows-container">
        <div style={{ textAlign: 'center', padding: '50px' }}>
          Ładowanie seriali...
        </div>
      </div>
    )
  }

  return (
    <div className="tv-shows-container">
      <FilterSort 
        genres={genres}
        selectedGenre={selectedGenre}
        onGenreChange={setSelectedGenre}
        sortBy={sortBy}
        onSortChange={setSortBy}
        type="tvshows"
      />
      
      <div className="results-info">
        Znaleziono {filteredAndSortedShows.length} seriali
        {selectedGenre !== 'all' && ` w kategorii: ${selectedGenre}`}
      </div>

      <div className="tv-shows-grid">
        {filteredAndSortedShows.slice(0, 12).map(show => (
          <div 
            key={show.id} 
            className="tv-show-card"
            onClick={() => navigate(`/tv-show/${show.id}`)}
            style={{ cursor: 'pointer' }}
          >
            <div className="tv-show-image">
              <img 
                src={show.image} 
                alt={show.title}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/250x350/d0d0d0/666?text=No+Image'
                }}
              />
              <button 
                className="tv-show-play"
                onClick={(e) => {
                  e.stopPropagation()
                }}
              >
                ▶
              </button>
            </div>
            <div className="tv-show-info">
              <h3 className="tv-show-title">{show.title}</h3>
              <p className="tv-show-subtitle">{show.subtitle}</p>
              <div className="tv-show-rating">
                <div className="stars">
                  {[...Array(5)].map((_, i) => (
                    <Star 
                      key={i} 
                      size={14} 
                      fill={i < Math.floor(show.rating) ? "#ffd700" : "#ddd"} 
                      color={i < Math.floor(show.rating) ? "#ffd700" : "#ddd"}
                    />
                  ))}
                </div>
                <span className="reviews-count">{show.reviews}</span>
              </div>
              <div className="tv-show-genre">{show.genre.split(',')[0]}</div>
              {show.episodeRuntime && (
                <div className="tv-show-episode-time">
                  Odcinek: {show.episodeRuntime}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
      
      {filteredAndSortedShows.length > 12 && (
        <div className="load-more-container">
          <button className="load-more-btn">
            Pokaż więcej
          </button>
        </div>
      )}
    </div>
  )
}

export default TVShowsGrid