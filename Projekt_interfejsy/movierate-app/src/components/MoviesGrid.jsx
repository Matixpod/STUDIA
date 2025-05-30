import React from 'react'
import { Link } from 'react-router-dom'
import { Star } from 'lucide-react'

const MoviesGrid = () => {
  const movies = [
    {
      id: 1,
      title: "Skazani na Shawshank (1994)",
      subtitle: "feat. Frank Darabont",
      rating: 4.9,
      reviews: "5.9k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Shawshank"
    },
    {
      id: 2,
      title: "Ted 2 (2015)",
      subtitle: "feat. Seth MacFarlane",
      rating: 4.3,
      reviews: "3.2k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Ted+2"
    },
    {
      id: 3,
      title: "Mroczny Rycerz (2008)",
      subtitle: "feat. Christopher Nolan",
      rating: 4.8,
      reviews: "4.5k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Dark+Knight"
    },
    {
      id: 4,
      title: "Pulp Fiction (1994)",
      subtitle: "feat. Quentin Tarantino",
      rating: 4.7,
      reviews: "4.2k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Pulp+Fiction"
    },
    {
      id: 5,
      title: "Forrest Gump (1994)",
      subtitle: "feat. Robert Zemeckis",
      rating: 4.6,
      reviews: "3.8k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Forrest+Gump"
    },
    {
      id: 6,
      title: "Podziemny krąg (1999)",
      subtitle: "feat. David Fincher",
      rating: 4.5,
      reviews: "3.5k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Fight+Club"
    },
    {
      id: 7,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Gavin Hood",
      rating: 4.2,
      reviews: "2.9k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=W+Pustyni"
    },
    {
      id: 8,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Hans Lampe",
      rating: 4.3,
      reviews: "2.1k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=W+Pustyni+2"
    },
    {
      id: 9,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Dirk Lampe",
      rating: 4.1,
      reviews: "1.9k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Placeholder+1"
    },
    {
      id: 10,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Hans Lampe",
      rating: 4.0,
      reviews: "1.5k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Placeholder+2"
    },
    {
      id: 11,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Clyde Lampe",
      rating: 4.2,
      reviews: "2.3k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Placeholder+3"
    },
    {
      id: 12,
      title: "W Pustyni i Puszczy (1997)",
      subtitle: "feat. Hans Lampe",
      rating: 3.9,
      reviews: "1.7k recenzji",
      image: "https://via.placeholder.com/250x350/d0d0d0/666?text=Placeholder+4"
    }
  ]

  return (
    <div className="movies-container">
      <div className="movies-grid">
        {movies.map(movie => (
          <div key={movie.id} className="movie-card">
            <div className="movie-image">
              <img src={movie.image} alt={movie.title} />
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