import React from 'react'
import { Star } from 'lucide-react'

const TVShowsGrid = () => {
  const shows = [
    {
      id: 1,
      title: "The Last of Us (2023)",
      subtitle: "feat. Craig Mazin, Neil Druckmann",
      rating: 4.5,
      reviews: "4.5k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 2,
      title: "Breaking Bad (2008 - 2013)",
      subtitle: "feat. Vince Gilligan",
      rating: 5,
      reviews: "3.2k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 3,
      title: "Biuro (2005 - 2013)",
      subtitle: "feat. Ricky Gervais, Stephen Merchant",
      rating: 4.3,
      reviews: "2.8k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 4,
      title: "Peaky Blinders (2013 - 2022)",
      subtitle: "feat. Steven Knight",
      rating: 4.7,
      reviews: "4.1k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 5,
      title: "Ted Lasso (2020)",
      subtitle: "feat. Brendan Hunt, Joe Kelly",
      rating: 4.6,
      reviews: "1.9k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 6,
      title: "Czas honoru (2008 - 2014)",
      subtitle: "feat. Michał Kwieciński",
      rating: 4.2,
      reviews: "2.3k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 7,
      title: "Yellowstone (2018 - 2024)",
      subtitle: "feat. Taylor Sheridan, John Linson",
      rating: 4.4,
      reviews: "3.5k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 8,
      title: "Lucyfer (2016 - 2021)",
      subtitle: "feat. Tom Kapinos",
      rating: 4.3,
      reviews: "5.2k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 9,
      title: "Euforia (2019)",
      subtitle: "feat. Sam Levinson",
      rating: 4.1,
      reviews: "3.8k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 10,
      title: "Ślepnąc od świateł (2018)",
      subtitle: "feat. Krzysztof Skonieczny",
      rating: 4.0,
      reviews: "1.5k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 11,
      title: "Naruto (2002 - 2007)",
      subtitle: "feat. Masashi Kishimoto",
      rating: 4.8,
      reviews: "6.7k recenzji",
      image: "/api/placeholder/250/350"
    },
    {
      id: 12,
      title: "Dom grozy (1997)",
      subtitle: "feat. John Logan",
      rating: 3.9,
      reviews: "2.1k recenzji",
      image: "/api/placeholder/250/350"
    }
  ]

  return (
    <div className="tv-shows-container">
      <div className="tv-shows-grid">
        {shows.map(show => (
          <div key={show.id} className="tv-show-card">
            <div className="tv-show-image">
              <img src={show.image} alt={show.title} />
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
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default TVShowsGrid