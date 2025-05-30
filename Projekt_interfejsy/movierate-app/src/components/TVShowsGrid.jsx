import React from 'react'
import { Star } from 'lucide-react'
import useTVShowsData from '../hooks/useTVShowsData'

const TVShowsGrid = () => {
  const { tvShows, loading } = useTVShowsData()

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
      <div className="tv-shows-grid">
        {tvShows.slice(0, 12).map(show => ( // Pokazuje pierwsze 12 seriali
          <div key={show.id} className="tv-show-card">
            <div className="tv-show-image">
              <img 
                src={show.image} 
                alt={show.title}
                onError={(e) => {
                  e.target.src = 'https://via.placeholder.com/250x350/d0d0d0/666?text=No+Image'
                }}
              />
              <button className="tv-show-play">▶</button>
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
    </div>
  )
}

export default TVShowsGrid