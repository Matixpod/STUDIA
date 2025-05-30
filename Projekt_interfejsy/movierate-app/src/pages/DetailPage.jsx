import { useParams, useNavigate } from 'react-router-dom'
import { useState, useEffect } from 'react'
import { Star, Clock, Calendar, Users, ArrowLeft } from 'lucide-react'
import useMoviesData from '../hooks/useMoviesData'
import useTVShowsData from '../hooks/useTVShowsData'

const DetailPage = ({ type }) => {
  const { id } = useParams()
  const navigate = useNavigate()
  const { movies } = useMoviesData()
  const { tvShows } = useTVShowsData()
  const [item, setItem] = useState(null)

  useEffect(() => {
    if (type === 'movie' && movies.length > 0) {
      const movie = movies.find(m => m.id === parseInt(id))
      setItem(movie)
    } else if (type === 'tvshow' && tvShows.length > 0) {
      const show = tvShows.find(s => s.id === parseInt(id))
      setItem(show)
    }
  }, [id, type, movies, tvShows])

  if (!item) {
    return (
      <div className="detail-loading">
        Ładowanie...
      </div>
    )
  }

  return (
    <div className="detail-page">
      <button className="back-button" onClick={() => navigate(-1)}>
        <ArrowLeft size={20} />
        Powrót
      </button>

      <div className="detail-container">
        <div className="detail-poster">
          <img 
            src={item.image} 
            alt={item.title}
            onError={(e) => {
              e.target.src = 'https://via.placeholder.com/400x600/d0d0d0/666?text=No+Image'
            }}
          />
        </div>

        <div className="detail-info">
          <h1 className="detail-title">{item.title}</h1>
          
          <div className="detail-meta">
            <div className="detail-rating">
              <div className="stars-large">
                {[...Array(5)].map((_, i) => (
                  <Star 
                    key={i} 
                    size={24} 
                    fill={i < Math.floor(item.rating) ? "#ffd700" : "#ddd"} 
                    color={i < Math.floor(item.rating) ? "#ffd700" : "#ddd"}
                  />
                ))}
              </div>
              <span className="rating-text">{(item.rating * 2).toFixed(1)}/10</span>
              <span className="votes-text">{item.reviews}</span>
            </div>

            <div className="detail-badges">
              {item.genre && (
                <span className="detail-badge">
                  {item.genre.split(',')[0]}
                </span>
              )}
              {item.runtime && (
                <span className="detail-badge">
                  <Clock size={14} />
                  {item.runtime}
                </span>
              )}
              {item.certificate && (
                <span className="detail-badge">
                  {item.certificate}
                </span>
              )}
            </div>
          </div>

          {item.overview && (
            <div className="detail-overview">
              <h2>Opis</h2>
              <p>{item.overview}</p>
            </div>
          )}

          {item.subtitle && (
            <div className="detail-director">
              <strong>Reżyseria:</strong> {item.subtitle.replace('feat. ', '')}
            </div>
          )}

          {item.stars && item.stars.length > 0 && (
            <div className="detail-cast">
              <h3>Obsada</h3>
              <div className="cast-list">
                {item.stars.map((star, index) => (
                  <span key={index} className="cast-member">
                    <Users size={16} />
                    {star}
                  </span>
                ))}
              </div>
            </div>
          )}

          {item.gross && (
            <div className="detail-gross">
              <strong>Box Office:</strong> {item.gross}
            </div>
          )}

          {type === 'tvshow' && item.episodeRuntime && (
            <div className="detail-episode">
              <Calendar size={16} />
              <span>Długość odcinka: {item.episodeRuntime}</span>
            </div>
          )}

          <div className="detail-actions">
            <button className="btn-watch">Oglądaj teraz</button>
            <button className="btn-trailer">Zwiastun</button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default DetailPage