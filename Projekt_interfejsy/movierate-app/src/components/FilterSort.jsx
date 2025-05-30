import React from 'react'
import { Filter, TrendingUp, Star, Calendar } from 'lucide-react'

const FilterSort = ({ 
  genres = [], 
  selectedGenre, 
  onGenreChange, 
  sortBy, 
  onSortChange,
  type = 'movies' 
}) => {
  return (
    <div className="filter-sort-container">
      <div className="filter-section">
        <div className="filter-header">
          <Filter size={18} />
          <span>Filtruj po gatunku:</span>
        </div>
        <div className="genre-filters">
          <button 
            className={`genre-btn ${selectedGenre === 'all' ? 'active' : ''}`}
            onClick={() => onGenreChange('all')}
          >
            Wszystkie
          </button>
          {genres.map(genre => (
            <button 
              key={genre}
              className={`genre-btn ${selectedGenre === genre ? 'active' : ''}`}
              onClick={() => onGenreChange(genre)}
            >
              {genre}
            </button>
          ))}
        </div>
      </div>

      <div className="sort-section">
        <div className="sort-header">
          <TrendingUp size={18} />
          <span>Sortuj według:</span>
        </div>
        <div className="sort-options">
          <button 
            className={`sort-btn ${sortBy === 'popularity' ? 'active' : ''}`}
            onClick={() => onSortChange('popularity')}
          >
            <TrendingUp size={16} />
            Popularność
          </button>
          <button 
            className={`sort-btn ${sortBy === 'rating' ? 'active' : ''}`}
            onClick={() => onSortChange('rating')}
          >
            <Star size={16} />
            Ocena
          </button>
          <button 
            className={`sort-btn ${sortBy === 'newest' ? 'active' : ''}`}
            onClick={() => onSortChange('newest')}
          >
            <Calendar size={16} />
            Najnowsze
          </button>
          <button 
            className={`sort-btn ${sortBy === 'alphabetical' ? 'active' : ''}`}
            onClick={() => onSortChange('alphabetical')}
          >
            A-Z
          </button>
        </div>
      </div>
    </div>
  )
}

export default FilterSort