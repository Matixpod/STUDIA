import React from 'react'
import { Star } from 'lucide-react'

const TrendingSection = () => {
  const trendingItems = [
    { id: 1, title: 'The Last Chapter', rating: 4.3, category: 'Drama' },
    { id: 2, title: 'Beyond Tomorrow', rating: 4.5, category: 'Sci-Fi' },
    { id: 3, title: 'Laugh Out Loud', rating: 4.7, category: 'Comedy' }
  ]

  return (
    <section className="trending-section">
      <h2 className="section-title">Trending Now</h2>
      
      <div className="trending-grid">
        {trendingItems.map(item => (
          <div key={item.id} className="trending-card">
            <div className="movie-placeholder">
              400 × 600
            </div>
            <h3 className="movie-title">{item.title}</h3>
            <div className="movie-info">
              <div className="rating">
                <Star size={16} fill="#ffd700" color="#ffd700" />
                <span>{item.rating}</span>
              </div>
              <span className="category">{item.category}</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  )
}

export default TrendingSection